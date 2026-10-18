# Smart Campus Operations and Facility Booking Platform

**KLE Society's P.C. Jabin Science College, Hubballi**  
*Department of Bachelor of Computer Applications (BCA)*  
*Autonomous College | Re-accredited by NAAC with 'A' Grade*

---

## Problem statement

Campus facilities and specialized computer laboratories in educational institutions are heavily contended resources: seminar halls are needed for guest lectures, computer labs host regular practicals and final-year capstone coding, digital classrooms support interactive pedagogy, and portable AV equipment (projectors and PA sound systems) moves between wings. 

Most colleges handle this through **manual logbooks, verbal permissions, or unstructured messaging groups**. This leads to:
1. **Frequent Double-Bookings**: Two faculty members or student batches arriving at the same lab or seminar hall simultaneously.
2. **Zero Auditability**: No reliable record of who authorized a booking, when equipment was taken, or why a room was occupied.
3. **Stale Availability Information**: Students and staff walking across campus to check if a lab is free.
4. **Untracked Maintenance**: Faulty Wi-Fi routers, broken HDMI cables, or crackling PA systems reported verbally and forgotten.

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
   No room or portable equipment can ever have concurrent pending or approved reservations.
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
   ├── resources (rooms, specialized labs, AV equipment)
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
2. **Facility Exploration** — filter by `Room` or `Equipment` and check real-time availability.
3. **Booking Request** — reserve Classroom 1 or Computer Lab 1 with a session purpose.
4. **Collision Block Test** — submit an overlapping request for the same room; witness the immediate mathematical blockage.
5. **Admin Decision Hub** — log in as administrator, review the pending queue, approve or reject with 1 click, and inspect the security audit trail.

---

## Campus Facility Inventory (`seed_data.py`)

All facilities are configured in one central file: [seed_data.py](seed_data.py):

| Facility / Resource Name | Type | Capacity | Location | Highlights |
| :--- | :--- | :--- | :--- | :--- |
| **Seminar Hall** | Room | 120 | Main Block, 2nd Floor | Overhead ceiling projector, sound amplifiers, podium mic |
| **Computer Lab 1** | Room | 60 | BCA Wing, Ground Floor | 60 high-performance desktops, Gigabit LAN, Python/Java/MySQL |
| **Computer Lab 2** | Room | 60 | BCA Wing, 1st Floor | Dedicated systems for Web Tech, Cloud & Data Science |
| **Language Laboratory** | Room | 40 | BCA Wing, 1st Floor | Workstations equipped with high-clarity speech headsets |
| **Library Discussion Area** | Room | 25 | Central Library, 1st Floor | Round tables, whiteboard for collaborative capstone study |
| **Classroom (digital) 1** | Room | 70 | BCA Wing, 2nd Floor | Interactive digital smart board, motorized screen, wall speakers |
| **Classroom (digital) 2** | Room | 70 | BCA Wing, 2nd Floor | Interactive digital smart board, motorized screen, wall speakers |
| **Indoor Games Room** | Room | 30 | Gymkhana Complex | Table tennis, carrom boards, chess tables |
| **Portable Projector** | Equipment | 1 | BCA Dept Office | Epson Full HD portable projector with HDMI & tripod |
| **Amplifier / Sound System** | Equipment | 1 | BCA Dept Office | Ahuja portable PA sound system with dual wireless mics |
| **Laptop Cart** | Equipment | 20 | BCA Dept Office | Mobile lockable charging trolley with 20 student laptops |

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

## Demo Logins

All demo accounts share the password: **`password123`** (or click the quick buttons on the login card):
- **Student**: `student@demo.edu`
- **Faculty / Staff**: `staff@demo.edu`
- **Administrator**: `admin@demo.edu`
