# Smart Campus Operations and Facility Booking Platform

**KLE Society's P.C. Jabin Science College, Hubballi**  
*Department of Bachelor of Computer Applications (BCA)*  
*Autonomous College | Re-accredited by NAAC with 'A' Grade*

---

## 📌 Project Overview
A lightweight, modern web platform designed for the BCA Department at KLE P.C. Jabin Science College to manage campus facilities, reserve laboratories and seminar halls, track AV equipment, and prevent scheduling conflicts in real time.

---

## 🛠️ Technology Stack
- **Backend**: Python 3.13 + Flask
- **Database**: SQLite3 (single database file with relational foreign keys)
- **Frontend**: Jinja2 HTML5 Templates + Tailwind CSS (via CDN)
- **Authentication**: Secure password hashing (`werkzeug.security`) and session-based role management
- **Zero Heavy Dependencies**: No node_modules, no npm build steps, no external cloud dependencies.

---

## ✨ Features
1. **Role-Based Access Control**:
   - **Student Portal**: Book labs and rooms, track reservation status, view personalized in-app notifications.
   - **Faculty / Staff Portal**: Reserve seminar halls and smart classrooms for lectures, view departmental schedules.
   - **Admin Control Center**: Approve/reject pending requests with 1-click controls, view active maintenance tickets, monitor campus-wide reservations, and inspect security audit logs.
2. **Dynamic & Demo Login Support**:
   - Supports 1-click demo logins (`student@demo.edu`, `staff@demo.edu`, `admin@demo.edu`).
   - Allows students and faculty to enter their custom name/username and test reservations with their own profile.
3. **Double-Booking & Conflict Prevention**:
   - Mathematically enforces non-overlapping intervals (`start_time < new_end AND end_time > new_start`).
   - Blocks double-bookings with an informative conflict alert showing who reserved the slot.
4. **Facility & Equipment Directory**:
   - Search facilities by keyword (e.g. *Lab*, *Projector*, *Classroom*).
   - Filter by type (Room vs. Portable Equipment).
   - Live availability checker for any custom date and time slot.
5. **Operating Hours Enforcement**:
   - Reservations are permitted strictly within campus hours (9:00 AM – 5:00 PM).
   - Input validations ensure dates are not in the past and end times occur after start times.
6. **Security Audit Trail**:
   - Comprehensive automated log tracking logins, logouts, booking creations, cancellations, approvals, and rejections.

---

## 🏛️ Campus Facility Inventory (`seed_data.py`)
- **Seminar Hall** (Capacity: 120+, ceiling projector & PA sound amplifiers)
- **Computer Lab 1** (Capacity: 60 desktops, programming & LAN environment)
- **Computer Lab 2** (Capacity: 60 desktops, web technologies & cloud computing)
- **Language Laboratory** (Capacity: 40 workstations with audio headsets)
- **Library Discussion Area** (Capacity: 25, collaborative whiteboards)
- **Classroom (digital) 1 & 2** (Capacity: 70 each, interactive digital smart boards)
- **Indoor Games Room** (Capacity: 30, table tennis, carrom & chess)
- **Portable Projector** (Epson Full HD with HDMI & stand)
- **Amplifier / Sound System** (Ahuja portable PA system with wireless mics)
- **Laptop Cart** (Mobile charging trolley with 20 student laptops)

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/omkarshirol4-cloud/smart-campus-jabin.git
cd smart-campus-jabin
```

### 2. Set Up Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate on Windows:
.\.venv\Scripts\activate

# Activate on macOS / Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```
Open **http://127.0.0.1:5000** in your browser.

---

## 🧪 Running Automated Tests
```bash
python test_auth.py
```

---

## 👥 Demo Logins
All accounts use the password: **`password123`** (or click the quick autofill buttons on the login screen):
- **Student**: `student@demo.edu`
- **Staff / Faculty**: `staff@demo.edu`
- **Admin**: `admin@demo.edu`
