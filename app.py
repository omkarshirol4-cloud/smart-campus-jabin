# app.py
# Main Flask application for KLE Society's P.C. Jabin Science College
# Smart Campus Operations and Facility Booking Platform (BCA Department).

import functools
from datetime import date, datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import database

# Initialize the Flask application
app = Flask(__name__)
# Secret key used by Flask to securely sign session cookies
app.secret_key = "pc-jabin-science-college-bca-smart-campus-key-2026"

# Ensure database and seed data are initialized automatically on boot
database.init_db()


# Standard operating booking time slots (9:00 AM to 5:00 PM)
TIME_SLOTS = [
    "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00"
]


# Helper Decorator: Ensures a user is logged in before accessing a page
def login_required(view_func):
    @functools.wraps(view_func)
    def wrapped_view(*args, **kwargs):
        if "user_id" not in session:
            flash("Please sign in to access this page.", "error")
            return redirect(url_for("login"))
        return view_func(*args, **kwargs)
    return wrapped_view


@app.route("/")
def index():
    """
    Default route: redirect to dashboard if logged in, otherwise go to login page.
    """
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Handle user login: supports existing demo accounts and allows entering
    ANY custom name/email and password for student and faculty testing.
    The exact username/name entered will be displayed in the header.
    """
    # If already logged in, redirect directly to dashboard
    if "user_id" in session:
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        raw_input = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()
        role = request.form.get("role", "student").strip().lower()

        # Fallback to student role if unexpected value
        if role not in ["student", "staff", "admin"]:
            role = "student"

        if not raw_input:
            flash("Please enter a username or email address.", "error")
            return render_template("login.html")

        if not password:
            flash("Please enter a password.", "error")
            return render_template("login.html")

        # Determine email and display name from user input
        if "@" in raw_input:
            email = raw_input.lower()
            name_part = raw_input.split("@")[0].replace(".", " ").replace("_", " ")
            display_name = name_part.title()
        else:
            # User entered a plain name like "Omkar" or "Rahul Patil"
            display_name = raw_input
            email = raw_input.lower().replace(" ", ".") + "@campus.edu"

        conn = database.get_db()
        cursor = conn.cursor()

        # Check if user already exists in database
        user = cursor.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()

        if user:
            # Check existing user's password
            # If it's a demo account, enforce password verification
            if email in ["student@demo.edu", "staff@demo.edu", "admin@demo.edu"]:
                if not check_password_hash(user["password_hash"], password):
                    conn.close()
                    flash("Invalid demo password. Please use password123.", "error")
                    return render_template("login.html")
            else:
                # For custom user testing, accept password and update hash if changed
                if not check_password_hash(user["password_hash"], password):
                    new_hash = generate_password_hash(password)
                    cursor.execute("UPDATE users SET password_hash = ? WHERE id = ?", (new_hash, user["id"]))
                    conn.commit()

            user_id = user["id"]
            user_role = user["role"]
            user_dept = user["department"]
            display_name = display_name if display_name else user["full_name"]

        else:
            # Automatically register a new user on the fly for testing
            dept = "BCA Student" if role == "student" else ("BCA Faculty" if role == "staff" else "Administration")
            hashed_pw = generate_password_hash(password)

            cursor.execute("""
                INSERT INTO users (email, password_hash, full_name, role, department)
                VALUES (?, ?, ?, ?, ?)
            """, (email, hashed_pw, display_name, role, dept))
            conn.commit()
            user_id = cursor.lastrowid
            user_role = role
            user_dept = dept

            # Add welcome notification for new user
            cursor.execute("""
                INSERT INTO notifications (user_id, title, message)
                VALUES (?, ?, ?)
            """, (user_id, "Welcome to Smart Campus!", f"Welcome {display_name}! You can now book facilities and check availability."))
            conn.commit()

        # Save user identity in session (display_name will show in header)
        session["user_id"] = user_id
        session["user_email"] = email
        session["user_name"] = display_name
        session["user_role"] = user_role
        session["user_dept"] = user_dept

        # Record login action into the audit trail
        cursor.execute(
            "INSERT INTO audit_logs (user_id, user_email, action, details) VALUES (?, ?, ?, ?)",
            (user_id, email, "LOGIN", f"User '{display_name}' logged in as {user_role}.")
        )
        conn.commit()
        conn.close()

        flash(f"Welcome, {display_name}!", "success")
        return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/dashboard")
@login_required
def dashboard():
    """
    Route users to their respective role-based home page (Student / Staff / Admin).
    """
    role = session.get("user_role")
    user_id = session.get("user_id")

    conn = database.get_db()
    user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    total_resources = conn.execute("SELECT COUNT(*) AS count FROM resources WHERE is_active = 1").fetchone()["count"]

    if role == "student":
        # Fetch student's real bookings and issues from SQLite
        bookings = conn.execute("""
            SELECT b.*, r.name as resource_name, r.type as resource_type, r.location as resource_location
            FROM bookings b 
            JOIN resources r ON b.resource_id = r.id 
            WHERE b.user_id = ? 
            ORDER BY b.created_at DESC
        """, (user_id,)).fetchall()

        issues = conn.execute("SELECT * FROM issues WHERE user_id = ?", (user_id,)).fetchall()
        notifications = conn.execute("SELECT * FROM notifications WHERE user_id = ? ORDER BY created_at DESC", (user_id,)).fetchall()
        conn.close()

        return render_template(
            "dashboard_student.html",
            user=user,
            bookings=bookings,
            issues=issues,
            notifications=notifications,
            total_resources=total_resources
        )

    elif role == "staff":
        # Fetch staff member's real bookings and issues from SQLite
        bookings = conn.execute("""
            SELECT b.*, r.name as resource_name, r.type as resource_type, r.location as resource_location
            FROM bookings b 
            JOIN resources r ON b.resource_id = r.id 
            WHERE b.user_id = ? 
            ORDER BY b.created_at DESC
        """, (user_id,)).fetchall()

        issues = conn.execute("SELECT * FROM issues WHERE user_id = ?", (user_id,)).fetchall()
        notifications = conn.execute("SELECT * FROM notifications WHERE user_id = ? ORDER BY created_at DESC", (user_id,)).fetchall()
        conn.close()

        return render_template(
            "dashboard_staff.html",
            user=user,
            bookings=bookings,
            issues=issues,
            notifications=notifications,
            total_resources=total_resources
        )

    elif role == "admin":
        # Fetch administrator overview data
        # All pending booking requests from both students and faculty
        pending_bookings = conn.execute("""
            SELECT b.*, u.full_name as user_name, u.role as user_role, u.department as user_dept, 
                   r.name as resource_name, r.location as resource_location
            FROM bookings b
            JOIN users u ON b.user_id = u.id
            JOIN resources r ON b.resource_id = r.id
            WHERE b.status = 'pending'
            ORDER BY b.created_at DESC
        """).fetchall()

        # All bookings across campus for full visibility
        all_bookings = conn.execute("""
            SELECT b.*, u.full_name as user_name, u.role as user_role, u.department as user_dept, 
                   r.name as resource_name, r.location as resource_location
            FROM bookings b
            JOIN users u ON b.user_id = u.id
            JOIN resources r ON b.resource_id = r.id
            ORDER BY b.created_at DESC
        """).fetchall()

        approved_count = conn.execute("SELECT COUNT(*) AS count FROM bookings WHERE status = 'approved'").fetchone()["count"]

        open_issues = conn.execute("""
            SELECT i.*, r.name as resource_name
            FROM issues i
            LEFT JOIN resources r ON i.resource_id = r.id
            WHERE i.status != 'resolved'
            ORDER BY i.created_at DESC
        """).fetchall()

        total_classes = conn.execute("SELECT COUNT(*) AS count FROM timetable_classes").fetchone()["count"]
        audit_logs = conn.execute("SELECT * FROM audit_logs ORDER BY created_at DESC LIMIT 15").fetchall()
        conn.close()

        return render_template(
            "dashboard_admin.html",
            user=user,
            pending_bookings=pending_bookings,
            all_bookings=all_bookings,
            approved_count=approved_count,
            open_issues=open_issues,
            audit_logs=audit_logs,
            total_resources=total_resources,
            total_classes=total_classes
        )

    conn.close()
    flash("Unknown user role.", "error")
    return redirect(url_for("logout"))


@app.route("/book", methods=["GET", "POST"])
@login_required
def book_facility():
    """
    Facility and equipment booking page for students and staff.
    Performs full input validation and blocks double-bookings.
    All student and faculty reservation requests start as 'pending' for admin review.
    """
    conn = database.get_db()
    today_str = date.today().isoformat()

    if request.method == "POST":
        user_id = session.get("user_id")
        user_email = session.get("user_email")
        user_role = session.get("user_role")

        resource_id = request.form.get("resource_id", "").strip()
        booking_date = request.form.get("booking_date", "").strip()
        start_time = request.form.get("start_time", "").strip()
        end_time = request.form.get("end_time", "").strip()
        purpose = request.form.get("purpose", "").strip()

        # 1. Basic field validation
        if not resource_id or not booking_date or not start_time or not end_time or not purpose:
            flash("All fields are required to reserve a facility.", "error")
            resources = conn.execute("SELECT * FROM resources WHERE is_active = 1 ORDER BY type, name").fetchall()
            conn.close()
            return render_template("book.html", resources=resources, today=today_str, time_slots=TIME_SLOTS)

        # 2. Prevent past dates
        try:
            parsed_date = datetime.strptime(booking_date, "%Y-%m-%d").date()
            if parsed_date < date.today():
                flash("Invalid booking date. You cannot reserve facilities for dates in the past.", "error")
                resources = conn.execute("SELECT * FROM resources WHERE is_active = 1 ORDER BY type, name").fetchall()
                conn.close()
                return render_template("book.html", resources=resources, today=today_str, time_slots=TIME_SLOTS)
        except ValueError:
            flash("Invalid date format.", "error")
            resources = conn.execute("SELECT * FROM resources WHERE is_active = 1 ORDER BY type, name").fetchall()
            conn.close()
            return render_template("book.html", resources=resources, today=today_str, time_slots=TIME_SLOTS)

        # 3. Validate operating hours and sequence (End must be after Start)
        if start_time not in TIME_SLOTS or end_time not in TIME_SLOTS:
            flash("Bookings are only permitted during campus hours (09:00 AM to 05:00 PM).", "error")
            resources = conn.execute("SELECT * FROM resources WHERE is_active = 1 ORDER BY type, name").fetchall()
            conn.close()
            return render_template("book.html", resources=resources, today=today_str, time_slots=TIME_SLOTS)

        if start_time >= end_time:
            flash("Invalid time selection: End time must be later than start time.", "error")
            resources = conn.execute("SELECT * FROM resources WHERE is_active = 1 ORDER BY type, name").fetchall()
            conn.close()
            return render_template("book.html", resources=resources, today=today_str, time_slots=TIME_SLOTS)

        # 4. Check resource existence
        resource = conn.execute("SELECT * FROM resources WHERE id = ? AND is_active = 1", (resource_id,)).fetchone()
        if not resource:
            flash("Selected facility was not found.", "error")
            resources = conn.execute("SELECT * FROM resources WHERE is_active = 1 ORDER BY type, name").fetchall()
            conn.close()
            return render_template("book.html", resources=resources, today=today_str, time_slots=TIME_SLOTS)

        # 4B. TIMETABLE CURRICULUM CLASS CHECK:
        # Check if an official curriculum class is scheduled in this room/lab at this time
        day_of_week = parsed_date.strftime("%A")  # 'Monday', 'Tuesday', ...
        if day_of_week == "Sunday":
            flash("Campus facilities are closed on Sundays. Please select a date from Monday to Saturday.", "error")
            resources = conn.execute("SELECT * FROM resources WHERE is_active = 1 ORDER BY type, name").fetchall()
            conn.close()
            return render_template("book.html", resources=resources, today=today_str, time_slots=TIME_SLOTS, selected_resource_id=int(resource_id))

        timetable_conflict = conn.execute("""
            SELECT * FROM timetable_classes
            WHERE resource_id = ?
              AND day_of_week = ?
              AND (start_time < ? AND end_time > ?)
        """, (resource_id, day_of_week, end_time, start_time)).fetchone()

        if timetable_conflict:
            flash(
                f"Timetable Conflict Blocked! '{resource['name']}' is assigned on {day_of_week}s "
                f"from {timetable_conflict['start_time']} to {timetable_conflict['end_time']} "
                f"for scheduled class: '{timetable_conflict['course_name']}' ({timetable_conflict['division']}). "
                f"Official academic classes cannot be displaced by manual bookings.",
                "error"
            )
            resources = conn.execute("SELECT * FROM resources WHERE is_active = 1 ORDER BY type, name").fetchall()
            conn.close()
            return render_template("book.html", resources=resources, today=today_str, time_slots=TIME_SLOTS, selected_resource_id=int(resource_id))

        # 5. DOUBLE-BOOKING CHECK:
        # Check if another booking for this resource on this date overlaps with requested slot
        conflict = conn.execute("""
            SELECT b.*, u.full_name as booked_by
            FROM bookings b
            JOIN users u ON b.user_id = u.id
            WHERE b.resource_id = ?
              AND b.booking_date = ?
              AND b.status IN ('pending', 'approved')
              AND (b.start_time < ? AND b.end_time > ?)
        """, (resource_id, booking_date, end_time, start_time)).fetchone()

        if conflict:
            flash(
                f"Double Booking Blocked! '{resource['name']}' is already booked on {booking_date} "
                f"between {conflict['start_time']} and {conflict['end_time']} "
                f"(Reserved by: {conflict['booked_by']}, Status: {conflict['status'].capitalize()}). "
                f"Please select a different time slot or facility.",
                "error"
            )
            resources = conn.execute("SELECT * FROM resources WHERE is_active = 1 ORDER BY type, name").fetchall()
            conn.close()
            return render_template("book.html", resources=resources, today=today_str, time_slots=TIME_SLOTS, selected_resource_id=int(resource_id))

        # 6. Save the booking
        # All requests from students and faculty start as 'pending' so Admin can review and approve them!
        initial_status = "pending"
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO bookings (user_id, resource_id, booking_date, start_time, end_time, purpose, status)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (user_id, resource_id, booking_date, start_time, end_time, purpose, initial_status))
        booking_id = cursor.lastrowid

        # 7. Add in-app notification for the user
        cursor.execute("""
            INSERT INTO notifications (user_id, title, message)
            VALUES (?, ?, ?)
        """, (
            user_id,
            "Booking Request Submitted",
            f"Your request for {resource['name']} on {booking_date} ({start_time} - {end_time}) has been submitted for admin approval."
        ))

        # 8. Record in audit trail
        cursor.execute("""
            INSERT INTO audit_logs (user_id, user_email, action, details)
            VALUES (?, ?, ?, ?)
        """, (
            user_id,
            user_email,
            "CREATE_BOOKING",
            f"Booking request #{booking_id} submitted for {resource['name']} ({booking_date} {start_time}-{end_time})."
        ))

        conn.commit()
        conn.close()

        flash(f"Success! Your booking request #{booking_id} for '{resource['name']}' on {booking_date} ({start_time} - {end_time}) was submitted and is pending administrator approval.", "success")
        return redirect(url_for("dashboard"))

    # GET Request: Show booking form
    selected_resource_id = request.args.get("resource_id", type=int)
    resources = conn.execute("SELECT * FROM resources WHERE is_active = 1 ORDER BY type, name").fetchall()
    conn.close()

    return render_template(
        "book.html",
        resources=resources,
        today=today_str,
        time_slots=TIME_SLOTS,
        selected_resource_id=selected_resource_id
    )


@app.route("/api/check-availability")
def api_check_availability():
    """
    Real-time availability check API for the booking form.
    Immediately verifies whether the selected room, date, and time slot conflicts
    with an ongoing curriculum class or existing reservation.
    """
    resource_id = request.args.get("resource_id", type=int)
    booking_date = request.args.get("booking_date", "").strip()
    start_time = request.args.get("start_time", "").strip()
    end_time = request.args.get("end_time", "").strip()

    if not resource_id or not booking_date or not start_time or not end_time:
        return jsonify({"status": "incomplete", "available": True, "message": ""})

    if start_time >= end_time:
        return jsonify({
            "status": "invalid_time",
            "available": False,
            "message": "End time must be later than start time."
        })

    try:
        parsed_date = datetime.strptime(booking_date, "%Y-%m-%d").date()
    except ValueError:
        return jsonify({"status": "invalid_date", "available": False, "message": "Invalid date format."})

    day_of_week = parsed_date.strftime("%A")
    if day_of_week == "Sunday":
        return jsonify({
            "status": "sunday",
            "available": False,
            "message": "Campus facilities are closed on Sundays. Facility cannot be booked."
        })

    conn = database.get_db()
    resource = conn.execute("SELECT * FROM resources WHERE id = ? AND is_active = 1", (resource_id,)).fetchone()
    if not resource:
        conn.close()
        return jsonify({"status": "not_found", "available": False, "message": "Facility not found."})

    # 1. Timetable Class Conflict Check
    timetable_conflict = conn.execute("""
        SELECT * FROM timetable_classes
        WHERE resource_id = ?
          AND day_of_week = ?
          AND (start_time < ? AND end_time > ?)
    """, (resource_id, day_of_week, end_time, start_time)).fetchone()

    if timetable_conflict:
        conn.close()
        return jsonify({
            "status": "timetable_conflict",
            "available": False,
            "room_name": resource["name"],
            "course_name": timetable_conflict["course_name"],
            "division": timetable_conflict["division"],
            "start_time": timetable_conflict["start_time"],
            "end_time": timetable_conflict["end_time"],
            "day_of_week": day_of_week,
            "message": f"Class in Session: '{timetable_conflict['course_name']}' ({timetable_conflict['division']}) is scheduled in {resource['name']} from {timetable_conflict['start_time']} to {timetable_conflict['end_time']} on {day_of_week}s. You cannot book this room."
        })

    # 2. Peer Booking Conflict Check
    conflict = conn.execute("""
        SELECT b.*, u.full_name as booked_by
        FROM bookings b
        JOIN users u ON b.user_id = u.id
        WHERE b.resource_id = ?
          AND b.booking_date = ?
          AND b.status IN ('pending', 'approved')
          AND (b.start_time < ? AND b.end_time > ?)
    """, (resource_id, booking_date, end_time, start_time)).fetchone()

    if conflict:
        conn.close()
        return jsonify({
            "status": "booking_conflict",
            "available": False,
            "room_name": resource["name"],
            "booked_by": conflict["booked_by"],
            "start_time": conflict["start_time"],
            "end_time": conflict["end_time"],
            "message": f"Already Booked: '{resource['name']}' is already reserved on {booking_date} from {conflict['start_time']} to {conflict['end_time']} by {conflict['booked_by']}."
        })

    conn.close()
    return jsonify({
        "status": "available",
        "available": True,
        "room_name": resource["name"],
        "message": f"'{resource['name']}' is free and available on {booking_date} from {start_time} to {end_time}."
    })


@app.route("/api/room-schedule")
def api_room_schedule():
    """
    Returns the list of classes scheduled in the selected room on the given date's day-of-week.
    Used by the booking form to display which hours are taken.
    """
    resource_id = request.args.get("resource_id", type=int)
    booking_date = request.args.get("booking_date", "").strip()

    if not resource_id or not booking_date:
        return jsonify({"classes": [], "day_of_week": ""})

    try:
        parsed_date = datetime.strptime(booking_date, "%Y-%m-%d").date()
        day_of_week = parsed_date.strftime("%A")
    except ValueError:
        return jsonify({"classes": [], "day_of_week": ""})

    conn = database.get_db()
    classes = conn.execute("""
        SELECT start_time, end_time, course_name, division
        FROM timetable_classes
        WHERE resource_id = ? AND day_of_week = ?
        ORDER BY start_time
    """, (resource_id, day_of_week)).fetchall()
    conn.close()

    return jsonify({
        "day_of_week": day_of_week,
        "classes": [dict(c) for c in classes]
    })


@app.route("/admin/bookings/<int:booking_id>/approve", methods=["POST"])
@login_required
def admin_approve_booking(booking_id):
    """
    Administrator endpoint to approve a pending booking request.
    """
    if session.get("user_role") != "admin":
        flash("Unauthorized. Admin access required.", "error")
        return redirect(url_for("dashboard"))

    conn = database.get_db()
    cursor = conn.cursor()
    booking = cursor.execute("""
        SELECT b.*, u.full_name as user_name, r.name as resource_name 
        FROM bookings b 
        JOIN users u ON b.user_id = u.id 
        JOIN resources r ON b.resource_id = r.id 
        WHERE b.id = ?
    """, (booking_id,)).fetchone()

    if not booking:
        conn.close()
        flash("Booking request not found.", "error")
        return redirect(url_for("dashboard"))

    cursor.execute("UPDATE bookings SET status = 'approved', updated_at = CURRENT_TIMESTAMP WHERE id = ?", (booking_id,))

    # Notify requester
    cursor.execute("""
        INSERT INTO notifications (user_id, title, message)
        VALUES (?, ?, ?)
    """, (
        booking["user_id"],
        "Booking Approved! 🎉",
        f"Your reservation for {booking['resource_name']} on {booking['booking_date']} ({booking['start_time']} - {booking['end_time']}) has been approved by the Admin."
    ))

    # Audit log
    cursor.execute("""
        INSERT INTO audit_logs (user_id, user_email, action, details)
        VALUES (?, ?, ?, ?)
    """, (
        session.get("user_id"),
        session.get("user_email"),
        "APPROVE_BOOKING",
        f"Admin approved booking #{booking_id} for {booking['resource_name']} (Requested by {booking['user_name']})."
    ))

    conn.commit()
    conn.close()

    flash(f"Booking #{booking_id} for '{booking['resource_name']}' has been approved.", "success")
    return redirect(url_for("dashboard"))


@app.route("/admin/bookings/<int:booking_id>/reject", methods=["POST"])
@login_required
def admin_reject_booking(booking_id):
    """
    Administrator endpoint to reject a pending booking request.
    """
    if session.get("user_role") != "admin":
        flash("Unauthorized. Admin access required.", "error")
        return redirect(url_for("dashboard"))

    conn = database.get_db()
    cursor = conn.cursor()
    booking = cursor.execute("""
        SELECT b.*, u.full_name as user_name, r.name as resource_name 
        FROM bookings b 
        JOIN users u ON b.user_id = u.id 
        JOIN resources r ON b.resource_id = r.id 
        WHERE b.id = ?
    """, (booking_id,)).fetchone()

    if not booking:
        conn.close()
        flash("Booking request not found.", "error")
        return redirect(url_for("dashboard"))

    cursor.execute("UPDATE bookings SET status = 'rejected', admin_notes = 'Declined by administration', updated_at = CURRENT_TIMESTAMP WHERE id = ?", (booking_id,))

    # Notify requester
    cursor.execute("""
        INSERT INTO notifications (user_id, title, message)
        VALUES (?, ?, ?)
    """, (
        booking["user_id"],
        "Booking Request Declined",
        f"Your reservation for {booking['resource_name']} on {booking['booking_date']} was declined by the Admin."
    ))

    # Audit log
    cursor.execute("""
        INSERT INTO audit_logs (user_id, user_email, action, details)
        VALUES (?, ?, ?, ?)
    """, (
        session.get("user_id"),
        session.get("user_email"),
        "REJECT_BOOKING",
        f"Admin rejected booking #{booking_id} for {booking['resource_name']} (Requested by {booking['user_name']})."
    ))

    conn.commit()
    conn.close()

    flash(f"Booking #{booking_id} for '{booking['resource_name']}' was declined.", "info")
    return redirect(url_for("dashboard"))


@app.route("/bookings/<int:booking_id>/cancel", methods=["POST"])
@login_required
def cancel_booking(booking_id):
    """
    Cancel an existing booking made by the user.
    """
    user_id = session.get("user_id")
    user_email = session.get("user_email")
    user_role = session.get("user_role")

    conn = database.get_db()
    cursor = conn.cursor()

    # Find booking
    booking = cursor.execute("""
        SELECT b.*, r.name as resource_name 
        FROM bookings b 
        JOIN resources r ON b.resource_id = r.id 
        WHERE b.id = ?
    """, (booking_id,)).fetchone()

    if not booking:
        conn.close()
        flash("Booking not found.", "error")
        return redirect(url_for("dashboard"))

    # Only the owner or an admin can cancel
    if booking["user_id"] != user_id and user_role != "admin":
        conn.close()
        flash("You are not authorized to cancel this booking.", "error")
        return redirect(url_for("dashboard"))

    if booking["status"] in ["cancelled", "rejected"]:
        conn.close()
        flash(f"This booking is already {booking['status']}.", "info")
        return redirect(url_for("dashboard"))

    # Update status to cancelled
    cursor.execute("UPDATE bookings SET status = 'cancelled', updated_at = CURRENT_TIMESTAMP WHERE id = ?", (booking_id,))

    # Add notification
    cursor.execute("""
        INSERT INTO notifications (user_id, title, message)
        VALUES (?, ?, ?)
    """, (
        booking["user_id"],
        "Booking Cancelled",
        f"Your reservation for {booking['resource_name']} on {booking['booking_date']} has been cancelled."
    ))

    # Log in audit trail
    cursor.execute("""
        INSERT INTO audit_logs (user_id, user_email, action, details)
        VALUES (?, ?, ?, ?)
    """, (
        user_id,
        user_email,
        "CANCEL_BOOKING",
        f"Booking #{booking_id} for {booking['resource_name']} was cancelled by {user_email}."
    ))

    conn.commit()
    conn.close()

    flash(f"Booking #{booking_id} for {booking['resource_name']} was successfully cancelled.", "info")
    return redirect(url_for("dashboard"))


@app.route("/resources")
@login_required
def list_resources():
    """
    List all rooms and laboratories with search, weekly schedule insights, and live availability checker.
    """
    query = request.args.get("q", "").strip()
    r_type = request.args.get("type", "").strip()
    check_date = request.args.get("date", "").strip()
    check_start = request.args.get("start", "").strip()
    check_end = request.args.get("end", "").strip()

    conn = database.get_db()
    sql = "SELECT * FROM resources WHERE is_active = 1"
    params = []

    if query:
        sql += " AND (name LIKE ? OR description LIKE ? OR location LIKE ?)"
        wildcard = f"%{query}%"
        params.extend([wildcard, wildcard, wildcard])

    if r_type and r_type in ["Room", "Equipment"]:
        sql += " AND type = ?"
        params.append(r_type)

    sql += " ORDER BY type, name"
    resources = conn.execute(sql, params).fetchall()

    # Preload scheduled classes for each resource to show on cards
    all_schedules = conn.execute("""
        SELECT resource_id, day_of_week, start_time, end_time, course_name, division
        FROM timetable_classes
        ORDER BY CASE day_of_week WHEN 'Monday' THEN 1 WHEN 'Tuesday' THEN 2 WHEN 'Wednesday' THEN 3 WHEN 'Thursday' THEN 4 WHEN 'Friday' THEN 5 WHEN 'Saturday' THEN 6 ELSE 7 END, start_time
    """).fetchall()
    
    resource_classes_map = {}
    for s in all_schedules:
        rid = s["resource_id"]
        if rid not in resource_classes_map:
            resource_classes_map[rid] = []
        resource_classes_map[rid].append(dict(s))

    # If availability filter is specified, check both user bookings AND timetable classes
    busy_resource_ids = set()
    timetable_busy_map = {}
    booking_busy_map = {}

    if check_date and check_start and check_end and check_start < check_end:
        # 1. User reservations
        conflicts = conn.execute("""
            SELECT resource_id, start_time, end_time, purpose 
            FROM bookings 
            WHERE booking_date = ? 
              AND status IN ('pending', 'approved')
              AND (start_time < ? AND end_time > ?)
        """, (check_date, check_end, check_start)).fetchall()
        for c in conflicts:
            busy_resource_ids.add(c["resource_id"])
            booking_busy_map[c["resource_id"]] = f"Reserved ({c['start_time']}-{c['end_time']})"

        # 2. Timetable curriculum classes
        try:
            day_name = datetime.strptime(check_date, "%Y-%m-%d").strftime("%A")
            if day_name != "Sunday":
                t_conflicts = conn.execute("""
                    SELECT resource_id, course_name, division, start_time, end_time
                    FROM timetable_classes
                    WHERE day_of_week = ?
                      AND (start_time < ? AND end_time > ?)
                """, (day_name, check_end, check_start)).fetchall()
                for tc in t_conflicts:
                    busy_resource_ids.add(tc["resource_id"])
                    timetable_busy_map[tc["resource_id"]] = f"{tc['course_name']} ({tc['division']})"
        except ValueError:
            pass

    conn.close()

    return render_template(
        "resources.html",
        resources=resources,
        query=query,
        selected_type=r_type,
        check_date=check_date,
        check_start=check_start,
        check_end=check_end,
        busy_resource_ids=busy_resource_ids,
        timetable_busy_map=timetable_busy_map,
        booking_busy_map=booking_busy_map,
        resource_classes_map=resource_classes_map,
        time_slots=TIME_SLOTS,
        today=date.today().isoformat()
    )


@app.route("/timetable")
@login_required
def view_timetable():
    """
    Timetable display has been removed per user preference.
    Redirects to facilities catalog where availability and conflict prevention are enforced.
    """
    return redirect(url_for("list_resources"))


@app.route("/logout")
def logout():
    """
    Log out the current user, record in audit log, and clear the session.
    """
    user_id = session.get("user_id")
    user_email = session.get("user_email")

    if user_id and user_email:
        conn = database.get_db()
        conn.execute(
            "INSERT INTO audit_logs (user_id, user_email, action, details) VALUES (?, ?, ?, ?)",
            (user_id, user_email, "LOGOUT", "User logged out.")
        )
        conn.commit()
        conn.close()

    session.clear()
    flash("You have been signed out successfully.", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    # Ensure database and tables exist on application startup
    database.init_db()
    print("Starting Smart Campus Platform for KLE P.C. Jabin Science College...")
    print("Application URL: http://127.0.0.1:5000")
    app.run(host="127.0.0.1", port=5000, debug=True)
