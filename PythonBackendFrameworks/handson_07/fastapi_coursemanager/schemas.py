from pydantic import BaseModel
from typing import Optional


# ==========================
# Department Schemas
# ==========================

class DepartmentBase(BaseModel):
    name: str
    code: str


class DepartmentResponse(DepartmentBase):
    id: int

    class Config:
        from_attributes = True


# ==========================
# Course Schemas
# ==========================

class CourseBase(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None


class CourseResponse(CourseBase):
    id: int
    department: Optional[DepartmentResponse] = None

    class Config:
        from_attributes = True


# ==========================
# Student Schemas
# ==========================

class StudentBase(BaseModel):
    name: str
    email: str


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None


class StudentResponse(StudentBase):
    id: int

    class Config:
        from_attributes = True


# ==========================
# Enrollment Schemas
# ==========================

class EnrollmentBase(BaseModel):
    student_id: int
    course_id: int


class EnrollmentCreate(EnrollmentBase):
    pass


class EnrollmentUpdate(BaseModel):
    student_id: Optional[int] = None
    course_id: Optional[int] = None


class EnrollmentResponse(EnrollmentBase):
    id: int
    student: Optional[StudentResponse] = None
    course: Optional[CourseResponse] = None

    class Config:
        from_attributes = True