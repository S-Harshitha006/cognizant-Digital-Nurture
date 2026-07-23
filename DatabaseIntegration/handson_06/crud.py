"""
N+1 Query Observation:
- Normal query issues multiple SQL statements.
- joinedload() fetches Student and Course together,
  reducing SQL queries to a single JOIN query.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload

from models import Department, Student, Course, Enrollment

engine = create_engine(
    "mysql+mysqlconnector://root:harshitha%402006@localhost/college_db_orm",
    echo=True
)

Session = sessionmaker(bind=engine)
session = Session()

# INSERT Departments
cs = Department(dept_name="Computer Science")
it = Department(dept_name="Information Technology")
ece = Department(dept_name="Electronics")

session.add_all([cs, it, ece])
session.commit()

# INSERT Students
students = [
    Student(name="Harshitha", email="harshitha@gmail.com", enrollment_year=2023, department=cs),
    Student(name="Anu", email="anu@gmail.com", enrollment_year=2022, department=cs),
    Student(name="Rahul", email="rahul@gmail.com", enrollment_year=2021, department=it),
    Student(name="Priya", email="priya@gmail.com", enrollment_year=2022, department=ece),
    Student(name="Kavin", email="kavin@gmail.com", enrollment_year=2023, department=cs),
]

session.add_all(students)
session.commit()

# INSERT Courses
courses = [
    Course(course_name="Database Systems", credits=4),
    Course(course_name="Python Programming", credits=3),
    Course(course_name="Machine Learning", credits=4),
]

session.add_all(courses)
session.commit()

# INSERT Enrollments
enrollments = [
    Enrollment(student=students[0], course=courses[0]),
    Enrollment(student=students[1], course=courses[1]),
    Enrollment(student=students[2], course=courses[2]),
    Enrollment(student=students[3], course=courses[0]),
]

session.add_all(enrollments)
session.commit()

# READ
print("\nStudents in Computer Science:\n")

result = (
    session.query(Student)
    .join(Department)
    .filter(Department.dept_name == "Computer Science")
)

for s in result:
    print(s.name)

# READ Enrollments
print("\nEnrollment Details:\n")

records = session.query(Enrollment).all()

for e in records:
    print(e.student.name, "->", e.course.course_name)

# UPDATE
student = session.query(Student).filter_by(
    email="harshitha@gmail.com"
).first()

if student:
    student.enrollment_year = 2024

session.commit()

# DELETE
record = session.query(Enrollment).first()

if record:
    session.delete(record)

session.commit()

# joinedload()
print("\nUsing joinedload()\n")

records = (
    session.query(Enrollment)
    .options(
        joinedload(Enrollment.student),
        joinedload(Enrollment.course)
    )
    .all()
)

for r in records:
    print(r.student.name, "-", r.course.course_name)

session.close()