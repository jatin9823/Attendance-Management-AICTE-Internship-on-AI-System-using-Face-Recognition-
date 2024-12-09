from flask import Flask, request, jsonify
import mysql.connector
import os
import numpy as np
import face_recognition
from flask_cors import CORS
from werkzeug.utils import secure_filename
import json

# Flask application setup
app = Flask(__name__)
CORS(app)

# Configuration
app.config['Image_db'] = 'Image_db'
app.config['UPLOAD_FOLDER'] = 'Uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload size

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Database configuration
db_config = {
    'user': 'root',
    'password': 'Jatin@123',
    'host': '127.0.0.1',
    'port': 3306,
    'database': 'student_records'
}

# Helper functions
def get_db_connection():
    """Establish and return a database connection."""
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None

def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Routes
@app.route('/api/enroll', methods=['POST'])
def enroll():
    """Enroll a new student with image and face encoding."""
    data = request.form
    name = data.get('name')
    roll_number = data.get('roll_number')
    course = data.get('course')
    year = data.get('year')
    section = data.get('section')

    if 'image' not in request.files or not allowed_file(request.files['image'].filename):
        return jsonify({'message': 'Invalid or missing image file!'}), 400

    file = request.files['image']
    file_extension = os.path.splitext(file.filename)[1]
    image_path = os.path.join(app.config['Image_db'], f"{roll_number}{file_extension}")
    file.save(image_path)

    known_image = face_recognition.load_image_file(image_path)
    face_encodings = face_recognition.face_encodings(known_image)

    if len(face_encodings) > 0:
        face_encoding = face_encodings[0]
        face_encoding_json = json.dumps(face_encoding.tolist())
    else:
        return jsonify({'message': 'No face detected in the uploaded image!'}), 400

    conn = get_db_connection()
    if not conn:
        return jsonify({'message': 'Database connection failed!'}), 500

    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO student (name, roll_number, course, year, section, image_path, face_encoding)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', (name, roll_number, course, year, section, image_path, face_encoding_json))
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return jsonify({'message': 'Failed to enroll student!'}), 500
    finally:
        cursor.close()
        conn.close()

    return jsonify({"message": "Enrollment successful!"}), 201


@app.route('/recognize', methods=['POST'])
def recognize():
    """Recognize a face from an uploaded image."""
    if 'image' not in request.files or not allowed_file(request.files['image'].filename):
        return jsonify({'message': 'Invalid or missing image file!'}), 400

    file = request.files['image']
    filename = secure_filename(file.filename)
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(image_path)

    unknown_image = face_recognition.load_image_file(image_path)
    unknown_encodings = face_recognition.face_encodings(unknown_image)

    if len(unknown_encodings) == 0:
        return jsonify({'message': 'No face detected in the uploaded image!'}), 400

    unknown_encoding = unknown_encodings[0]

    conn = get_db_connection()
    if not conn:
        return jsonify({'message': 'Database connection failed!'}), 500

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT name, face_encoding FROM student')
        students = cursor.fetchall()

        for student in students:
            face_encoding_json = student['face_encoding']
            known_encoding = np.array(json.loads(face_encoding_json))
            results = face_recognition.compare_faces([known_encoding], unknown_encoding)

            if results[0]:
                return jsonify({'message': f"Match found! Student: {student['name']}"}), 200
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return jsonify({'message': 'Failed to recognize face!'}), 500
    finally:
        cursor.close()
        conn.close()

    return jsonify({'message': 'No match found!'}), 200

# Main application entry point
if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['Image_db'], exist_ok=True)
    app.run(debug=True)
