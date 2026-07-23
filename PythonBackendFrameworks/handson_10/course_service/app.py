from flask import Flask, request, jsonify
from models import db, Course

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///course.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


# Home Route
@app.route("/")
def home():
    return {"message": "Course Service is running"}


# Get All Courses
@app.route("/api/courses", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return jsonify([course.to_dict() for course in courses])


# Get Course by ID
@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    course = Course.query.get(course_id)

    if not course:
        return jsonify({"message": "Course not found"}), 404

    return jsonify(course.to_dict())


# Add Course
@app.route("/api/courses", methods=["POST"])
def add_course():
    data = request.get_json()

    course = Course(
        name=data["name"],
        department=data["department"]
    )

    db.session.add(course)
    db.session.commit()

    return jsonify(course.to_dict()), 201


# Delete Course
@app.route("/api/courses/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    course = Course.query.get(course_id)

    if not course:
        return jsonify({"message": "Course not found"}), 404

    db.session.delete(course)
    db.session.commit()

    return jsonify({"message": "Course deleted"})


if __name__ == "__main__":
    app.run(port=5001, debug=True)