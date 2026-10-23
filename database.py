# database.py
# SQLite database setup and demo data seeder.
# This file creates the tables and loads seed_data.py on first start.

import sqlite3
import os
from werkzeug.security import generate_password_hash
import seed_data

# The single SQLite database file stored in the project folder
DB_FILE = os.path.join(os.path.dirname(__file__), "campus.db")


def get_db():
    """
    Connect to the SQLite database.
    row_factory = sqlite3.Row allows accessing columns by name, like row['email'].
    """
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    # Enable foreign keys support in SQLite
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    """
    Create all required tables if they don't already exist.
    """
    conn = get_db()
    cursor = conn.cursor()

    # 1. Users Table (student, staff, admin)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        full_name TEXT NOT NULL,
        role TEXT NOT NULL CHECK(role IN ('student', 'staff', 'admin')),
        department TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 2. Resources Table (Rooms and Equipment)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resources (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        type TEXT NOT NULL CHECK(type IN ('Room', 'Equipment')),
        capacity INTEGER NOT NULL DEFAULT 1,
        location TEXT NOT NULL,
        description TEXT NOT NULL,
        is_active INTEGER NOT NULL DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 3. Bookings Table (facility reservations)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        resource_id INTEGER NOT NULL REFERENCES resources(id) ON DELETE CASCADE,
        booking_date TEXT NOT NULL,
        start_time TEXT NOT NULL,
        end_time TEXT NOT NULL,
        purpose TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'pending' CHECK(status IN ('pending', 'approved', 'rejected', 'cancelled')),
        admin_notes TEXT DEFAULT '',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 4. Issues Table (maintenance reports)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS issues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        resource_id INTEGER REFERENCES resources(id) ON DELETE SET NULL,
        title TEXT NOT NULL,
        category TEXT NOT NULL,
        description TEXT NOT NULL,
        priority TEXT NOT NULL DEFAULT 'medium' CHECK(priority IN ('low', 'medium', 'high', 'urgent')),
        status TEXT NOT NULL DEFAULT 'open' CHECK(status IN ('open', 'in_progress', 'resolved')),
        admin_response TEXT DEFAULT '',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 5. Audit Logs Table (tracks who did what and when)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS audit_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        user_email TEXT NOT NULL,
        action TEXT NOT NULL,
        details TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 6. Notifications Table (in-app alerts for users)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notifications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
        title TEXT NOT NULL,
        message TEXT NOT NULL,
        is_read INTEGER NOT NULL DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 7. Timetable Classes Table (official recurring weekly academic curriculum classes)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS timetable_classes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        resource_id INTEGER NOT NULL REFERENCES resources(id) ON DELETE CASCADE,
        day_of_week TEXT NOT NULL CHECK(day_of_week IN ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')),
        start_time TEXT NOT NULL,
        end_time TEXT NOT NULL,
        course_name TEXT NOT NULL,
        division TEXT NOT NULL,
        faculty_title TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    conn.commit()

    # Automatically load demo data if database is fresh (empty users table)
    cursor.execute("SELECT COUNT(*) AS count FROM users")
    if cursor.fetchone()["count"] == 0:
        seed_database(conn)

    conn.close()


def seed_database(conn):
    """
    Populate demo data from seed_data.py into the SQLite database.
    """
    cursor = conn.cursor()

    # 1. Insert Users
    user_id_map = {}
    for u in seed_data.USERS:
        # We store the securely hashed password rather than plain text
        hashed_pw = generate_password_hash(u["password"])
        cursor.execute("""
            INSERT INTO users (email, password_hash, full_name, role, department)
            VALUES (?, ?, ?, ?, ?)
        """, (u["email"], hashed_pw, u["full_name"], u["role"], u["department"]))
        user_id_map[u["email"]] = cursor.lastrowid

    # 2. Insert Resources
    resource_id_map = {}
    for r in seed_data.RESOURCES:
        cursor.execute("""
            INSERT INTO resources (name, type, capacity, location, description)
            VALUES (?, ?, ?, ?, ?)
        """, (r["name"], r["type"], r["capacity"], r["location"], r["description"]))
        resource_id_map[r["name"]] = cursor.lastrowid

    # 3. Insert Sample Bookings
    for b in seed_data.SAMPLE_BOOKINGS:
        u_id = user_id_map.get(b["user_email"])
        r_id = resource_id_map.get(b["resource_name"])
        if u_id and r_id:
            cursor.execute("""
                INSERT INTO bookings (user_id, resource_id, booking_date, start_time, end_time, purpose, status, admin_notes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (u_id, r_id, b["booking_date"], b["start_time"], b["end_time"], b["purpose"], b["status"], b["admin_notes"]))

    # 4. Insert Sample Issues
    for iss in seed_data.SAMPLE_ISSUES:
        u_id = user_id_map.get(iss["user_email"])
        r_id = resource_id_map.get(iss["resource_name"])
        if u_id:
            cursor.execute("""
                INSERT INTO issues (user_id, resource_id, title, category, description, priority, status, admin_response)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (u_id, r_id, iss["title"], iss["category"], iss["description"], iss["priority"], iss["status"], iss["admin_response"]))

    # 5. Insert Sample Notifications
    for n in seed_data.SAMPLE_NOTIFICATIONS:
        u_id = user_id_map.get(n["user_email"])
        if u_id:
            cursor.execute("""
                INSERT INTO notifications (user_id, title, message)
                VALUES (?, ?, ?)
            """, (u_id, n["title"], n["message"]))

    # 6. Insert Timetable Classes from seed_data.py
    if hasattr(seed_data, "TIMETABLE_CLASSES"):
        for tc in seed_data.TIMETABLE_CLASSES:
            r_id = resource_id_map.get(tc["resource_name"])
            if r_id:
                cursor.execute("""
                    INSERT INTO timetable_classes (resource_id, day_of_week, start_time, end_time, course_name, division, faculty_title)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (r_id, tc["day_of_week"], tc["start_time"], tc["end_time"], tc["course_name"], tc["division"], tc["faculty_title"]))

    # 7. Record Initial Audit Log
    cursor.execute("""
        INSERT INTO audit_logs (user_email, action, details)
        VALUES ('system', 'SYSTEM_INITIALIZATION', 'Database created and populated with demo resources, timetable classes, and users.')
    """)

    conn.commit()
    print("Database initialized and demo data loaded successfully!")


def reset_and_seed_db():
    """
    Drop existing tables and completely reload with fresh data from seed_data.py.
    """
    conn = get_db()
    cursor = conn.cursor()
    tables = ["notifications", "timetable_classes", "audit_logs", "issues", "bookings", "resources", "users"]
    for t in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {t};")
    conn.commit()
    conn.close()
    init_db()


if __name__ == "__main__":
    reset_and_seed_db()
