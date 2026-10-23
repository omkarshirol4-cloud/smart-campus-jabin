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


# -----------------------------------------------------------------------------
# 8. OFFICIAL WEEKLY TIMETABLE CLASSES (BCA I, III & V Semesters)
# Grounded in official college timetables (Monday to Saturday)
# -----------------------------------------------------------------------------
TIMETABLE_CLASSES = [
    # --- Ubuntu Hall (BCA III Semester - A1 Division) ---
    {"resource_name": "Ubuntu Hall", "day_of_week": "Monday", "start_time": "09:00", "end_time": "10:00", "course_name": "Linear Algebra, Statistics & Probability", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Monday", "start_time": "10:00", "end_time": "11:00", "course_name": "Introduction to Artificial Intelligence", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Monday", "start_time": "11:00", "end_time": "12:00", "course_name": "English Communication", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Monday", "start_time": "12:00", "end_time": "13:00", "course_name": "Design and Analysis of Algorithms", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Monday", "start_time": "14:00", "end_time": "15:00", "course_name": "Advance Java with Frameworks", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Ubuntu Hall", "day_of_week": "Tuesday", "start_time": "09:00", "end_time": "10:00", "course_name": "Introduction to Artificial Intelligence", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Tuesday", "start_time": "10:00", "end_time": "11:00", "course_name": "Advance Java with Frameworks", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Tuesday", "start_time": "11:00", "end_time": "12:00", "course_name": "Design and Analysis of Algorithms", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Tuesday", "start_time": "12:00", "end_time": "13:00", "course_name": "Kannada / Hindi Language", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Tuesday", "start_time": "14:00", "end_time": "15:00", "course_name": "Linear Algebra, Statistics & Probability", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Ubuntu Hall", "day_of_week": "Wednesday", "start_time": "09:00", "end_time": "10:00", "course_name": "Kannada / Hindi Language", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Wednesday", "start_time": "10:00", "end_time": "11:00", "course_name": "English Communication", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Wednesday", "start_time": "11:00", "end_time": "12:00", "course_name": "Introduction to Artificial Intelligence", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Wednesday", "start_time": "12:00", "end_time": "13:00", "course_name": "Linear Algebra, Statistics & Probability", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Wednesday", "start_time": "14:00", "end_time": "15:00", "course_name": "Design and Analysis of Algorithms", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Ubuntu Hall", "day_of_week": "Thursday", "start_time": "09:00", "end_time": "10:00", "course_name": "Introduction to Artificial Intelligence", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Thursday", "start_time": "10:00", "end_time": "11:00", "course_name": "Advance Java with Frameworks", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Thursday", "start_time": "11:00", "end_time": "12:00", "course_name": "Design and Analysis of Algorithms", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Thursday", "start_time": "12:00", "end_time": "13:00", "course_name": "English Communication", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Thursday", "start_time": "14:00", "end_time": "15:00", "course_name": "Advance Java with Frameworks", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Ubuntu Hall", "day_of_week": "Friday", "start_time": "09:00", "end_time": "10:00", "course_name": "Activity / Technical Screening", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Friday", "start_time": "10:00", "end_time": "11:00", "course_name": "Advance Java with Frameworks", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Friday", "start_time": "11:00", "end_time": "12:00", "course_name": "Design and Analysis of Algorithms", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Friday", "start_time": "12:00", "end_time": "13:00", "course_name": "Introduction to Artificial Intelligence", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Friday", "start_time": "14:00", "end_time": "15:00", "course_name": "Linear Algebra, Statistics & Probability", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Ubuntu Hall", "day_of_week": "Saturday", "start_time": "09:00", "end_time": "10:00", "course_name": "Linear Algebra, Statistics & Probability", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Saturday", "start_time": "10:00", "end_time": "11:00", "course_name": "Introduction to Artificial Intelligence", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Saturday", "start_time": "11:00", "end_time": "12:00", "course_name": "Advance Web Technologies", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Saturday", "start_time": "12:00", "end_time": "13:00", "course_name": "Design and Analysis of Algorithms", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Ubuntu Hall", "day_of_week": "Saturday", "start_time": "14:00", "end_time": "15:00", "course_name": "Advance Java with Frameworks", "division": "BCA III (A1)", "faculty_title": "Faculty Coordinator"},

    # --- Windows Hall (BCA III Semester - A2 Division) ---
    {"resource_name": "Windows Hall", "day_of_week": "Monday", "start_time": "09:00", "end_time": "10:00", "course_name": "Advance Java with Frameworks", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Windows Hall", "day_of_week": "Monday", "start_time": "10:00", "end_time": "11:00", "course_name": "Kannada / Hindi Language", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Windows Hall", "day_of_week": "Monday", "start_time": "11:00", "end_time": "12:00", "course_name": "Introduction to Artificial Intelligence", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Windows Hall", "day_of_week": "Monday", "start_time": "12:00", "end_time": "13:00", "course_name": "Design and Analysis of Algorithms", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Windows Hall", "day_of_week": "Monday", "start_time": "14:00", "end_time": "15:00", "course_name": "Linear Algebra, Statistics & Probability", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Windows Hall", "day_of_week": "Tuesday", "start_time": "09:00", "end_time": "10:00", "course_name": "Advance Java with Frameworks", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Windows Hall", "day_of_week": "Tuesday", "start_time": "10:00", "end_time": "11:00", "course_name": "Design and Analysis of Algorithms", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Windows Hall", "day_of_week": "Tuesday", "start_time": "11:00", "end_time": "12:00", "course_name": "Introduction to Artificial Intelligence", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Windows Hall", "day_of_week": "Tuesday", "start_time": "12:00", "end_time": "13:00", "course_name": "English Communication", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Windows Hall", "day_of_week": "Wednesday", "start_time": "09:00", "end_time": "10:00", "course_name": "Design and Analysis of Algorithms", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Windows Hall", "day_of_week": "Wednesday", "start_time": "10:00", "end_time": "11:00", "course_name": "Advance Java with Frameworks", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Windows Hall", "day_of_week": "Wednesday", "start_time": "11:00", "end_time": "12:00", "course_name": "Introduction to Artificial Intelligence", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Windows Hall", "day_of_week": "Wednesday", "start_time": "12:00", "end_time": "13:00", "course_name": "Kannada / Hindi Language", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Windows Hall", "day_of_week": "Thursday", "start_time": "09:00", "end_time": "10:00", "course_name": "Kannada / Hindi Language", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Windows Hall", "day_of_week": "Thursday", "start_time": "10:00", "end_time": "11:00", "course_name": "English Communication", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Windows Hall", "day_of_week": "Thursday", "start_time": "11:00", "end_time": "12:00", "course_name": "Design and Analysis of Algorithms", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Windows Hall", "day_of_week": "Thursday", "start_time": "12:00", "end_time": "13:00", "course_name": "Advance Java with Frameworks", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Windows Hall", "day_of_week": "Friday", "start_time": "09:00", "end_time": "10:00", "course_name": "English Communication", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Windows Hall", "day_of_week": "Friday", "start_time": "10:00", "end_time": "11:00", "course_name": "Linear Algebra, Statistics & Probability", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Windows Hall", "day_of_week": "Friday", "start_time": "11:00", "end_time": "12:00", "course_name": "Design and Analysis of Algorithms", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Windows Hall", "day_of_week": "Friday", "start_time": "12:00", "end_time": "13:00", "course_name": "Introduction to Artificial Intelligence", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Windows Hall", "day_of_week": "Saturday", "start_time": "09:00", "end_time": "10:00", "course_name": "English Communication", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Windows Hall", "day_of_week": "Saturday", "start_time": "10:00", "end_time": "11:00", "course_name": "Linear Algebra, Statistics & Probability", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Windows Hall", "day_of_week": "Saturday", "start_time": "11:00", "end_time": "12:00", "course_name": "Advance Java with Frameworks", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Windows Hall", "day_of_week": "Saturday", "start_time": "12:00", "end_time": "13:00", "course_name": "Design and Analysis of Algorithms", "division": "BCA III (A2)", "faculty_title": "Faculty Coordinator"},

    # --- iOS Hall (BCA III A3 & BCA V A5) ---
    {"resource_name": "iOS Hall", "day_of_week": "Monday", "start_time": "09:00", "end_time": "11:00", "course_name": "Hindi/Kannada & DAA", "division": "BCA III (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "iOS Hall", "day_of_week": "Monday", "start_time": "11:00", "end_time": "13:00", "course_name": "Advance Java & Linear Algebra", "division": "BCA III (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "iOS Hall", "day_of_week": "Monday", "start_time": "14:00", "end_time": "16:00", "course_name": "Cyber Security & Cryptography", "division": "BCA V (A5)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "iOS Hall", "day_of_week": "Tuesday", "start_time": "09:00", "end_time": "11:00", "course_name": "Advance Java & Hindi/Kan", "division": "BCA III (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "iOS Hall", "day_of_week": "Tuesday", "start_time": "11:00", "end_time": "13:00", "course_name": "Linear Algebra & English", "division": "BCA III (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "iOS Hall", "day_of_week": "Tuesday", "start_time": "14:00", "end_time": "16:00", "course_name": "Cryptography & Activity", "division": "BCA V (A5)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "iOS Hall", "day_of_week": "Wednesday", "start_time": "09:00", "end_time": "11:00", "course_name": "Hindi/Kan & DAA", "division": "BCA III (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "iOS Hall", "day_of_week": "Wednesday", "start_time": "11:00", "end_time": "13:00", "course_name": "Intro to AI & Adv Java", "division": "BCA III (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "iOS Hall", "day_of_week": "Wednesday", "start_time": "14:00", "end_time": "16:00", "course_name": "Research Methodology & Cyber Security", "division": "BCA V (A5)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "iOS Hall", "day_of_week": "Thursday", "start_time": "09:00", "end_time": "11:00", "course_name": "Intro to AI & Adv Java", "division": "BCA III (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "iOS Hall", "day_of_week": "Thursday", "start_time": "11:00", "end_time": "13:00", "course_name": "Linear Algebra & DAA", "division": "BCA III (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "iOS Hall", "day_of_week": "Thursday", "start_time": "14:00", "end_time": "16:00", "course_name": "Android Programming & Crypto", "division": "BCA V (A5)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "iOS Hall", "day_of_week": "Friday", "start_time": "09:00", "end_time": "11:00", "course_name": "Intro to AI & DAA", "division": "BCA III (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "iOS Hall", "day_of_week": "Friday", "start_time": "11:00", "end_time": "13:00", "course_name": "Linear Algebra & English", "division": "BCA III (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "iOS Hall", "day_of_week": "Friday", "start_time": "14:00", "end_time": "16:00", "course_name": "Cyber Security & Cryptography", "division": "BCA V (A5)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "iOS Hall", "day_of_week": "Saturday", "start_time": "09:00", "end_time": "11:00", "course_name": "DAA & Intro to AI", "division": "BCA III (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "iOS Hall", "day_of_week": "Saturday", "start_time": "11:00", "end_time": "13:00", "course_name": "English & Adv Java", "division": "BCA III (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "iOS Hall", "day_of_week": "Saturday", "start_time": "14:00", "end_time": "16:00", "course_name": "Android Programming & Cyber Security", "division": "BCA V (A5)", "faculty_title": "Faculty Coordinator"},

    # --- Fedora Hall (BCA III Semester - A4 Division) ---
    {"resource_name": "Fedora Hall", "day_of_week": "Monday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA III Core Lectures (DAA, AI, Java)", "division": "BCA III (A4)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Fedora Hall", "day_of_week": "Tuesday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA III Core Lectures (Linear Algebra, Java)", "division": "BCA III (A4)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Fedora Hall", "day_of_week": "Wednesday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA III Core Lectures (AI, DAA, Web)", "division": "BCA III (A4)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Fedora Hall", "day_of_week": "Thursday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA III Core Lectures (Java, Linear Algebra)", "division": "BCA III (A4)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Fedora Hall", "day_of_week": "Friday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA III Core Lectures (AI, Java, English)", "division": "BCA III (A4)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Fedora Hall", "day_of_week": "Saturday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA III Core Lectures (DAA, Linear Algebra)", "division": "BCA III (A4)", "faculty_title": "Faculty Coordinator"},

    # --- Android Hall (BCA III Semester - A5 Division) ---
    {"resource_name": "Android Hall", "day_of_week": "Monday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA III Core Lectures (DAA, AI, Java)", "division": "BCA III (A5)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Android Hall", "day_of_week": "Tuesday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA III Core Lectures (AI, Java, Stats)", "division": "BCA III (A5)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Android Hall", "day_of_week": "Wednesday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA III Core Lectures (Linear Algebra, DAA)", "division": "BCA III (A5)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Android Hall", "day_of_week": "Thursday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA III Core Lectures (Java, AI, English)", "division": "BCA III (A5)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Android Hall", "day_of_week": "Friday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA III Core Lectures (DAA, Java, Kannada)", "division": "BCA III (A5)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Android Hall", "day_of_week": "Saturday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA III Core Lectures (AI, Stats, Web)", "division": "BCA III (A5)", "faculty_title": "Faculty Coordinator"},

    # --- Norton Hall (BCA III Semester - A6 Division) ---
    {"resource_name": "Norton Hall", "day_of_week": "Monday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA III Cyber Security & Core Lectures", "division": "BCA III (A6)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Norton Hall", "day_of_week": "Tuesday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA III Core Lectures (AI, Java, DAA)", "division": "BCA III (A6)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Norton Hall", "day_of_week": "Wednesday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA III Core Lectures (Linear Algebra, DAA)", "division": "BCA III (A6)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Norton Hall", "day_of_week": "Thursday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA III Core Lectures (Java, AI, English)", "division": "BCA III (A6)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Norton Hall", "day_of_week": "Friday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA III Core Lectures (DAA, Cyber Law)", "division": "BCA III (A6)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Norton Hall", "day_of_week": "Saturday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA III Core Lectures (Java, Stats)", "division": "BCA III (A6)", "faculty_title": "Faculty Coordinator"},

    # --- Panda Hall (BCA V Semester - A1 Division) ---
    {"resource_name": "Panda Hall", "day_of_week": "Monday", "start_time": "09:00", "end_time": "10:00", "course_name": "Android Programming", "division": "BCA V (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Panda Hall", "day_of_week": "Monday", "start_time": "10:00", "end_time": "11:00", "course_name": "Artificial Intelligence", "division": "BCA V (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Panda Hall", "day_of_week": "Tuesday", "start_time": "09:00", "end_time": "10:00", "course_name": "Artificial Intelligence", "division": "BCA V (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Panda Hall", "day_of_week": "Tuesday", "start_time": "10:00", "end_time": "11:00", "course_name": "Introduction to Machine Learning", "division": "BCA V (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Panda Hall", "day_of_week": "Wednesday", "start_time": "09:00", "end_time": "10:00", "course_name": "Research Methodology", "division": "BCA V (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Panda Hall", "day_of_week": "Wednesday", "start_time": "10:00", "end_time": "11:00", "course_name": "Android Programming", "division": "BCA V (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Panda Hall", "day_of_week": "Wednesday", "start_time": "11:00", "end_time": "12:00", "course_name": "Artificial Intelligence", "division": "BCA V (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Panda Hall", "day_of_week": "Thursday", "start_time": "09:00", "end_time": "10:00", "course_name": "Placement Preparation Session", "division": "BCA V (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Panda Hall", "day_of_week": "Thursday", "start_time": "10:00", "end_time": "11:00", "course_name": "Introduction to Machine Learning", "division": "BCA V (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Panda Hall", "day_of_week": "Thursday", "start_time": "11:00", "end_time": "12:00", "course_name": "Android Programming", "division": "BCA V (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Panda Hall", "day_of_week": "Friday", "start_time": "09:00", "end_time": "10:00", "course_name": "Android Programming", "division": "BCA V (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Panda Hall", "day_of_week": "Friday", "start_time": "10:00", "end_time": "11:00", "course_name": "Introduction to Machine Learning", "division": "BCA V (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Panda Hall", "day_of_week": "Saturday", "start_time": "09:00", "end_time": "10:00", "course_name": "Artificial Intelligence", "division": "BCA V (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Panda Hall", "day_of_week": "Saturday", "start_time": "10:00", "end_time": "11:00", "course_name": "Research Methodology", "division": "BCA V (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Panda Hall", "day_of_week": "Saturday", "start_time": "11:00", "end_time": "12:00", "course_name": "Introduction to Machine Learning", "division": "BCA V (A1)", "faculty_title": "Faculty Coordinator"},

    # --- AVG Hall (BCA V Semester - A2 Division) ---
    {"resource_name": "AVG Hall", "day_of_week": "Monday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA V Lectures (Android, AI, ML)", "division": "BCA V (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "AVG Hall", "day_of_week": "Tuesday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA V Lectures (AI, Machine Learning)", "division": "BCA V (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "AVG Hall", "day_of_week": "Wednesday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA V Lectures (Research Methodology, AI)", "division": "BCA V (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "AVG Hall", "day_of_week": "Thursday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA V Lectures (Placement Prep, ML, Android)", "division": "BCA V (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "AVG Hall", "day_of_week": "Friday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA V Lectures (Android, Machine Learning)", "division": "BCA V (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "AVG Hall", "day_of_week": "Saturday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA V Lectures (AI, RM, Machine Learning)", "division": "BCA V (A2)", "faculty_title": "Faculty Coordinator"},

    # --- Viper Hall (BCA V Semester - A3 Division) ---
    {"resource_name": "Viper Hall", "day_of_week": "Monday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA V Lectures (ML, Android, AI)", "division": "BCA V (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Viper Hall", "day_of_week": "Tuesday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA V Lectures (Machine Learning, Android)", "division": "BCA V (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Viper Hall", "day_of_week": "Wednesday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA V Lectures (AI, ML, Android)", "division": "BCA V (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Viper Hall", "day_of_week": "Thursday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA V Lectures (AI, Android, ML)", "division": "BCA V (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Viper Hall", "day_of_week": "Friday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA V Lectures (Research Methodology, Activity)", "division": "BCA V (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Viper Hall", "day_of_week": "Saturday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA V Lectures (Placement Prep, RM, Full Stack)", "division": "BCA V (A3)", "faculty_title": "Faculty Coordinator"},

    # --- MAC Hall (BCA V Semester - A4 Division) ---
    {"resource_name": "MAC Hall", "day_of_week": "Monday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA V Lectures (AI, RM, Android)", "division": "BCA V (A4)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "MAC Hall", "day_of_week": "Tuesday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA V Lectures (AI, Android, Placement Prep)", "division": "BCA V (A4)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "MAC Hall", "day_of_week": "Wednesday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA V Lectures (RM, Android, ML)", "division": "BCA V (A4)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "MAC Hall", "day_of_week": "Thursday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA V Lectures (ML, AI, Full Stack)", "division": "BCA V (A4)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "MAC Hall", "day_of_week": "Friday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA V Lectures (AI, Machine Learning)", "division": "BCA V (A4)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "MAC Hall", "day_of_week": "Saturday", "start_time": "09:00", "end_time": "13:00", "course_name": "BCA V Lectures (Android, ML, Research Methodology)", "division": "BCA V (A4)", "faculty_title": "Faculty Coordinator"},

    # --- Avira Hall (BCA I Semester - A1 Division) ---
    {"resource_name": "Avira Hall", "day_of_week": "Monday", "start_time": "09:00", "end_time": "10:00", "course_name": "Database Management Systems", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Avira Hall", "day_of_week": "Monday", "start_time": "10:00", "end_time": "11:00", "course_name": "Kannada Language", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Avira Hall", "day_of_week": "Monday", "start_time": "11:00", "end_time": "12:00", "course_name": "Data Structures using C", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Avira Hall", "day_of_week": "Monday", "start_time": "12:00", "end_time": "13:00", "course_name": "English Communication", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Avira Hall", "day_of_week": "Tuesday", "start_time": "10:00", "end_time": "11:00", "course_name": "Database Management Systems", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Avira Hall", "day_of_week": "Tuesday", "start_time": "11:00", "end_time": "12:00", "course_name": "Kannada Language", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Avira Hall", "day_of_week": "Tuesday", "start_time": "12:00", "end_time": "13:00", "course_name": "Educational Movie Screening", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Avira Hall", "day_of_week": "Wednesday", "start_time": "09:00", "end_time": "10:00", "course_name": "Discrete Mathematical Structures", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Avira Hall", "day_of_week": "Wednesday", "start_time": "10:00", "end_time": "11:00", "course_name": "Constitutional Values - 1", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Avira Hall", "day_of_week": "Wednesday", "start_time": "11:00", "end_time": "12:00", "course_name": "Data Structures using C", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Avira Hall", "day_of_week": "Wednesday", "start_time": "12:00", "end_time": "13:00", "course_name": "English Communication", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Avira Hall", "day_of_week": "Thursday", "start_time": "09:00", "end_time": "10:00", "course_name": "English Communication", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Avira Hall", "day_of_week": "Thursday", "start_time": "10:00", "end_time": "11:00", "course_name": "Discrete Mathematical Structures", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Avira Hall", "day_of_week": "Thursday", "start_time": "11:00", "end_time": "12:00", "course_name": "Database Management Systems", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Avira Hall", "day_of_week": "Thursday", "start_time": "12:00", "end_time": "13:00", "course_name": "Data Structures using C", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Avira Hall", "day_of_week": "Friday", "start_time": "09:00", "end_time": "10:00", "course_name": "English Communication", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Avira Hall", "day_of_week": "Friday", "start_time": "10:00", "end_time": "11:00", "course_name": "Constitutional Values - 1", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Avira Hall", "day_of_week": "Friday", "start_time": "11:00", "end_time": "12:00", "course_name": "Database Management Systems", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Avira Hall", "day_of_week": "Saturday", "start_time": "09:00", "end_time": "10:00", "course_name": "Data Structures using C", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Avira Hall", "day_of_week": "Saturday", "start_time": "10:00", "end_time": "11:00", "course_name": "Kannada Language", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Avira Hall", "day_of_week": "Saturday", "start_time": "11:00", "end_time": "12:00", "course_name": "Activity / Workshop", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Avira Hall", "day_of_week": "Saturday", "start_time": "12:00", "end_time": "13:00", "course_name": "Discrete Mathematical Structures", "division": "BCA I (A1)", "faculty_title": "Faculty Coordinator"},

    # --- ESET Hall (BCA I Semester - A2 Division) ---
    {"resource_name": "ESET Hall", "day_of_week": "Monday", "start_time": "09:00", "end_time": "10:00", "course_name": "Kannada Language", "division": "BCA I (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "ESET Hall", "day_of_week": "Monday", "start_time": "10:00", "end_time": "11:00", "course_name": "Data Structures using C", "division": "BCA I (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "ESET Hall", "day_of_week": "Monday", "start_time": "11:00", "end_time": "12:00", "course_name": "Database Management Systems", "division": "BCA I (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "ESET Hall", "day_of_week": "Monday", "start_time": "12:00", "end_time": "13:00", "course_name": "Discrete Mathematical Structures", "division": "BCA I (A2)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "ESET Hall", "day_of_week": "Tuesday", "start_time": "09:00", "end_time": "10:00", "course_name": "Kannada Language", "division": "BCA I (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "ESET Hall", "day_of_week": "Tuesday", "start_time": "10:00", "end_time": "11:00", "course_name": "Data Structures using C", "division": "BCA I (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "ESET Hall", "day_of_week": "Tuesday", "start_time": "11:00", "end_time": "13:00", "course_name": "English Communication (Double Period)", "division": "BCA I (A2)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "ESET Hall", "day_of_week": "Wednesday", "start_time": "09:00", "end_time": "10:00", "course_name": "Data Structures using C", "division": "BCA I (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "ESET Hall", "day_of_week": "Wednesday", "start_time": "10:00", "end_time": "11:00", "course_name": "Discrete Mathematical Structures", "division": "BCA I (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "ESET Hall", "day_of_week": "Wednesday", "start_time": "11:00", "end_time": "12:00", "course_name": "English Communication", "division": "BCA I (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "ESET Hall", "day_of_week": "Wednesday", "start_time": "12:00", "end_time": "13:00", "course_name": "Database Management Systems", "division": "BCA I (A2)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "ESET Hall", "day_of_week": "Thursday", "start_time": "09:00", "end_time": "10:00", "course_name": "Database Management Systems", "division": "BCA I (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "ESET Hall", "day_of_week": "Thursday", "start_time": "10:00", "end_time": "11:00", "course_name": "Kannada Language", "division": "BCA I (A2)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "ESET Hall", "day_of_week": "Friday", "start_time": "09:00", "end_time": "10:00", "course_name": "Discrete Mathematical Structures", "division": "BCA I (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "ESET Hall", "day_of_week": "Friday", "start_time": "10:00", "end_time": "11:00", "course_name": "Data Structures using C", "division": "BCA I (A2)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "ESET Hall", "day_of_week": "Saturday", "start_time": "09:00", "end_time": "10:00", "course_name": "English Communication", "division": "BCA I (A2)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "ESET Hall", "day_of_week": "Saturday", "start_time": "10:00", "end_time": "11:00", "course_name": "Database Management Systems", "division": "BCA I (A2)", "faculty_title": "Faculty Coordinator"},

    # --- Mcafee Hall (BCA I Semester - A3 Division) ---
    {"resource_name": "Mcafee Hall", "day_of_week": "Monday", "start_time": "09:00", "end_time": "10:00", "course_name": "Database Management Systems", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Mcafee Hall", "day_of_week": "Monday", "start_time": "10:00", "end_time": "11:00", "course_name": "English Communication", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Mcafee Hall", "day_of_week": "Tuesday", "start_time": "09:00", "end_time": "10:00", "course_name": "Discrete Mathematical Structures", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Mcafee Hall", "day_of_week": "Tuesday", "start_time": "10:00", "end_time": "11:00", "course_name": "English Communication", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Mcafee Hall", "day_of_week": "Wednesday", "start_time": "09:00", "end_time": "10:00", "course_name": "English Communication", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Mcafee Hall", "day_of_week": "Wednesday", "start_time": "10:00", "end_time": "11:00", "course_name": "Data Structures using C", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Mcafee Hall", "day_of_week": "Thursday", "start_time": "09:00", "end_time": "10:00", "course_name": "English Communication", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Mcafee Hall", "day_of_week": "Thursday", "start_time": "10:00", "end_time": "11:00", "course_name": "Constitutional Values - 1", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Mcafee Hall", "day_of_week": "Thursday", "start_time": "11:00", "end_time": "12:00", "course_name": "Database Management Systems", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Mcafee Hall", "day_of_week": "Thursday", "start_time": "12:00", "end_time": "13:00", "course_name": "Kannada Language", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Mcafee Hall", "day_of_week": "Thursday", "start_time": "14:00", "end_time": "15:00", "course_name": "Data Structures using C", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Mcafee Hall", "day_of_week": "Friday", "start_time": "09:00", "end_time": "10:00", "course_name": "Constitutional Values - 1", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Mcafee Hall", "day_of_week": "Friday", "start_time": "10:00", "end_time": "11:00", "course_name": "Data Structures using C", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Mcafee Hall", "day_of_week": "Friday", "start_time": "11:00", "end_time": "12:00", "course_name": "Kannada Language", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Mcafee Hall", "day_of_week": "Friday", "start_time": "12:00", "end_time": "13:00", "course_name": "Database Management Systems", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Mcafee Hall", "day_of_week": "Friday", "start_time": "14:00", "end_time": "15:00", "course_name": "Discrete Mathematical Structures", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},

    {"resource_name": "Mcafee Hall", "day_of_week": "Saturday", "start_time": "09:00", "end_time": "10:00", "course_name": "Discrete Mathematical Structures", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Mcafee Hall", "day_of_week": "Saturday", "start_time": "10:00", "end_time": "11:00", "course_name": "Kannada Language", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Mcafee Hall", "day_of_week": "Saturday", "start_time": "11:00", "end_time": "12:00", "course_name": "Data Structures using C", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Mcafee Hall", "day_of_week": "Saturday", "start_time": "12:00", "end_time": "13:00", "course_name": "Database Management Systems", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},
    {"resource_name": "Mcafee Hall", "day_of_week": "Saturday", "start_time": "14:00", "end_time": "15:00", "course_name": "Technical Activity / Screening", "division": "BCA I (A3)", "faculty_title": "Faculty Coordinator"},

    # --- Specialized Computer Laboratories (Recurring Lab Practicals) ---
    # Flink Lab: BCA III Advance Java Practical Lab
    {"resource_name": "Flink Lab", "day_of_week": "Monday", "start_time": "14:00", "end_time": "17:00", "course_name": "Advance Java with Frameworks Lab", "division": "BCA III (A1/A2)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Flink Lab", "day_of_week": "Tuesday", "start_time": "14:00", "end_time": "17:00", "course_name": "Advance Java with Frameworks Lab", "division": "BCA III (A3/A4)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Flink Lab", "day_of_week": "Wednesday", "start_time": "14:00", "end_time": "17:00", "course_name": "Advance Java with Frameworks Lab", "division": "BCA III (A5/A6)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Flink Lab", "day_of_week": "Thursday", "start_time": "14:00", "end_time": "17:00", "course_name": "Advance Java with Frameworks Lab", "division": "BCA III (A1/A2)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Flink Lab", "day_of_week": "Friday", "start_time": "14:00", "end_time": "17:00", "course_name": "Advance Java with Frameworks Lab", "division": "BCA III (A3/A4)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Flink Lab", "day_of_week": "Saturday", "start_time": "14:00", "end_time": "17:00", "course_name": "Advance Java with Frameworks Lab", "division": "BCA III (A5/A6)", "faculty_title": "Faculty Lab In-Charge"},

    # Cloudera 3 Lab: BCA III AI Practical Lab
    {"resource_name": "Cloudera 3 Lab (AI & Security)", "day_of_week": "Monday", "start_time": "14:00", "end_time": "17:00", "course_name": "Introduction to Artificial Intelligence Lab", "division": "BCA III (A2)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Cloudera 3 Lab (AI & Security)", "day_of_week": "Tuesday", "start_time": "14:00", "end_time": "17:00", "course_name": "Introduction to Artificial Intelligence Lab", "division": "BCA III (A3)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Cloudera 3 Lab (AI & Security)", "day_of_week": "Wednesday", "start_time": "14:00", "end_time": "17:00", "course_name": "Introduction to Artificial Intelligence Lab", "division": "BCA III (A1)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Cloudera 3 Lab (AI & Security)", "day_of_week": "Thursday", "start_time": "14:00", "end_time": "17:00", "course_name": "Introduction to Artificial Intelligence Lab", "division": "BCA III (A2)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Cloudera 3 Lab (AI & Security)", "day_of_week": "Friday", "start_time": "14:00", "end_time": "17:00", "course_name": "Introduction to Artificial Intelligence Lab", "division": "BCA III (A3)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Cloudera 3 Lab (AI & Security)", "day_of_week": "Saturday", "start_time": "14:00", "end_time": "17:00", "course_name": "Introduction to Artificial Intelligence Lab", "division": "BCA III (A1)", "faculty_title": "Faculty Lab In-Charge"},

    # Spark Lab: BCA III Adv MERN Stack Lab
    {"resource_name": "Spark Lab", "day_of_week": "Monday", "start_time": "14:00", "end_time": "17:00", "course_name": "Advance MERN Stack Lab", "division": "BCA III (A3)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Spark Lab", "day_of_week": "Tuesday", "start_time": "14:00", "end_time": "17:00", "course_name": "Advance MERN Stack Lab", "division": "BCA III (A1)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Spark Lab", "day_of_week": "Wednesday", "start_time": "14:00", "end_time": "17:00", "course_name": "Advance MERN Stack Lab", "division": "BCA III (A2)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Spark Lab", "day_of_week": "Thursday", "start_time": "14:00", "end_time": "17:00", "course_name": "Advance MERN Stack Lab", "division": "BCA III (A3)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Spark Lab", "day_of_week": "Friday", "start_time": "14:00", "end_time": "17:00", "course_name": "Advance MERN Stack Lab", "division": "BCA III (A1)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Spark Lab", "day_of_week": "Saturday", "start_time": "14:00", "end_time": "17:00", "course_name": "Advance MERN Stack Lab", "division": "BCA III (A2)", "faculty_title": "Faculty Lab In-Charge"},

    # Hadoop Big Data Lab: BCA V Android Programming Lab
    {"resource_name": "Hadoop Big Data Lab", "day_of_week": "Monday", "start_time": "14:00", "end_time": "17:00", "course_name": "Android Application Programming Lab", "division": "BCA V (A1)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Hadoop Big Data Lab", "day_of_week": "Tuesday", "start_time": "14:00", "end_time": "17:00", "course_name": "Android Application Programming Lab", "division": "BCA V (A2)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Hadoop Big Data Lab", "day_of_week": "Wednesday", "start_time": "14:00", "end_time": "17:00", "course_name": "Android Application Programming Lab", "division": "BCA V (A3)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Hadoop Big Data Lab", "day_of_week": "Thursday", "start_time": "14:00", "end_time": "17:00", "course_name": "Android Application Programming Lab", "division": "BCA V (A4)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Hadoop Big Data Lab", "day_of_week": "Friday", "start_time": "14:00", "end_time": "17:00", "course_name": "Android Application Programming Lab", "division": "BCA V (A5)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Hadoop Big Data Lab", "day_of_week": "Saturday", "start_time": "14:00", "end_time": "17:00", "course_name": "Android Application Programming Lab", "division": "BCA V (A6)", "faculty_title": "Faculty Lab In-Charge"},

    # Samza AIML Lab: BCA V AI & Machine Learning Lab
    {"resource_name": "Samza AIML Lab", "day_of_week": "Monday", "start_time": "14:00", "end_time": "17:00", "course_name": "Machine Learning & Neural Networks Lab", "division": "BCA V (A2)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Samza AIML Lab", "day_of_week": "Tuesday", "start_time": "14:00", "end_time": "17:00", "course_name": "Machine Learning & Neural Networks Lab", "division": "BCA V (A3)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Samza AIML Lab", "day_of_week": "Wednesday", "start_time": "14:00", "end_time": "17:00", "course_name": "Machine Learning & Neural Networks Lab", "division": "BCA V (A1)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Samza AIML Lab", "day_of_week": "Thursday", "start_time": "14:00", "end_time": "17:00", "course_name": "Machine Learning & Neural Networks Lab", "division": "BCA V (A2)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Samza AIML Lab", "day_of_week": "Friday", "start_time": "14:00", "end_time": "17:00", "course_name": "Machine Learning & Neural Networks Lab", "division": "BCA V (A3)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Samza AIML Lab", "day_of_week": "Saturday", "start_time": "14:00", "end_time": "17:00", "course_name": "Machine Learning & Neural Networks Lab", "division": "BCA V (A1)", "faculty_title": "Faculty Lab In-Charge"},

    # FSD Lab: BCA V Full Stack Development Lab
    {"resource_name": "FSD Lab (Full Stack)", "day_of_week": "Monday", "start_time": "14:00", "end_time": "17:00", "course_name": "Full Stack Development Practical Lab", "division": "BCA V (A3)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "FSD Lab (Full Stack)", "day_of_week": "Tuesday", "start_time": "14:00", "end_time": "17:00", "course_name": "Full Stack Development Practical Lab", "division": "BCA V (A1)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "FSD Lab (Full Stack)", "day_of_week": "Wednesday", "start_time": "14:00", "end_time": "17:00", "course_name": "Full Stack Development Practical Lab", "division": "BCA V (A2)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "FSD Lab (Full Stack)", "day_of_week": "Thursday", "start_time": "14:00", "end_time": "17:00", "course_name": "Full Stack Development Practical Lab", "division": "BCA V (A3)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "FSD Lab (Full Stack)", "day_of_week": "Friday", "start_time": "14:00", "end_time": "17:00", "course_name": "Full Stack Development Practical Lab", "division": "BCA V (A1)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "FSD Lab (Full Stack)", "day_of_week": "Saturday", "start_time": "14:00", "end_time": "17:00", "course_name": "Full Stack Development Practical Lab", "division": "BCA V (A2)", "faculty_title": "Faculty Lab In-Charge"},

    # Cloudera 1 Lab: BCA I Data Structures in C Lab
    {"resource_name": "Cloudera 1 Lab (DS Lab)", "day_of_week": "Monday", "start_time": "11:00", "end_time": "13:00", "course_name": "Data Structures in C Practical Lab", "division": "BCA I (A1/A3)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Cloudera 1 Lab (DS Lab)", "day_of_week": "Tuesday", "start_time": "11:00", "end_time": "13:00", "course_name": "Data Structures in C Practical Lab", "division": "BCA I (A2/A3)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Cloudera 1 Lab (DS Lab)", "day_of_week": "Wednesday", "start_time": "11:00", "end_time": "13:00", "course_name": "Data Structures in C Practical Lab", "division": "BCA I (A1/A2)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Cloudera 1 Lab (DS Lab)", "day_of_week": "Thursday", "start_time": "14:00", "end_time": "16:00", "course_name": "Data Structures in C Practical Lab", "division": "BCA I (A1/A3)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Cloudera 1 Lab (DS Lab)", "day_of_week": "Friday", "start_time": "14:00", "end_time": "16:00", "course_name": "Data Structures in C Practical Lab", "division": "BCA I (A2/A3)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Cloudera 1 Lab (DS Lab)", "day_of_week": "Saturday", "start_time": "14:00", "end_time": "16:00", "course_name": "Data Structures in C Practical Lab", "division": "BCA I (A1/A2)", "faculty_title": "Faculty Lab In-Charge"},

    # Cloudera 2 Lab: BCA I Database Management Systems Lab
    {"resource_name": "Cloudera 2 Lab (DBMS Lab)", "day_of_week": "Monday", "start_time": "11:00", "end_time": "13:00", "course_name": "Database Management Systems Lab", "division": "BCA I (A2/A3)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Cloudera 2 Lab (DBMS Lab)", "day_of_week": "Tuesday", "start_time": "11:00", "end_time": "13:00", "course_name": "Database Management Systems Lab", "division": "BCA I (A1/A3)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Cloudera 2 Lab (DBMS Lab)", "day_of_week": "Wednesday", "start_time": "11:00", "end_time": "13:00", "course_name": "Database Management Systems Lab", "division": "BCA I (A1/A2)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Cloudera 2 Lab (DBMS Lab)", "day_of_week": "Thursday", "start_time": "14:00", "end_time": "16:00", "course_name": "Database Management Systems Lab", "division": "BCA I (A2/A3)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Cloudera 2 Lab (DBMS Lab)", "day_of_week": "Friday", "start_time": "14:00", "end_time": "16:00", "course_name": "Database Management Systems Lab", "division": "BCA I (A1/A3)", "faculty_title": "Faculty Lab In-Charge"},
    {"resource_name": "Cloudera 2 Lab (DBMS Lab)", "day_of_week": "Saturday", "start_time": "14:00", "end_time": "16:00", "course_name": "Database Management Systems Lab", "division": "BCA I (A1/A2)", "faculty_title": "Faculty Lab In-Charge"},
]
