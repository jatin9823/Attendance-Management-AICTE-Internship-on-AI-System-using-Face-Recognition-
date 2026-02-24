# 🚀 SAM (Smart Attendance Manager)

🔗 **Project Portfolio:**
https://professional-journey.netlify.app/virtual-internship-3

------------------------------------------------------------------------

## 📌 Overview

**SAM (Smart Attendance Manager)** is an AI-powered attendance
management system designed to eliminate proxy attendance, reduce manual
errors, and automate classroom attendance processes.

Developed during **TechSaksham (Microsoft & SAP Collaboration) -- AI
Transformative Learning Internship (Nov 2024 -- Dec 2024)**.

SAM leverages **Facial Recognition, Geolocation APIs, and Local Network
Communication** to provide a secure, cost-effective, and
hardware-independent attendance system.

------------------------------------------------------------------------

## ❌ Problem Statement

Current attendance systems face multiple issues:

-   Manual attendance tracking is slow and error-prone\
-   Proxy attendance compromises data accuracy\
-   Systems depend on costly specialized hardware\
-   Internet dependency limits flexibility\
-   Synchronizing attendance data across devices is difficult\
-   Data synchronization challenges in inconsistent connectivity

------------------------------------------------------------------------

## ✅ Solution

SAM provides an intelligent and scalable solution:

-   Facial Recognition for real-time attendance marking\
-   Local Wi-Fi network creation for offline operation\
-   Mobile phones act as capture devices (no dedicated hardware
    required)\
-   Geolocation validation to ensure student presence\
-   Automated attendance recording\
-   Real-time verification and anti-proxy mechanism\
-   Cost-effective implementation using existing devices

------------------------------------------------------------------------

## 🎯 Key Features

-   98% Facial Recognition Accuracy\
-   Real-time attendance validation\
-   Geolocation-based authentication\
-   Admin dashboard with reporting system\
-   MySQL database integration\
-   Offline capability via local Wi-Fi\
-   Secure authentication system

------------------------------------------------------------------------

## 🛠 Tech Stack

**Frontend** - Node.js\
- HTML / CSS / JavaScript

**Backend** - Python\
- OpenCV\
- Face Recognition Libraries\
- Geolocation APIs

**Database** - MySQL

------------------------------------------------------------------------

## 🧠 Challenges Faced

### Problem:

Synchronizing attendance data across different devices and locations in
real-time, especially with inconsistent connectivity.

### Solution:

-   Implemented robust data synchronization mechanisms\
-   Designed offline-first architecture\
-   Optimized local data storage and syncing logic

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### 1️⃣ Install Node Modules

``` bash
npm install
```

### 2️⃣ Run Frontend

``` bash
npm run dev
```

### 3️⃣ Run Backend API

``` bash
python api.py
```

------------------------------------------------------------------------

## 🗄 Database Setup

### MySQL Login

``` bash
mysql -h 127.0.0.1 -P 3306 -u root -p student_records
```

Password: Jatin@123

------------------------------------------------------------------------

### Database Configuration (Python)

``` python
db_config = {
    'user': 'root',
    'password': 'Jatin@123',
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'student_records'
}
```

------------------------------------------------------------------------

### Useful SQL Commands

``` sql
SHOW TABLES;
SELECT * FROM student;
SELECT id, name, roll_number, course, year, section, image_path FROM student;
```

------------------------------------------------------------------------

## 📊 Internship Details

**Organization:** TechSaksham (Microsoft & SAP Collaboration)\
**Role:** AI Transformative Learning Intern\
**Duration:** Nov 2024 -- Dec 2024\
**Mode:** Remote

### Achievements:

-   Built AI-powered Attendance System\
-   Achieved 98% recognition accuracy\
-   Implemented facial recognition authentication\
-   Integrated real-time location validation\
-   Developed admin dashboard with automated reports

------------------------------------------------------------------------

## 👨‍💻 Author

**Jatin Gupta**\
MCA Student \| Full Stack Developer \| AI & Open Source Enthusiast

🔗 GitHub: https://github.com/jatin009v\
🔗 LinkedIn: https://linkedin.com/in/jatingupta09\
🌐 Portfolio:
https://professional-journey.netlify.app/virtual-internship-3

------------------------------------------------------------------------

## 🤝 Open Source Contribution

This project is open for contributions.\
Feel free to fork, improve, and submit pull requests.

If you found this useful, consider giving it a ⭐ on GitHub.

------------------------------------------------------------------------

## 📜 License

This project is developed for educational and internship purposes.
