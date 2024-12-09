The problem SAM (Smart Attendance Manager) solves
Current attendance systems are inefficient, prone to errors, and vulnerable to proxy attendance.
Manual attendance tracking is slow and error-prone
They depend on costly, specialized hardware and often require internet access, limiting flexibility and functionality.
Proxy attendance compromises accuracy.

Solution:
SAM software uses facial recognition to ensure real-time attendance marking.
It creates a local Wi-Fi network to connect devices (e.g., mobile phones), which act as the hardware for capturing student faces, verifying their presence, and preventing proxies.
Automates attendance, reducing time and errors.
Prevents proxy attendance.
No dedicated hardware needed, any mobile phone can be used.
Lowers costs by utilizing existing devices.
Operates without internet via a local Wi-Fi network.

Challenges we ran into
Problem: Synchronizing attendance data across different locations or devices in real-time can be challenging, especially if connectivity is inconsistent.
Also Data Synchronization was a problem
Solution: Use robust data synchronization techniques and ensure offline capabilities where possible
cmd for install and run

Npm insatll for node moudule
npm run dev
python api.py DB :- mysql -h 127.0.0.1 -P 3306 -u root -p student_records Jatin@123 cd sam npm run dev

db configraution

db_config = { 'user': 'root', 'password': 'Jatin@123', 'host': '127.0.0.1', 'port': 3306, 'database': 'student_records' }

select * from student ; show tables ; select id, name, rool_number, course, year, section, image_path

