
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.orm import declarative_base, relationship

# Change username and password if required
engine = create_engine(
    "mysql+mysqlconnector://root:password@localhost/college_db_orm",
    echo=True
)

Base = declarative_base()


class Department(Base):
    __tablename__ = "departments"

    dept_id = Column(Integer, primary_key=True)
    dept_name = Column(String(100), nullable=False)

    students = relationship("Student", back_populates="department")


class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    enrollment_year = Column(Integer)

    dept_id = Column(Integer, ForeignKey("departments.dept_id"))

    department = relationship("Department", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")


class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(100))
    credits = Column(Integer)

    enrollments = relationship("Enrollment", back_populates="course")


class Professor(Base):
    __tablename__ = "professors"

    professor_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(100))


class Enrollment(Base):
    __tablename__ = "enrollments"

    enrollment_id = Column(Integer, primary_key=True)

    student_id = Column(Integer, ForeignKey("students.student_id"))
    course_id = Column(Integer, ForeignKey("courses.course_id"))

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("All tables created successfully.")