# seed_data.py
# Real Synthetic Data for KLE Society's P.C. Jabin Science College
# Bachelor of Computer Applications (BCA Department), Vidyanagar, Hubballi.
# Grounded in official III & V Semester Timetables and I Semester Schedules (2026-27).

from datetime import date, timedelta

# Default password for all demo and faculty accounts
DEFAULT_PASSWORD = "password123"

# -----------------------------------------------------------------------------
# 1. REAL FACULTY, STUDENT & ADMIN USERS (from official college timetables)
# -----------------------------------------------------------------------------
USERS = [
    # Demo standard logins
    {
        "email": "student@demo.edu",
        "full_name": "Rahul Patil (225AI015)",
        "role": "student",
        "department": "BCA III Sem (A1 Ubuntu)",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "staff@demo.edu",
        "full_name": "Prof. Savita G",
        "role": "staff",
        "department": "BCA Faculty (AI & Cyber Security)",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "admin@demo.edu",
        "full_name": "Dr. R. M. Hiremath",
        "role": "admin",
        "department": "Campus Administration & HOD",
        "password": DEFAULT_PASSWORD,
    },

    # Real Faculty Members from college timetables
    {
        "email": "prof.maheshrao@jabin.edu",
        "full_name": "Prof. Maheshrao",
        "role": "staff",
        "department": "BCA Faculty (AI & Research Methodology)",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "prof.sharada@jabin.edu",
        "full_name": "Prof. Sharada M",
        "role": "staff",
        "department": "BCA Faculty (Advance Java & Frameworks)",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "prof.poornimac@jabin.edu",
        "full_name": "Prof. Poornima C",
        "role": "staff",
        "department": "BCA Faculty (Android Programming & Cyber Law)",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "prof.deepak@jabin.edu",
        "full_name": "Prof. Deepak S",
        "role": "staff",
        "department": "BCA Faculty (Machine Learning & Full Stack)",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "prof.soniya@jabin.edu",
        "full_name": "Prof. Soniya G",
        "role": "staff",
        "department": "BCA Faculty (Artificial Intelligence Lab)",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "prof.ravikiran@jabin.edu",
        "full_name": "Prof. Ravikiran B",
        "role": "staff",
        "department": "BCA Faculty (AI & Cyber Security)",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "prof.shridevi@jabin.edu",
        "full_name": "Prof. Shridevi B Kuri",
        "role": "staff",
        "department": "BCA Faculty (Advance Java Frameworks)",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "prof.jyoti@jabin.edu",
        "full_name": "Prof. Jyothi K",
        "role": "staff",
        "department": "BCA Faculty (Design & Analysis of Algorithms)",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "prof.shilpa@jabin.edu",
        "full_name": "Prof. Shilpa",
        "role": "staff",
        "department": "BCA Faculty (DBMS & Cyber Security Lab)",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "prof.seemajain@jabin.edu",
        "full_name": "Prof. Seema Jain",
        "role": "staff",
        "department": "BCA Faculty (Cyber Security & Cyber Law)",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "prof.shashank@jabin.edu",
        "full_name": "Prof. Shashank J",
        "role": "staff",
        "department": "Mathematics (Linear Algebra, Stats & Probability)",
        "password": DEFAULT_PASSWORD,
    },

    # Real Student Representatives from Class Cohorts
    {
        "email": "kavya.225ai088@jabin.edu",
        "full_name": "Kavya Kulkarni (225AI088)",
        "role": "student",
        "department": "BCA III Sem (A2 Windows)",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "aditya.225cs280@jabin.edu",
        "full_name": "Aditya Joshi (225CS280)",
        "role": "student",
        "department": "BCA III Sem (A5 Division)",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "darshan.225ai160@jabin.edu",
        "full_name": "Darshan Gowda (225AI160)",
        "role": "student",
        "department": "BCA V Sem (A1 Panda)",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "pooja.u02as26@jabin.edu",
        "full_name": "Pooja Hiremath (U02AS26S0085)",
        "role": "student",
        "department": "BCA I Sem (A1 Avira)",
        "password": DEFAULT_PASSWORD,
    },
]

# -----------------------------------------------------------------------------
# 2. REAL CAMPUS FACILITIES & EQUIPMENT (from College Timetables)
# -----------------------------------------------------------------------------
RESOURCES = [
    # Lecture & Smart Digital Classrooms named after OS & Platforms
    {
        "name": "Ubuntu Hall",
        "type": "Room",
        "capacity": 75,
        "location": "BCA Block, Ground Floor (Room 101)",
        "description": "BCA III Sem (A1 Division) Classroom. Equipped with smart interactive board, motorized screen, and dual wall speakers.",
    },
    {
        "name": "Windows Hall",
        "type": "Room",
        "capacity": 75,
        "location": "BCA Block, Ground Floor (Room 102)",
        "description": "BCA III Sem (A2 Division) Classroom. Smart digital interactive board, podium mic, and LAN projection.",
    },
    {
        "name": "iOS Hall",
        "type": "Room",
        "capacity": 75,
        "location": "BCA Block, 1st Floor (Room 201)",
        "description": "BCA III (A3) & BCA V (A5) Lecture Hall. High-definition AV system, Apple AirPlay enabled smart display.",
    },
    {
        "name": "Fedora Hall",
        "type": "Room",
        "capacity": 75,
        "location": "BCA Block, 1st Floor (Room 202)",
        "description": "BCA III Sem (A4 Division) Classroom. Linux environment, interactive smart screen, and surround audio.",
    },
    {
        "name": "Android Hall",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Block, 2nd Floor (Room 301)",
        "description": "BCA III Sem (A5 Division) Hall. Dedicated mobile computing, Android emulator smart display, and digital podium.",
    },
    {
        "name": "AVG Hall",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Block, 2nd Floor (Room 302)",
        "description": "BCA III & V Semester Digital Classroom. Overhead projection, sound system, and motorized screen.",
    },
    {
        "name": "Mcafee Hall",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Block, 2nd Floor (Room 303)",
        "description": "BCA I Sem (A3) & BCA III (A5) Classroom. Smart digital interactive board and dual microphones.",
    },
    {
        "name": "Avira Hall",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Block, 3rd Floor (Room 401)",
        "description": "BCA I Sem (A1 Division) Foundation Classroom. Interactive digital smart board and high-clarity sound system.",
    },
    {
        "name": "ESET Hall",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Block, 3rd Floor (Room 402)",
        "description": "BCA I Sem (A2 Division) Classroom. Digital podium, overhead ceiling projector, and dual speakers.",
    },
    {
        "name": "Panda Hall",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Senior Wing, 1st Floor (Room 205)",
        "description": "BCA V Sem (A1 Division) Classroom. Advanced machine learning & AI theory lecture setup.",
    },
    {
        "name": "Viper Hall",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Senior Wing, 1st Floor (Room 206)",
        "description": "BCA V Sem (A3 Division) Classroom. Smart board, full stack development presentation environment.",
    },
    {
        "name": "MAC Hall",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Senior Wing, 2nd Floor (Room 305)",
        "description": "BCA V Sem (A4 Division) Classroom. Cloud computing & enterprise architecture presentation hall.",
    },
    {
        "name": "Norton Hall",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Senior Wing, 2nd Floor (Room 306)",
        "description": "BCA III Sem (A6 Division) Cyber Law, Network Security, and Ethics Classroom.",
    },
    {
        "name": "PG Hall No. 1",
        "type": "Room",
        "capacity": 85,
        "location": "PG & Research Wing, 2nd Floor",
        "description": "Joint lecture hall for postgraduate seminars, faculty research meetings, and guest lectures.",
    },
    {
        "name": "Twister Hall",
        "type": "Room",
        "capacity": 50,
        "location": "BCA Wing, 3rd Floor",
        "description": "Discussion, debate, and final year project review screening hall.",
    },

    # Specialized Computer Laboratories from College Timetables
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
        "description": "Android Programming & Distributed Big Data Lab. 60 high-performance systems with Android Studio.",
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
        "description": "Full Stack Development & Capstone Project Lab. Cloud-connected development nodes.",
    },
    {
        "name": "Language Laboratory",
        "type": "Room",
        "capacity": 40,
        "location": "Central Library Annex, 1st Floor",
        "description": "Audio-visual speech enhancement workstations and noise-canceling headsets for professional communication.",
    },

    # Campus Central Halls & Recreation
    {
        "name": "College Seminar Hall",
        "type": "Room",
        "capacity": 150,
        "location": "Main Administrative Block, 2nd Floor",
        "description": "Central auditorium equipped with motorized projector screen, stage lights, podium mic, and Ahuja PA sound system.",
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

    # Portable Equipment
    {
        "name": "Epson Full HD Portable Projector",
        "type": "Equipment",
        "capacity": 1,
        "location": "BCA Dept Office (Cabinet A1)",
        "description": "Portable 4000 lumens projector with HDMI, VGA, wireless dongle, and adjustable tripod stand.",
    },
    {
        "name": "BenQ High-Contrast Portable Projector",
        "type": "Equipment",
        "capacity": 1,
        "location": "BCA Dept Office (Cabinet A2)",
        "description": "Portable high-lumen projector for guest sessions in non-digital lecture halls.",
    },
    {
        "name": "Ahuja Portable PA Sound System",
        "type": "Equipment",
        "capacity": 1,
        "location": "BCA Dept Office (Audio Rack)",
        "description": "Ahuja rechargeable portable PA amplifier with two wireless handheld microphones.",
    },
    {
        "name": "Mobile Laptop Cart (20 Dell Laptops)",
        "type": "Equipment",
        "capacity": 20,
        "location": "BCA Dept Office (Charging Station)",
        "description": "Lockable mobile trolley with 20 charged Dell Core i5 laptops for hands-on campus workshops.",
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
# 5. REALISTIC SAMPLE BOOKINGS (Grounded in Timetable Sessions)
# -----------------------------------------------------------------------------
today = date.today()
tomorrow = today + timedelta(days=1)
day_after = today + timedelta(days=2)
yesterday = today - timedelta(days=1)

SAMPLE_BOOKINGS = [
    # 1. Approved Timetable Sessions
    {
        "user_email": "prof.poornimac@jabin.edu",
        "resource_name": "Hadoop Big Data Lab",
        "booking_date": today.isoformat(),
        "start_time": "11:00",
        "end_time": "13:00",
        "purpose": "BCA V Sem (A1 Panda) Android Lab - Batch B1 Practical Session",
        "status": "approved",
        "admin_notes": "Timetable scheduled practical. Android Studio verified.",
    },
    {
        "user_email": "prof.maheshrao@jabin.edu",
        "resource_name": "Samza AIML Lab",
        "booking_date": today.isoformat(),
        "start_time": "11:00",
        "end_time": "13:00",
        "purpose": "BCA V Sem (A1 Panda) AIML Lab - Batch B2 Machine Learning Models",
        "status": "approved",
        "admin_notes": "GPU workstation nodes reserved for model training.",
    },
    {
        "user_email": "prof.sharada@jabin.edu",
        "resource_name": "Flink Lab",
        "booking_date": tomorrow.isoformat(),
        "start_time": "14:00",
        "end_time": "16:00",
        "purpose": "BCA III Sem (A1 Ubuntu) Advance Java with Frameworks Lab - Batch B2",
        "status": "approved",
        "admin_notes": "Spring Boot & Hibernate lab environment.",
    },
    {
        "user_email": "staff@demo.edu",
        "resource_name": "Cloudera 3 Lab (AI & Security)",
        "booking_date": tomorrow.isoformat(),
        "start_time": "10:00",
        "end_time": "12:00",
        "purpose": "BCA III Sem (A5) Cyber Security & Ethical Hacking Hands-on Practical",
        "status": "approved",
        "admin_notes": "Wireshark & Packet Analyzer installed.",
    },
    {
        "user_email": "prof.deepak@jabin.edu",
        "resource_name": "College Seminar Hall",
        "booking_date": day_after.isoformat(),
        "start_time": "10:00",
        "end_time": "13:00",
        "purpose": "State-level BCA Technical Symposium & AI Project Exhibition",
        "status": "approved",
        "admin_notes": "HOD approved. Audio & AV team scheduled.",
    },

    # 2. Pending Requests Awaiting Administrator Review
    {
        "user_email": "student@demo.edu",
        "resource_name": "Ubuntu Hall",
        "booking_date": tomorrow.isoformat(),
        "start_time": "15:00",
        "end_time": "17:00",
        "purpose": "BCA III A1 Activity / Movie Screening & Tech Quiz Preparation",
        "status": "pending",
        "admin_notes": "",
    },
    {
        "user_email": "kavya.225ai088@jabin.edu",
        "resource_name": "Windows Hall",
        "booking_date": day_after.isoformat(),
        "start_time": "14:00",
        "end_time": "16:00",
        "purpose": "BCA III A2 Division Peer Coding Circle & Algorithm Review",
        "status": "pending",
        "admin_notes": "",
    },
    {
        "user_email": "prof.ravikiran@jabin.edu",
        "resource_name": "Cloudera 3 Lab (AI & Security)",
        "booking_date": day_after.isoformat(),
        "start_time": "14:00",
        "end_time": "16:00",
        "purpose": "Cyber Security Certification Practical Exam (Batch A6)",
        "status": "pending",
        "admin_notes": "",
    },

    # 3. Cancelled / Historical Bookings
    {
        "user_email": "darshan.225ai160@jabin.edu",
        "resource_name": "Epson Full HD Portable Projector",
        "booking_date": yesterday.isoformat(),
        "start_time": "11:00",
        "end_time": "13:00",
        "purpose": "Outdoor campus presentation for environmental science",
        "status": "cancelled",
        "admin_notes": "Cancelled by student as hall already had fixed projection.",
    },
]

# -----------------------------------------------------------------------------
# 6. REALISTIC CAMPUS MAINTENANCE ISSUES
# -----------------------------------------------------------------------------
SAMPLE_ISSUES = [
    {
        "user_email": "staff@demo.edu",
        "resource_name": "Samza AIML Lab",
        "title": "Workstation Node 14 GPU Driver crash during PyTorch training",
        "category": "Computer/Hardware",
        "priority": "high",
        "status": "in_progress",
        "description": "System 14 shows blue screen when CUDA memory is allocated. Needs driver update.",
        "admin_response": "System admin instructed to re-install NVIDIA CUDA 12.2 toolkit.",
    },
    {
        "user_email": "prof.sharada@jabin.edu",
        "resource_name": "Ubuntu Hall",
        "title": "Smart Board HDMI connection loose on podium",
        "category": "Projector/AV",
        "priority": "medium",
        "status": "open",
        "description": "Screen flickers while presenting slides from faculty laptop.",
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
        "admin_response": "Network engineer checking Ethernet patch cord and switch port 18.",
    },
    {
        "user_email": "prof.shilpa@jabin.edu",
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
# 7. REALISTIC NOTIFICATIONS
# -----------------------------------------------------------------------------
SAMPLE_NOTIFICATIONS = [
    {
        "user_email": "student@demo.edu",
        "title": "Welcome to P.C. Jabin Smart Campus!",
        "message": "Explore campus facilities, check real-time lab availability, and submit booking requests.",
    },
    {
        "user_email": "staff@demo.edu",
        "title": "Cloudera 3 Lab Approved",
        "message": "Your reservation for Cloudera 3 Lab on tomorrow 10:00 AM - 12:00 PM is approved.",
    },
    {
        "user_email": "prof.maheshrao@jabin.edu",
        "title": "Samza AIML Lab Confirmed",
        "message": "Your booking for BCA V Sem (A1 Panda) AIML Lab today 11:00 AM - 1:00 PM is active.",
    },
    {
        "user_email": "admin@demo.edu",
        "title": "New Booking Requests Pending",
        "message": "3 facility requests for Ubuntu Hall, Windows Hall, and Cloudera 3 Lab await your review.",
    },
]
