# seed_data.py
# Synthetic Data for KLE Society's P.C. Jabin Science College
# Bachelor of Computer Applications (BCA Department), Vidyanagar, Hubballi.
# Contains real campus rooms, labs, and halls (No portable equipment and no private faculty names).

from datetime import date, timedelta

# Default password for all demo accounts
DEFAULT_PASSWORD = "password123"

# -----------------------------------------------------------------------------
# 1. USER ACCOUNTS (Fictional / Role-Based Accounts)
# -----------------------------------------------------------------------------
USERS = [
    {
        "email": "student@demo.edu",
        "full_name": "Rahul Patil",
        "role": "student",
        "department": "BCA 5th Sem",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "staff@demo.edu",
        "full_name": "Faculty Coordinator",
        "role": "staff",
        "department": "BCA Faculty",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "faculty.labs@jabin.edu",
        "full_name": "Faculty Lab In-Charge",
        "role": "staff",
        "department": "BCA Laboratories",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "admin@demo.edu",
        "full_name": "Campus Administrator",
        "role": "admin",
        "department": "Campus Administration",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "student.rep@demo.edu",
        "full_name": "Kavya Kulkarni",
        "role": "student",
        "department": "BCA 3rd Sem",
        "password": DEFAULT_PASSWORD,
    },
]

# -----------------------------------------------------------------------------
# 2. CAMPUS FACILITIES (Rooms, Halls, and Specialized Laboratories ONLY)
# Note: All portable equipment has been removed as requested.
# -----------------------------------------------------------------------------
RESOURCES = [
    # Lecture & Smart Digital Classrooms named after OS & Platforms
    {
        "name": "Ubuntu Hall",
        "type": "Room",
        "capacity": 75,
        "location": "BCA Block, Ground Floor (Room 101)",
        "description": "BCA Lecture Classroom. Equipped with smart interactive board, motorized screen, and dual wall speakers.",
    },
    {
        "name": "Windows Hall",
        "type": "Room",
        "capacity": 75,
        "location": "BCA Block, Ground Floor (Room 102)",
        "description": "BCA Digital Classroom. Smart interactive board, podium mic, and LAN projection.",
    },
    {
        "name": "iOS Hall",
        "type": "Room",
        "capacity": 75,
        "location": "BCA Block, 1st Floor (Room 201)",
        "description": "BCA Lecture Hall. High-definition AV system and AirPlay enabled smart display.",
    },
    {
        "name": "Fedora Hall",
        "type": "Room",
        "capacity": 75,
        "location": "BCA Block, 1st Floor (Room 202)",
        "description": "BCA Linux Classroom. Open-source development environment, interactive smart screen, and surround audio.",
    },
    {
        "name": "Android Hall",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Block, 2nd Floor (Room 301)",
        "description": "Mobile computing lecture hall with Android emulator projection and digital podium.",
    },
    {
        "name": "AVG Hall",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Block, 2nd Floor (Room 302)",
        "description": "BCA Digital Classroom. Overhead projection, sound system, and motorized screen.",
    },
    {
        "name": "Mcafee Hall",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Block, 2nd Floor (Room 303)",
        "description": "Systems & security lecture hall with interactive smart board and dual microphones.",
    },
    {
        "name": "Avira Hall",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Block, 3rd Floor (Room 401)",
        "description": "Foundation lecture classroom. Interactive smart board and high-clarity sound system.",
    },
    {
        "name": "ESET Hall",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Block, 3rd Floor (Room 402)",
        "description": "Programming lecture classroom. Digital podium, overhead ceiling projector, and dual speakers.",
    },
    {
        "name": "Panda Hall",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Senior Wing, 1st Floor (Room 205)",
        "description": "Machine learning & AI theory classroom with smart presentation setup.",
    },
    {
        "name": "Viper Hall",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Senior Wing, 1st Floor (Room 206)",
        "description": "Full stack development presentation classroom with interactive whiteboard.",
    },
    {
        "name": "MAC Hall",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Senior Wing, 2nd Floor (Room 305)",
        "description": "Cloud computing & enterprise architecture presentation hall.",
    },
    {
        "name": "Norton Hall",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Senior Wing, 2nd Floor (Room 306)",
        "description": "Cyber law, network security, and ethics classroom.",
    },
    {
        "name": "PG Hall No. 1",
        "type": "Room",
        "capacity": 85,
        "location": "PG & Research Wing, 2nd Floor",
        "description": "Joint lecture hall for seminars, faculty meetings, and guest presentations.",
    },
    {
        "name": "Twister Hall",
        "type": "Room",
        "capacity": 50,
        "location": "BCA Wing, 3rd Floor",
        "description": "Discussion, debate, and project review screening hall.",
    },

    # Specialized Computer Laboratories
    {
        "name": "Samza AIML Lab",
        "type": "Room",
        "capacity": 60,
        "location": "Advanced Tech Wing, Ground Floor",
        "description": "Artificial Intelligence & Machine Learning Lab. 60 GPU workstations, TensorFlow/PyTorch, JupyterHub environment.",
    },
    {
        "name": "Hadoop Big Data Lab",
        "type": "Room",
        "capacity": 60,
        "location": "Advanced Tech Wing, Ground Floor",
        "description": "Android Programming & Big Data Lab. 60 high-performance systems with Android Studio.",
    },
    {
        "name": "Flink Lab",
        "type": "Room",
        "capacity": 60,
        "location": "BCA Lab Complex, 1st Floor",
        "description": "Advance Java with Frameworks Lab. 60 desktops with Eclipse/IntelliJ, Spring Boot, Hibernate.",
    },
    {
        "name": "Spark Lab",
        "type": "Room",
        "capacity": 60,
        "location": "BCA Lab Complex, 1st Floor",
        "description": "Advance Web & MERN Stack Development Lab. 60 systems with Node.js, React, MongoDB, and Git.",
    },
    {
        "name": "Cloudera 1 Lab (DS Lab)",
        "type": "Room",
        "capacity": 60,
        "location": "BCA Lab Complex, 2nd Floor",
        "description": "Data Structures using C & Algorithms Laboratory. 60 Linux workstations, GCC toolchain, GDB debugger.",
    },
    {
        "name": "Cloudera 2 Lab (DBMS Lab)",
        "type": "Room",
        "capacity": 60,
        "location": "BCA Lab Complex, 2nd Floor",
        "description": "Database Management Systems Laboratory. 60 workstations with MySQL, Oracle 19c, PostgreSQL.",
    },
    {
        "name": "Cloudera 3 Lab (AI & Security)",
        "type": "Room",
        "capacity": 60,
        "location": "BCA Lab Complex, 2nd Floor",
        "description": "Cyber Security & Artificial Intelligence Lab. Kali Linux, Wireshark, Metasploit, Python AI packages.",
    },
    {
        "name": "FSD Lab (Full Stack)",
        "type": "Room",
        "capacity": 60,
        "location": "BCA Lab Complex, 3rd Floor",
        "description": "Full Stack Web Development & Capstone Project Lab. Cloud-connected development workstations.",
    },
    {
        "name": "Language Laboratory",
        "type": "Room",
        "capacity": 40,
        "location": "Central Library Annex, 1st Floor",
        "description": "Audio-visual speech enhancement workstations and noise-canceling headsets for professional communication.",
    },

    # Campus Central Facilities & Recreation
    {
        "name": "College Seminar Hall",
        "type": "Room",
        "capacity": 150,
        "location": "Main Administrative Block, 2nd Floor",
        "description": "Central auditorium equipped with motorized projector screen, stage lights, podium mic, and sound system.",
    },
    {
        "name": "Library Discussion Area",
        "type": "Room",
        "capacity": 30,
        "location": "Central Library, 1st Floor",
        "description": "Round tables, magnetic whiteboards, and quiet zone for collaborative academic discussions.",
    },
    {
        "name": "Indoor Games Room",
        "type": "Room",
        "capacity": 40,
        "location": "Gymkhana Sports Complex",
        "description": "Table tennis tables, chess stations, and carrom recreation area.",
    },
]

# -----------------------------------------------------------------------------
# 3. STANDARD ISSUE CATEGORIES
# -----------------------------------------------------------------------------
ISSUE_CATEGORIES = [
    "Electrical",
    "Internet/Wi-Fi",
    "Computer/Hardware",
    "Furniture",
    "Cleanliness",
    "Projector/AV",
    "Other",
]

# -----------------------------------------------------------------------------
# 4. OPERATING HOURS (9:00 AM to 5:00 PM)
# -----------------------------------------------------------------------------
OPERATING_HOURS = {
    "start": "09:00",
    "end": "17:00",
}

# -----------------------------------------------------------------------------
# 5. SAMPLE BOOKINGS (Rooms & Laboratories Only)
# -----------------------------------------------------------------------------
today = date.today()
tomorrow = today + timedelta(days=1)
day_after = today + timedelta(days=2)
yesterday = today - timedelta(days=1)

SAMPLE_BOOKINGS = [
    # 1. Approved Timetable Sessions
    {
        "user_email": "staff@demo.edu",
        "resource_name": "Hadoop Big Data Lab",
        "booking_date": today.isoformat(),
        "start_time": "11:00",
        "end_time": "13:00",
        "purpose": "BCA V Sem Android Application Programming Lab Practical",
        "status": "approved",
        "admin_notes": "Scheduled timetable lab. Android Studio verified.",
    },
    {
        "user_email": "faculty.labs@jabin.edu",
        "resource_name": "Samza AIML Lab",
        "booking_date": today.isoformat(),
        "start_time": "11:00",
        "end_time": "13:00",
        "purpose": "Machine Learning Model Training & Neural Network Hands-on",
        "status": "approved",
        "admin_notes": "GPU workstation nodes allocated.",
    },
    {
        "user_email": "staff@demo.edu",
        "resource_name": "Flink Lab",
        "booking_date": tomorrow.isoformat(),
        "start_time": "14:00",
        "end_time": "16:00",
        "purpose": "Advance Java with Frameworks Lab Practical Session",
        "status": "approved",
        "admin_notes": "Spring Boot & Hibernate environment active.",
    },
    {
        "user_email": "faculty.labs@jabin.edu",
        "resource_name": "Cloudera 3 Lab (AI & Security)",
        "booking_date": tomorrow.isoformat(),
        "start_time": "10:00",
        "end_time": "12:00",
        "purpose": "Network Security & Penetration Testing Hands-on Lab",
        "status": "approved",
        "admin_notes": "Wireshark & Packet Analyzer verified.",
    },
    {
        "user_email": "staff@demo.edu",
        "resource_name": "College Seminar Hall",
        "booking_date": day_after.isoformat(),
        "start_time": "10:00",
        "end_time": "13:00",
        "purpose": "BCA Technical Symposium & Project Exhibition",
        "status": "approved",
        "admin_notes": "Approved by HOD. AV and stage arrangement confirmed.",
    },

    # 2. Pending Requests Awaiting Administrator Review
    {
        "user_email": "student@demo.edu",
        "resource_name": "Ubuntu Hall",
        "booking_date": tomorrow.isoformat(),
        "start_time": "15:00",
        "end_time": "17:00",
        "purpose": "BCA Student Tech Quiz Preparation & Peer Coding",
        "status": "pending",
        "admin_notes": "",
    },
    {
        "user_email": "student.rep@demo.edu",
        "resource_name": "Windows Hall",
        "booking_date": day_after.isoformat(),
        "start_time": "14:00",
        "end_time": "16:00",
        "purpose": "Algorithm Study Circle & Problem Solving Session",
        "status": "pending",
        "admin_notes": "",
    },
    {
        "user_email": "faculty.labs@jabin.edu",
        "resource_name": "Cloudera 3 Lab (AI & Security)",
        "booking_date": day_after.isoformat(),
        "start_time": "14:00",
        "end_time": "16:00",
        "purpose": "Cyber Security Certification Practical Exam",
        "status": "pending",
        "admin_notes": "",
    },

    # 3. Cancelled Booking
    {
        "user_email": "student@demo.edu",
        "resource_name": "Library Discussion Area",
        "booking_date": yesterday.isoformat(),
        "start_time": "11:00",
        "end_time": "13:00",
        "purpose": "Mini Project Team Discussion",
        "status": "cancelled",
        "admin_notes": "Cancelled by student as team rescheduled to lab.",
    },
]

# -----------------------------------------------------------------------------
# 6. REALISTIC CAMPUS MAINTENANCE ISSUES
# -----------------------------------------------------------------------------
SAMPLE_ISSUES = [
    {
        "user_email": "staff@demo.edu",
        "resource_name": "Samza AIML Lab",
        "title": "Workstation Node 14 GPU Driver issue during PyTorch training",
        "category": "Computer/Hardware",
        "priority": "high",
        "status": "in_progress",
        "description": "System 14 shows display error when allocating CUDA memory. Needs driver update.",
        "admin_response": "System admin instructed to re-install CUDA toolkit.",
    },
    {
        "user_email": "faculty.labs@jabin.edu",
        "resource_name": "Ubuntu Hall",
        "title": "Smart Board HDMI connection loose on podium",
        "category": "Projector/AV",
        "priority": "medium",
        "status": "open",
        "description": "Screen flickers while presenting slides from laptop.",
        "admin_response": "",
    },
    {
        "user_email": "student@demo.edu",
        "resource_name": "Hadoop Big Data Lab",
        "title": "Row 2 Wi-Fi access point intermittently dropping connections",
        "category": "Internet/Wi-Fi",
        "priority": "high",
        "status": "in_progress",
        "description": "Desktops 09 to 16 lose LAN connectivity during Android SDK downloads.",
        "admin_response": "Network engineer checking Ethernet patch cord.",
    },
    {
        "user_email": "staff@demo.edu",
        "resource_name": "Cloudera 2 Lab (DBMS Lab)",
        "title": "MySQL service stopped unexpectedly on host 04",
        "category": "Computer/Hardware",
        "priority": "medium",
        "status": "resolved",
        "description": "MySQL 8.0 daemon crashed due to disk space limit on /var.",
        "admin_response": "Temporary tables purged and service restarted. Operating normally.",
    },
]

# -----------------------------------------------------------------------------
# 7. NOTIFICATIONS
# -----------------------------------------------------------------------------
SAMPLE_NOTIFICATIONS = [
    {
        "user_email": "student@demo.edu",
        "title": "Welcome to P.C. Jabin Smart Campus!",
        "message": "Explore campus facilities, check real-time lab availability, and submit booking requests.",
    },
    {
        "user_email": "staff@demo.edu",
        "title": "Flink Lab Approved",
        "message": "Your reservation for Flink Lab tomorrow 2:00 PM - 4:00 PM is approved.",
    },
    {
        "user_email": "faculty.labs@jabin.edu",
        "title": "Samza AIML Lab Confirmed",
        "message": "Your booking for Samza AIML Lab today 11:00 AM - 1:00 PM is active.",
    },
    {
        "user_email": "admin@demo.edu",
        "title": "New Booking Requests Pending",
        "message": "3 facility requests for Ubuntu Hall, Windows Hall, and Cloudera 3 Lab await your review.",
    },
]
