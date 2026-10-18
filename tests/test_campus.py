# tests/test_campus.py
# Verification tests for database, dynamic custom logins, booking, double-booking prevention, admin approvals, and cancellations.

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
        # Clean up any leftover test bookings from previous runs
        conn = database.get_db()
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
        self.assertIn(b"Student Portal", response.data)

    def test_04_faculty_custom_login(self):
        response = self.client.post("/login", data={
            "email": "Prof. Anand",
            "password": "anandpassword",
            "role": "staff"
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Prof. Anand", response.data)
        self.assertIn(b"Faculty & Staff Portal", response.data)

    def test_05_student_and_faculty_requests_show_in_admin_dashboard(self):
        # 1. Student requests Classroom 1
        self.client.get("/logout")
        self.client.post("/login", data={
            "email": "test_student_user",
            "password": "password123",
            "role": "student"
        }, follow_redirects=True)

        target_date = (date.today() + timedelta(days=20)).isoformat()
        student_req = self.client.post("/book", data={
            "resource_id": "6",
            "booking_date": target_date,
            "start_time": "09:00",
            "end_time": "11:00",
            "purpose": "BCA Student Seminar on Cloud Computing"
        }, follow_redirects=True)
        self.assertEqual(student_req.status_code, 200)
        self.assertIn(b"BCA Student Seminar on Cloud Computing", student_req.data)

        # 2. Faculty requests Classroom 2
        self.client.get("/logout")
        self.client.post("/login", data={
            "email": "test_faculty_user",
            "password": "password123",
            "role": "staff"
        }, follow_redirects=True)

        faculty_req = self.client.post("/book", data={
            "resource_id": "7",
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
        # 1. Create student & faculty test bookings
        self.client.get("/logout")
        self.client.post("/login", data={"email": "test_student_user", "password": "password123", "role": "student"})
        target_date = (date.today() + timedelta(days=22)).isoformat()
        self.client.post("/book", data={
            "resource_id": "6", "booking_date": target_date, "start_time": "09:00", "end_time": "11:00",
            "purpose": "BCA Student Seminar on Cloud Computing"
        })

        self.client.get("/logout")
        self.client.post("/login", data={"email": "test_faculty_user", "password": "password123", "role": "staff"})
        self.client.post("/book", data={
            "resource_id": "7", "booking_date": target_date, "start_time": "11:00", "end_time": "13:00",
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

        conflict_date = (date.today() + timedelta(days=25)).isoformat()
        self.client.post("/book", data={
            "resource_id": "8",
            "booking_date": conflict_date,
            "start_time": "10:00",
            "end_time": "12:00",
            "purpose": "College Table Tennis Tournament"
        })

        res_overlap = self.client.post("/book", data={
            "resource_id": "8",
            "booking_date": conflict_date,
            "start_time": "11:00",
            "end_time": "13:00",
            "purpose": "Chess Championship"
        }, follow_redirects=True)

        self.assertIn(b"Double Booking Blocked!", res_overlap.data)

if __name__ == "__main__":
    unittest.main()
