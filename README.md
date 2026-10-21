# Smart Campus Operations and Facility Booking Platform

**KLE Society's P.C. Jabin Science College, Hubballi**  
*Department of Bachelor of Computer Applications (BCA)*  
*Autonomous College | Re-accredited by NAAC with 'A' Grade*

---

## Problem statement

Campus facilities and specialized computer laboratories in educational institutions are heavily contended resources: seminar halls are needed for guest lectures, computer labs host regular practicals and final-year capstone coding, and digital classrooms support interactive pedagogy. 

Most colleges handle this through **manual logbooks, verbal permissions, or unstructured messaging groups**. This leads to:
1. **Frequent Double-Bookings**: Two faculty members or student batches arriving at the same lab or seminar hall simultaneously.
2. **Zero Auditability**: No reliable record of who authorized a booking or why a room was occupied.
3. **Stale Availability Information**: Students and staff walking across campus to check if a lab is free.
4. **Untracked Maintenance**: Faulty Wi-Fi routers, broken HDMI cables, or display issues reported verbally and forgotten.

---

## Solution

A **deterministic, conflict-free facility booking and campus operations platform** that treats reservations as pure mathematical intervals and guarantees zero double-bookings:

```
ReservationDecision = f(Resource_ID, Booking_Date, Start_Time, End_Time,
                        Requester_Role, Existing_Active_Reservations)
```

Given a facility + date + time interval, the engine verifies availability, enforces campus operational hours (**9:00 AM – 5:00 PM**), routes requests to the administrator control center for confirmation, notifies users through in-app alerts, and writes every action to an **append-only security audit log**.

---

## Core innovation

1. **Mathematical Interval Intersection**: Conflicting bookings are prevented using strict interval overlap logic:
   ```sql
   (start_time < new_end) AND (end_time > new_start)
   ```
   No room, hall, or laboratory can ever have concurrent pending or approved reservations.
2. **Immutable Audit Trail**: All authentication events, reservation submissions, approvals, rejections, and cancellations are written to an append-only ledger (`audit_logs`) with user email, timestamp, and action code.
3. **Zero External Dependencies / Completely Offline**: Runs without external accounts, cloud subscriptions, or paid API keys. Everything runs locally with Python Flask, SQLite, and Tailwind CSS.

---

## Status

- **P0 Foundations**: Relational SQLite schema, foreign keys, deterministic seed data, password hashing.
- **P1 Authentication & Dynamic Roles**: Custom username/email authentication for Students and Faculty, header identity sync, 1-click demo accounts.
- **P2 Booking & Conflict Engine**: Operating hours check (9 AM - 5 PM), past-date prevention, mathematical double-booking blockage, reservation cancellations.
- **P3 Admin Review & Ledger**: Pending approval queue with 1-click `Approve` and `Reject` decision buttons, whole-campus reservations ledger.
- **P4 Facility Search & Availability**: Keyword search and live time-slot availability check.
- **Automated Verification**: 7/7 unit tests passing with zero failures.

---

## Architecture

```
Jinja2 Templates + Tailwind CSS (Browser / Mobile Responsive)
                    │  HTML Form Actions & GET Requests
                    ▼
Flask Application Controller (app.py)
   ├── Session Management (werkzeug.security password hashes)
   ├── Validation Guard (Operating hours, No past dates, End > Start)
   ├── Conflict Engine (Interval overlap check on bookings table)
   └── Role Dispatcher (Student / Faculty / Administrator)
                    │
                    ▼
SQLite Single-File Database (campus.db)
   ├── users (students, faculty, administrators)
   ├── resources (rooms, digital classrooms, specialized labs)
   ├── bookings (pending, approved, rejected, cancelled)
   ├── issues (maintenance tickets)
   ├── audit_logs (append-only ledger)
   └── notifications (in-app alerts)
```

---

## Tech stack

- **Backend:** Python 3.13 · Flask 3.1 · Werkzeug (secure password hashing)
- **Database:** SQLite3 (single file `campus.db`, row-factory dictionary mapping, foreign key enforcement via `PRAGMA foreign_keys = ON`)
- **Frontend:** HTML5 · Jinja2 Templates · Tailwind CSS (CDN loaded, zero npm/node_modules build steps)
- **Testing:** Python `unittest` (`tests/test_campus.py`, automated suite)
- **Ops:** Dockerfile + `docker-compose.yml` for 1-command containerized demo.

---

## Repository layout

```
smart-campus-jabin/
├── Dockerfile                   # Docker container specification
├── docker-compose.yml           # 1-command Docker Compose stack
├── .dockerignore                # Excludes virtual environments and databases from image
├── .gitignore                   # Excludes .venv and runtime SQLite files
├── .gitattributes               # Line-ending normalizations
├── .env.example                 # Example environment variables
├── README.md                    # Master competition/project documentation
├── DEMO.md                      # 3-5 minute Evaluator / Viva walkthrough script
├── app.py                       # Main Flask web application & route handlers
├── database.py                  # SQLite schema manager & auto-seeder
├── seed_data.py                 # Single configuration file for demo facilities & accounts
├── requirements.txt             # Python dependencies (Flask & Werkzeug)
├── tests/
│   ├── __init__.py
│   └── test_campus.py           # Automated test suite (7 tests)
└── templates/                   # Mobile-responsive Tailwind UI templates
    ├── base.html                # Navigation bar with user badge & flash messages
    ├── login.html               # Sign-in page with demo autofill buttons
    ├── dashboard_student.html   # Student portal & booking status
    ├── dashboard_staff.html     # Faculty portal & lecture reservations
    ├── dashboard_admin.html     # Admin control center (Approve/Reject + Ledger)
    ├── book.html                # Facility reservation form with validations
    └── resources.html           # Campus facility catalog & availability checker
```

---

## Running locally

### Prerequisites
- Python 3.10+ installed on your system.

### Option 1: Native Windows (PowerShell)

```powershell
# 1. Clone repository
git clone https://github.com/omkarshirol4-cloud/smart-campus-jabin.git
cd smart-campus-jabin

# 2. Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Start application
python app.py
```
Open **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser.

---

### Option 2: Docker Compose (1-Command Startup)

```powershell
docker compose up --build
```
Access the application at **[http://localhost:5000](http://localhost:5000)**.

---

## Running Automated Tests

```powershell
# Run the test suite:
.\.venv\Scripts\python.exe -m unittest discover tests -v
```
*(All 7 tests pass with exit code 0)*.

---

## Evaluator Demo Flow

A complete 3–5 minute evaluation guide is documented in **[DEMO.md](DEMO.md)**:

1. **Custom Identity Login** — enter any custom name (e.g. `Omkar`), pick a role, and verify the header syncs the identity.
2. **Facility Exploration** — search across classrooms, seminar halls, and laboratories, and check real-time availability.
3. **Booking Request** — reserve Classroom 1 or Computer Lab 1 with a session purpose.
4. **Collision Block Test** — submit an overlapping request for the same room; witness the immediate mathematical blockage.
5. **Admin Decision Hub** — log in as administrator, review the pending queue, approve or reject with 1 click, and inspect the security audit trail.

---

## Campus Facility Inventory (`seed_data.py`)

All facilities are configured in one central file: [seed_data.py](seed_data.py), extracted directly from the official college timetables:

| Facility / Resource Name | Type | Capacity | Location | Highlights |
| :--- | :--- | :--- | :--- | :--- |
| **Ubuntu Hall** | Room | 75 | BCA Block, Ground Floor | BCA III Sem (A1 Division) smart board & dual audio |
| **Windows Hall** | Room | 75 | BCA Block, Ground Floor | BCA III Sem (A2 Division) interactive digital board |
| **iOS Hall** | Room | 75 | BCA Block, 1st Floor | BCA III (A3) & BCA V (A5) Apple AirPlay smart display |
| **Fedora Hall** | Room | 75 | BCA Block, 1st Floor | BCA III Sem (A4 Division) Linux presentation environment |
| **Android Hall** | Room | 70 | BCA Block, 2nd Floor | BCA III Sem (A5 Division) mobile computing & emulators |
| **AVG Hall** | Room | 70 | BCA Block, 2nd Floor | BCA III & V Semester digital classroom setup |
| **Mcafee Hall** | Room | 70 | BCA Block, 2nd Floor | BCA I (A3) & BCA III (A5) security lecture hall |
| **Avira Hall** | Room | 70 | BCA Block, 3rd Floor | BCA I Sem (A1 Division) interactive smart board |
| **ESET Hall** | Room | 70 | BCA Block, 3rd Floor | BCA I Sem (A2 Division) digital podium & projector |
| **Panda Hall** | Room | 70 | BCA Senior Wing, 1st Floor | BCA V Sem (A1 Division) machine learning theory room |
| **Viper Hall** | Room | 70 | BCA Senior Wing, 1st Floor | BCA V Sem (A3 Division) full stack lecture room |
| **MAC Hall** | Room | 70 | BCA Senior Wing, 2nd Floor | BCA V Sem (A4 Division) systems architecture hall |
| **Norton Hall** | Room | 70 | BCA Senior Wing, 2nd Floor | BCA III Sem (A6 Division) cyber law & security hall |
| **PG Hall No. 1** | Room | 85 | PG Wing, 2nd Floor | Joint lecture hall for postgraduate seminars & workshops |
| **Twister Hall** | Room | 50 | BCA Wing, 3rd Floor | Discussion, debate, and project review screening hall |
| **Samza AIML Lab** | Room | 60 | Advanced Tech Wing, GF | 60 GPU workstations for AI/ML, TensorFlow & PyTorch |
| **Hadoop Big Data Lab** | Room | 60 | Advanced Tech Wing, GF | 60 systems with Android Studio & Big Data tools |
| **Flink Lab** | Room | 60 | BCA Lab Complex, 1st Floor | 60 systems with Advance Java, Spring Boot & Hibernate |
| **Spark Lab** | Room | 60 | BCA Lab Complex, 1st Floor | 60 systems for Advance MERN Stack & Cloud Computing |
| **Cloudera 1 Lab (DS Lab)**| Room | 60 | BCA Lab Complex, 2nd Floor | 60 Linux workstations for Data Structures using C |
| **Cloudera 2 Lab (DBMS Lab)**| Room | 60 | BCA Lab Complex, 2nd Floor | 60 workstations with MySQL, Oracle 19c & PostgreSQL |
| **Cloudera 3 Lab (AI & Security)**| Room | 60 | BCA Lab Complex, 2nd Floor | Kali Linux, Wireshark, Metasploit & Python AI packages |
| **FSD Lab (Full Stack)** | Room | 60 | BCA Lab Complex, 3rd Floor | Full stack development & capstone project workstations |
| **Language Laboratory** | Room | 40 | Central Library Annex, 1F | Speech enhancement workstations and noise-canceling headsets |
| **College Seminar Hall** | Room | 150 | Main Block, 2nd Floor | Central auditorium with Ahuja PA sound system & stage lights |
| **Library Discussion Area**| Room | 30 | Central Library, 1st Floor | Round tables & magnetic whiteboards for group study |
| **Indoor Games Room** | Room | 40 | Gymkhana Complex | Table tennis, carrom boards & chess stations |

---

## API & Route Reference

| Method | Path | Access | Purpose |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | Public | Root redirect to dashboard if logged in, else login |
| `GET` | `/login` | Public | Renders sign-in page with role selector & demo buttons |
| `POST` | `/login` | Public | Authenticates credentials or auto-registers custom user |
| `GET` | `/dashboard` | Authenticated | Role-based dashboard (Student, Faculty, or Admin) |
| `GET` | `/book` | Authenticated | Renders facility reservation form |
| `POST` | `/book` | Authenticated | Validates input, checks double-bookings, saves request |
| `POST` | `/bookings/<id>/cancel` | Owner / Admin | Cancels an active or pending reservation |
| `POST` | `/admin/bookings/<id>/approve` | Admin Only | Approves a pending booking, alerts user, logs audit |
| `POST` | `/admin/bookings/<id>/reject` | Admin Only | Declines a booking request with administrative remarks |
| `GET` | `/resources` | Authenticated | Catalogs facilities with search & availability checker |
| `GET` | `/logout` | Authenticated | Terminates user session and records audit event |

---

## Demo Accounts

All accounts share the default password: **`password123`** (with instant 1-click fill buttons on the sign-in card):
- **Student**: `student@demo.edu` (Rahul Patil, BCA 5th Sem)
- **Faculty Coordinator**: `staff@demo.edu` (Faculty Coordinator, BCA Faculty)
- **Faculty Lab In-Charge**: `faculty.labs@jabin.edu` (Faculty Lab In-Charge, BCA Laboratories)
- **Campus Administrator**: `admin@demo.edu` (Campus Administration)
