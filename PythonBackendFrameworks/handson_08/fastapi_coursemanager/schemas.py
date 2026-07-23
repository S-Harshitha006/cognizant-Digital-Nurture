from typing import Optional, List
from pydantic import BaseModel


# =====================================================
# DEPARTMENT
# =====================================================

class DepartmentBase(BaseModel):
    name: str
    code: str


class DepartmentResponse(DepartmentBase):
    id: int

    class Config:
        from_attributes = True


# =====================================================
# COURSE
# =====================================================

class CourseBase(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int


class CourseCreate(CourseBase):
    pass


# Used for PATCH
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


# =====================================================
# PAGINATION
# =====================================================

class CoursePagination(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[CourseResponse]


# =====================================================
# STUDENT
# =====================================================

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


# =====================================================
# ENROLLMENT
# =====================================================

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


# =====================================================
# STANDARD ERROR RESPONSE
# =====================================================

class ErrorDetails(BaseModel):
    code: str
    message: str
    field: Optional[str] = None


class ErrorResponse(BaseModel):
    error: ErrorDetails