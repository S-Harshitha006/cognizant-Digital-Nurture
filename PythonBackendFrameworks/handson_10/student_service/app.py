from flask import Flask, request, jsonify
from models import db, Student
import requests

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///student.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return {"message": "Student Service is running"}


# Get all students
@app.route("/api/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    return jsonify([student.to_dict() for student in students])


# Add student
@app.route("/api/students", methods=["POST"])
def add_student():
    data = request.get_json()

    student = Student(
        name=data["name"],
        email=data["email"]
    )

    db.session.add(student)
    db.session.commit()

    return jsonify(student.to_dict()), 201


# Enroll Student
@app.route("/api/students/<int:student_id>/enroll", methods=["POST"])
def enroll(student_id):

    student = Student.query.get(student_id)

    if not student:
        return jsonify({"message": "Student not found"}), 404

    data = request.get_json()
    course_id = data["course_id"]

    try:
        response = requests.get(
            f"http://localhost:5001/api/courses/{course_id}"
        )

        if response.status_code != 200:
            return jsonify({"message": "Course not found"}), 404

    except requests.exceptions.ConnectionError:
        return jsonify({
            "message": "Course Service unavailable"
        }), 503

    student.enrolled_course = course_id
    db.session.commit()

    return jsonify({
        "message": "Enrollment Successful",
        "student": student.to_dict()
    })


if __name__ == "__main__":
    app.run(port=5002, debug=True)