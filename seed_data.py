# seed_data.py
# Demo data for KLE Society's P.C. Jabin Science College (BCA Department), Hubballi.
# Edit names, capacities, and facilities here as needed.

from datetime import date, timedelta

# Default password for all demo accounts (easy to remember for presentation)
DEFAULT_PASSWORD = "password123"

# 1. Demo User Accounts
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
        "full_name": "Prof. Savita Kulkarni",
        "role": "staff",
        "department": "BCA Faculty",
        "password": DEFAULT_PASSWORD,
    },
    {
        "email": "admin@demo.edu",
        "full_name": "Dr. R. M. Hiremath",
        "role": "admin",
        "department": "Campus Administration",
        "password": DEFAULT_PASSWORD,
    },
]

# 2. Campus Facilities and Equipment (Rooms & Gear)
RESOURCES = [
    {
        "name": "Seminar Hall",
        "type": "Room",
        "capacity": 120,
        "location": "Main Block, 2nd Floor",
        "description": "Capacity 100+, fitted with ceiling projector, audio amplifier, and podium mic.",
    },
    {
        "name": "Computer Lab 1",
        "type": "Room",
        "capacity": 60,
        "location": "BCA Wing, Ground Floor",
        "description": "60 modern desktops, Gigabit LAN, Python/Java/MySQL lab environment.",
    },
    {
        "name": "Computer Lab 2",
        "type": "Room",
        "capacity": 60,
        "location": "BCA Wing, 1st Floor",
        "description": "60 desktops dedicated to web development, data science, and cloud computing.",
    },
    {
        "name": "Language Laboratory",
        "type": "Room",
        "capacity": 40,
        "location": "BCA Wing, 1st Floor",
        "description": "Dedicated language training workstations with high-clarity headsets.",
    },
    {
        "name": "Library Discussion Area",
        "type": "Room",
        "capacity": 25,
        "location": "Central Library, 1st Floor",
        "description": "Round tables, magnetic whiteboard, and quiet zone for student group study.",
    },
    {
        "name": "Classroom (digital) 1",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Wing, 2nd Floor",
        "description": "Smart digital interactive board, motorized screen, and wall speakers.",
    },
    {
        "name": "Classroom (digital) 2",
        "type": "Room",
        "capacity": 70,
        "location": "BCA Wing, 2nd Floor",
        "description": "Smart digital interactive board, motorized screen, and wall speakers.",
    },
    {
        "name": "Indoor Games Room",
        "type": "Room",
        "capacity": 30,
        "location": "Gymkhana Complex",
        "description": "Table tennis tables, chess boards, and carrom recreation space.",
    },
    {
        "name": "Portable Projector",
        "type": "Equipment",
        "capacity": 1,
        "location": "BCA Dept Office",
        "description": "Epson Full HD portable projector with HDMI cable and tripod stand.",
    },
    {
        "name": "Amplifier / Sound System",
        "type": "Equipment",
        "capacity": 1,
        "location": "BCA Dept Office",
        "description": "Ahuja portable PA sound system with two wireless handheld mics.",
    },
    {
        "name": "Laptop Cart",
        "type": "Equipment",
        "capacity": 20,
        "location": "BCA Dept Office",
        "description": "Mobile locking charging trolley with 20 ready-to-use Dell laptops.",
    },
]

# 3. Standard Issue Categories
ISSUE_CATEGORIES = [
    "Electrical",
    "Internet/Wi-Fi",
    "Computer/Hardware",
    "Furniture",
    "Cleanliness",
    "Projector/AV",
    "Other",
]

# 4. Standard Allowed Booking Hours (9:00 AM to 5:00 PM)
OPERATING_HOURS = {
    "start": "09:00",
    "end": "17:00",
}

# 5. Dynamic Sample Bookings (dates are calculated relative to today)
today = date.today()
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)

SAMPLE_BOOKINGS = [
    {
        "user_email": "staff@demo.edu",
        "resource_name": "Seminar Hall",
        "booking_date": tomorrow.isoformat(),
        "start_time": "10:00",
        "end_time": "12:00",
        "purpose": "State-level BCA Guest Lecture on AI and Cloud Computing",
        "status": "approved",
        "admin_notes": "Approved by HOD. AV technician informed.",
    },
    {
        "user_email": "student@demo.edu",
        "resource_name": "Computer Lab 1",
        "booking_date": today.isoformat(),
        "start_time": "14:00",
        "end_time": "16:00",
        "purpose": "BCA Final Year Project Team Coding & Testing Session",
        "status": "pending",
        "admin_notes": "Waiting for lab supervisor confirmation.",
    },
    {
        "user_email": "student@demo.edu",
        "resource_name": "Portable Projector",
        "booking_date": yesterday.isoformat(),
        "start_time": "11:00",
        "end_time": "13:00",
        "purpose": "Mini project presentation to external review panel",
        "status": "cancelled",
        "admin_notes": "Cancelled by student as room already had fixed projector.",
    },
]

# 6. Sample Issues Reported
SAMPLE_ISSUES = [
    {
        "user_email": "staff@demo.edu",
        "resource_name": "Computer Lab 2",
        "title": "Wi-Fi access point not assigning IP addresses",
        "category": "Internet/Wi-Fi",
        "priority": "high",
        "status": "in_progress",
        "description": "Systems at row 3 and 4 are unable to connect to campus network.",
        "admin_response": "Campus network team has been notified to reset switch port.",
    },
    {
        "user_email": "student@demo.edu",
        "resource_name": "Classroom (digital) 1",
        "title": "Left audio speaker has crackling noise",
        "category": "Projector/AV",
        "priority": "medium",
        "status": "open",
        "description": "Crackling sound during presentation audio playback.",
        "admin_response": "",
    },
]

# 7. Sample Initial Notifications
SAMPLE_NOTIFICATIONS = [
    {
        "user_email": "student@demo.edu",
        "title": "Welcome to Smart Campus Jabin!",
        "message": "You can explore facilities, check availability, and report any maintenance issues.",
    },
    {
        "user_email": "staff@demo.edu",
        "title": "Booking Approved",
        "message": "Your booking for Seminar Hall on tomorrow 10:00 AM - 12:00 PM has been approved.",
    },
    {
        "user_email": "admin@demo.edu",
        "title": "New Booking Request",
        "message": "A new pending booking for Computer Lab 1 requires your review.",
    },
]
