# Evaluator Demo Script — Smart Campus Operations & Facility Booking Platform

**KLE Society's P.C. Jabin Science College, Hubballi**  
*Department of Bachelor of Computer Applications (BCA)*  
**Duration: 3–5 minutes.** One browser window, one continuous story.

---

## 🛠️ Setup (Before the Evaluators / Judges Arrive)

1. Open PowerShell and start the local server:
   ```powershell
   cd C:\Users\omkar\.gemini\antigravity\scratch\smart_campus_jabin
   .\.venv\Scripts\python.exe app.py
   ```
   *(Or with Docker: `docker compose up -d`)*

2. Open browser to **`http://127.0.0.1:5000`**.
3. Verify that the login page loads cleanly with the college header and 1-click demo buttons.

---

## 🎬 The Walkthrough Script (Step by Step)

### Step 1: The Core Problem & College Context (30 seconds)
> *"Welcome! In our college, BCA students and faculty frequently need Seminar Halls, Computer Labs, and Smart Digital Classrooms. Traditionally, scheduling happened via manual sign-up sheets or verbal requests, which led to double bookings, clashes, and zero accountability.*  
> *We built this Smart Campus Platform with zero external frameworks or APIs: pure Python Flask, SQLite, and Tailwind CSS."*

---

### Step 2: Dynamic Role-Based Login & Custom Identity (45 seconds)
1. On the login screen (`http://127.0.0.1:5000/login`):
   - Type your own name into **Your Name or Email** (e.g., `Omkar`).
   - Type any password.
   - Select **🎓 Student** and click **Sign In**.
2. **Show the Evaluator:**
   - Notice the top navigation bar immediately updates to display `Omkar` as the logged-in student.
   - Point out the **Student Portal** badge and student metric cards.
   - Mention that demo 1-click accounts (`student@demo.edu`, `staff@demo.edu`, `admin@demo.edu`) are also available.

---

### Step 3: Facility Inventory & Live Availability Check (45 seconds)
1. Click **Facilities & Rooms** in the top navigation bar (`/resources`).
2. Show the real college facility catalog:
   - College Seminar Hall (150 capacity, sound system, stage lighting)
   - Specialized Laboratories (Samza AIML Lab, Hadoop Big Data Lab, Flink Lab, Cloudera Labs)
   - Language Laboratory & Library Discussion Area
   - Smart Digital Classrooms (Ubuntu Hall, Windows Hall, iOS Hall, Fedora Hall)
3. Type `"Lab"` into the Search box and hit Filter — watch the list filter down instantly.
4. Show the **Check Date Availability** filter: pick today's date and a time slot to see instant live `Available` vs `Booked for Slot` status indicators.

---

### Step 4: Facility Reservation Request (45 seconds)
1. Click **+ Book Facility** (`/book`).
2. Select **`Classroom (digital) 1`**.
3. Pick a future date (e.g. tomorrow) with slot **10:00 to 12:00**.
4. Enter purpose: `"Final Year BCA Capstone Project Presentation"`.
5. Click **Confirm & Reserve Facility**.
6. **Show the Evaluator:**
   - The booking is instantly recorded in SQLite and appears under **My Facility Bookings** with status **Pending**.
   - An in-app alert notification is generated.

---

### Step 5: The Double-Booking Prevention Engine (30 seconds)
1. Immediately click **+ Book Facility** again.
2. Select the **same facility** (`Classroom (digital) 1`) on the **same date**.
3. Choose an **overlapping time slot** (e.g. **11:00 to 13:00**).
4. Click **Confirm & Reserve Facility**.
5. **Show the Evaluator:**
   - The system mathematically blocks the submission:
     > *"Double Booking Blocked! 'Classroom (digital) 1' is already booked on [Date] between 10:00 and 12:00 (Reserved by: Omkar, Status: Pending)."*
   - Explain the interval intersection logic: `start_time < new_end AND end_time > new_start`.

---

### Step 6: Admin Approval Workflow & Campus Ledger (45 seconds)
1. Click **Logout** and sign in as **Admin** (click the **Admin Account** demo button or enter `admin@demo.edu`).
2. Look at the **Admin Control Center**:
   - The top table **⚡ Pending Booking Requests** prominently features Omkar's request for Classroom 1.
   - Point out the requester's name, role badge (`Student`), facility, date, and purpose.
3. Click the green **`[✓ Approve]`** button:
   - Status updates instantly to **Approved**.
   - The student receives an approval notification.
   - The reservation transitions into the **All Campus Bookings & Reservations** ledger below.
4. Point out the **Security & System Audit Log** at the bottom:
   - Shows the exact audit record: `APPROVE_BOOKING` with admin email and timestamp.

---

### Step 7: Conclusion & Code Architecture (30 seconds)
> *"Every transaction is backed by SQLite transactions and audited in real time. The codebase is clean, modular, and easy for any BCA student to inspect and extend."*
