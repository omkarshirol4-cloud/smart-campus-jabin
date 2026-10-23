# tests/test_campus.py
# Verification tests for database, dynamic custom logins, booking, timetable conflict prevention,
# double-booking prevention, admin approvals, and cancellations.

import unittest
from datetime import date, timedelta
import sys
import os

# Ensure parent directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app
import database

class CampusTestSuite(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["WTF_CSRF_ENABLED"] = False
        self.client = app.test_client()
        database.init_db()
        self.client.get("/logout")

        conn = database.get_db()
        # Clean up any leftover test bookings from previous runs
        conn.execute("""
            DELETE FROM bookings 
            WHERE purpose LIKE 'Test%' 
               OR purpose LIKE 'BCA Student Seminar%' 
               OR purpose LIKE 'Faculty Guest Lecture%' 
               OR purpose LIKE 'College Table Tennis%'
               OR purpose LIKE 'Chess Championship%'
               OR purpose LIKE 'Final Year BCA Capstone%'
               OR purpose LIKE 'Another overlapping%'
               OR purpose LIKE 'Session to be cancelled%'
        """)
        conn.commit()

        # Cache IDs of open facilities (no timetable recurring lectures)
        self.seminar_id = str(conn.execute("SELECT id FROM resources WHERE name = 'College Seminar Hall'").fetchone()["id"])
        self.games_id = str(conn.execute("SELECT id FROM resources WHERE name = 'Indoor Games Room'").fetchone()["id"])
        self.ubuntu_id = str(conn.execute("SELECT id FROM resources WHERE name = 'Ubuntu Hall'").fetchone()["id"])
        conn.close()

    def test_01_index_redirects_to_login(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", response.headers["Location"])

    def test_02_login_page_renders_with_custom_inputs(self):
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Your Name or Email", response.data)
        self.assertIn(b"Select Your Role", response.data)

    def test_03_custom_username_login_and_header_display(self):
        response = self.client.post("/login", data={
            "email": "Omkar",
            "password": "myrandompassword99",
            "role": "student"
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Omkar", response.data)
        self.assertIn(b"Student", response.data)

    def test_04_faculty_custom_login(self):
        response = self.client.post("/login", data={
            "email": "Prof. Anand",
            "password": "anandpassword",
            "role": "staff"
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Prof. Anand", response.data)
        self.assertIn(b"Faculty", response.data)

    def test_05_student_and_faculty_requests_show_in_admin_dashboard(self):
        # Pick a future weekday (Mon-Sat)
        target_dt = date.today() + timedelta(days=20)
        if target_dt.weekday() == 6:  # Sunday
            target_dt += timedelta(days=1)
        target_date = target_dt.isoformat()

        # 1. Student requests College Seminar Hall
        self.client.get("/logout")
        self.client.post("/login", data={
            "email": "test_student_user",
            "password": "password123",
            "role": "student"
        }, follow_redirects=True)

        student_req = self.client.post("/book", data={
            "resource_id": self.seminar_id,
            "booking_date": target_date,
            "start_time": "09:00",
            "end_time": "11:00",
            "purpose": "BCA Student Seminar on Cloud Computing"
        }, follow_redirects=True)
        self.assertEqual(student_req.status_code, 200)
        self.assertIn(b"BCA Student Seminar on Cloud Computing", student_req.data)

        # 2. Faculty requests Indoor Games Room
        self.client.get("/logout")
        self.client.post("/login", data={
            "email": "test_faculty_user",
            "password": "password123",
            "role": "staff"
        }, follow_redirects=True)

        faculty_req = self.client.post("/book", data={
            "resource_id": self.games_id,
            "booking_date": target_date,
            "start_time": "11:00",
            "end_time": "13:00",
            "purpose": "Faculty Guest Lecture on Cyber Security"
        }, follow_redirects=True)
        self.assertEqual(faculty_req.status_code, 200)
        self.assertIn(b"Faculty Guest Lecture on Cyber Security", faculty_req.data)

        # 3. Admin checks dashboard
        self.client.get("/logout")
        self.client.post("/login", data={
            "email": "admin@demo.edu",
            "password": "password123",
            "role": "admin"
        }, follow_redirects=True)

        admin_dash = self.client.get("/dashboard")
        self.assertEqual(admin_dash.status_code, 200)
        self.assertIn(b"BCA Student Seminar on Cloud Computing", admin_dash.data)
        self.assertIn(b"Faculty Guest Lecture on Cyber Security", admin_dash.data)
        self.assertIn(b"Approve", admin_dash.data)
        self.assertIn(b"Reject", admin_dash.data)

    def test_06_admin_approve_and_reject_actions(self):
        target_dt = date.today() + timedelta(days=22)
        if target_dt.weekday() == 6:
            target_dt += timedelta(days=1)
        target_date = target_dt.isoformat()

        # 1. Create student & faculty test bookings on open facilities
        self.client.get("/logout")
        self.client.post("/login", data={"email": "test_student_user", "password": "password123", "role": "student"})
        self.client.post("/book", data={
            "resource_id": self.seminar_id, "booking_date": target_date, "start_time": "09:00", "end_time": "11:00",
            "purpose": "BCA Student Seminar on Cloud Computing"
        })

        self.client.get("/logout")
        self.client.post("/login", data={"email": "test_faculty_user", "password": "password123", "role": "staff"})
        self.client.post("/book", data={
            "resource_id": self.games_id, "booking_date": target_date, "start_time": "11:00", "end_time": "13:00",
            "purpose": "Faculty Guest Lecture on Cyber Security"
        })

        conn = database.get_db()
        b_student = conn.execute("SELECT id FROM bookings WHERE purpose = 'BCA Student Seminar on Cloud Computing'").fetchone()
        b_faculty = conn.execute("SELECT id FROM bookings WHERE purpose = 'Faculty Guest Lecture on Cyber Security'").fetchone()
        conn.close()

        self.client.get("/logout")
        self.client.post("/login", data={
            "email": "admin@demo.edu",
            "password": "password123",
            "role": "admin"
        }, follow_redirects=True)

        app_res = self.client.post(f"/admin/bookings/{b_student['id']}/approve", follow_redirects=True)
        self.assertEqual(app_res.status_code, 200)
        self.assertIn(b"has been approved", app_res.data)

        rej_res = self.client.post(f"/admin/bookings/{b_faculty['id']}/reject", follow_redirects=True)
        self.assertEqual(rej_res.status_code, 200)
        self.assertIn(b"was declined", rej_res.data)

        conn = database.get_db()
        s_status = conn.execute("SELECT status FROM bookings WHERE id = ?", (b_student["id"],)).fetchone()["status"]
        f_status = conn.execute("SELECT status FROM bookings WHERE id = ?", (b_faculty["id"],)).fetchone()["status"]
        conn.close()
        self.assertEqual(s_status, "approved")
        self.assertEqual(f_status, "rejected")

    def test_07_double_booking_prevention(self):
        self.client.get("/logout")
        self.client.post("/login", data={
            "email": "student@demo.edu",
            "password": "password123",
            "role": "student"
        }, follow_redirects=True)

        target_dt = date.today() + timedelta(days=25)
        if target_dt.weekday() == 6:
            target_dt += timedelta(days=1)
        conflict_date = target_dt.isoformat()

        # First booking in Seminar Hall
        self.client.post("/book", data={
            "resource_id": self.seminar_id,
            "booking_date": conflict_date,
            "start_time": "10:00",
            "end_time": "12:00",
            "purpose": "College Table Tennis Tournament"
        })

        # Overlapping booking in the same room on the same date
        res_overlap = self.client.post("/book", data={
            "resource_id": self.seminar_id,
            "booking_date": conflict_date,
            "start_time": "11:00",
            "end_time": "13:00",
            "purpose": "Chess Championship"
        }, follow_redirects=True)

        self.assertIn(b"Double Booking Blocked!", res_overlap.data)

    def test_08_timetable_class_conflict_blocking(self):
        # Pick next Monday
        today = date.today()
        days_ahead = (7 - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        next_monday = (today + timedelta(days=days_ahead)).isoformat()

        self.client.get("/logout")
        self.client.post("/login", data={
            "email": "student@demo.edu",
            "password": "password123",
            "role": "student"
        }, follow_redirects=True)

        # Attempt to book Ubuntu Hall during Monday 10:00 - 11:00 (Intro to AI class scheduled)
        res = self.client.post("/book", data={
            "resource_id": self.ubuntu_id,
            "booking_date": next_monday,
            "start_time": "10:00",
            "end_time": "11:00",
            "purpose": "Test Peer Study Group"
        }, follow_redirects=True)

        self.assertIn(b"Timetable Conflict Blocked!", res.data)
        self.assertIn(b"Introduction to Artificial Intelligence", res.data)
        self.assertIn(b"BCA III (A1)", res.data)

    def test_09_sunday_booking_blocked(self):
        # Pick next Sunday
        today = date.today()
        days_ahead = (6 - today.weekday()) % 7
        if days_ahead == 0:
            days_ahead = 7
        next_sunday = (today + timedelta(days=days_ahead)).isoformat()

        self.client.get("/logout")
        self.client.post("/login", data={
            "email": "staff@demo.edu",
            "password": "password123",
            "role": "staff"
        }, follow_redirects=True)

        res = self.client.post("/book", data={
            "resource_id": self.seminar_id,
            "booking_date": next_sunday,
            "start_time": "10:00",
            "end_time": "12:00",
            "purpose": "Sunday Guest Workshop"
        }, follow_redirects=True)

        self.assertIn(b"closed on Sundays", res.data)

    def test_10_timetable_page_renders_classes(self):
        self.client.get("/logout")
        self.client.post("/login", data={
            "email": "student@demo.edu",
            "password": "password123",
            "role": "student"
        }, follow_redirects=True)

        res = self.client.get("/timetable")
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Academic Class Timetables", res.data)
        self.assertIn(b"Ubuntu Hall", res.data)
        self.assertIn(b"Linear Algebra", res.data)

if __name__ == "__main__":
    unittest.main()
