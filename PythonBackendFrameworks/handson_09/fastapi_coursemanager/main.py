from typing import Optional

from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    BackgroundTasks,
    Response,
    status
)

from sqlalchemy.ext.asyncio import AsyncSession

import crud
import models
import schemas

from database import engine, get_db
from datetime import timedelta

from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt

from security import (
    create_access_token,
    oauth2_scheme,
    SECRET_KEY,
    ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES
)


# =====================================================
# FASTAPI APP
# =====================================================

app = FastAPI(
    title="Course Management API",
    description="RESTful API for managing Departments, Courses, Students and Enrollments",
    version="1.0.0",
    contact={
        "name": "Course Manager",
        "email": "admin@example.com"
    }
)

# =====================================================
# CORS CONFIGURATION
# =====================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =====================================================
# CREATE TABLES
# =====================================================

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


# =====================================================
# ROOT
# =====================================================

@app.get("/")
async def root():
    return {
        "message": "Course Management API Running"
    }


# =====================================================
# BACKGROUND TASK
# =====================================================

def send_confirmation_email(student_id: int):
    print(f"Confirmation email sent to student {student_id}")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db)
):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        email = payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = await crud.get_user_by_email(
        db,
        email
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user    
 
# =====================================================
# COURSE APIs (Version 1)
# =====================================================

@app.get(
    "/api/v1/courses",
    response_model=schemas.CoursePagination,
    tags=["Courses"]
)
async def read_courses(
    page: int = 1,
    page_size: int = 5,
    search: Optional[str] = None,
    db: AsyncSession = Depends(get_db)
):
    result = await crud.get_courses(
        db,
        page,
        page_size,
        search
    )

    count = result["count"]

    next_link = None
    previous_link = None

    if page * page_size < count:
        next_link = (
            f"/api/v1/courses?page={page + 1}&page_size={page_size}"
        )

    if page > 1:
        previous_link = (
            f"/api/v1/courses?page={page - 1}&page_size={page_size}"
        )

    return {
        "count": count,
        "next": next_link,
        "previous": previous_link,
        "results": result["results"]
    }


@app.get(
    "/api/v1/courses/{course_id}",
    response_model=schemas.CourseResponse,
    tags=["Courses"]
)
async def read_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):
    course = await crud.get_course(db, course_id)

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


@app.post(
    "/api/v1/courses",
    response_model=schemas.CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"]
)
async def create_course(
    course: schemas.CourseCreate,
    response: Response,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    db_course = await crud.create_course(db, course)

    response.headers["Location"] = (
        f"/api/v1/courses/{db_course.id}"
    )

    return db_course

# =====================================================
# UPDATE COURSE
# =====================================================

@app.put(
    "/api/v1/courses/{course_id}",
    response_model=schemas.CourseResponse,
    tags=["Courses"]
)
async def update_course(
    course_id: int,
    course: schemas.CourseCreate,
    db: AsyncSession = Depends(get_db)
):
    updated = await crud.update_course(
        db,
        course_id,
        course
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return updated


# =====================================================
# PATCH COURSE
# =====================================================

@app.patch(
    "/api/v1/courses/{course_id}",
    response_model=schemas.CourseResponse,
    tags=["Courses"]
)
async def patch_course(
    course_id: int,
    course: schemas.CourseUpdate,
    db: AsyncSession = Depends(get_db)
):
    updated = await crud.patch_course(
        db,
        course_id,
        course
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return updated


# =====================================================
# DELETE COURSE
# =====================================================

@app.delete(
    "/api/v1/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Courses"]
)
async def delete_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    deleted = await crud.delete_course(
        db,
        course_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)


# =====================================================
# STUDENT APIs
# =====================================================

@app.get(
    "/api/v1/students",
    response_model=list[schemas.StudentResponse],
    tags=["Students"]
)
async def read_students(
    db: AsyncSession = Depends(get_db)
):
    return await crud.get_students(db)


@app.get(
    "/api/v1/students/{student_id}",
    response_model=schemas.StudentResponse,
    tags=["Students"]
)
async def read_student(
    student_id: int,
    db: AsyncSession = Depends(get_db)
):
    student = await crud.get_student(
        db,
        student_id
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@app.post(
    "/api/v1/students",
    response_model=schemas.StudentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Students"]
)
async def create_student(
    student: schemas.StudentCreate,
    response: Response,
    db: AsyncSession = Depends(get_db)
):
    db_student = await crud.create_student(
        db,
        student
    )

    response.headers["Location"] = (
        f"/api/v1/students/{db_student.id}"
    )

    return db_student


@app.put(
    "/api/v1/students/{student_id}",
    response_model=schemas.StudentResponse,
    tags=["Students"]
)
async def update_student(
    student_id: int,
    student: schemas.StudentCreate,
    db: AsyncSession = Depends(get_db)
):
    updated = await crud.update_student(
        db,
        student_id,
        student
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return updated


@app.patch(
    "/api/v1/students/{student_id}",
    response_model=schemas.StudentResponse,
    tags=["Students"]
)
async def patch_student(
    student_id: int,
    student: schemas.StudentUpdate,
    db: AsyncSession = Depends(get_db)
):
    updated = await crud.patch_student(
        db,
        student_id,
        student
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return updated


@app.delete(
    "/api/v1/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Students"]
)
async def delete_student(
    student_id: int,
    db: AsyncSession = Depends(get_db)
):
    deleted = await crud.delete_student(
        db,
        student_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)

# =====================================================
# ENROLLMENT APIs
# =====================================================

@app.get(
    "/api/v1/enrollments",
    response_model=list[schemas.EnrollmentResponse],
    tags=["Enrollments"]
)
async def read_enrollments(
    db: AsyncSession = Depends(get_db)
):
    return await crud.get_enrollments(db)


@app.get(
    "/api/v1/enrollments/{enrollment_id}",
    response_model=schemas.EnrollmentResponse,
    tags=["Enrollments"]
)
async def read_enrollment(
    enrollment_id: int,
    db: AsyncSession = Depends(get_db)
):
    enrollment = await crud.get_enrollment(db, enrollment_id)

    if not enrollment:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return enrollment


@app.post(
    "/api/v1/enrollments",
    response_model=schemas.EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Enrollments"]
)
async def create_enrollment(
    enrollment: schemas.EnrollmentCreate,
    response: Response,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db)
):
    db_enrollment = await crud.create_enrollment(
        db,
        enrollment
    )

    background_tasks.add_task(
        send_confirmation_email,
        enrollment.student_id
    )

    response.headers["Location"] = (
        f"/api/v1/enrollments/{db_enrollment.id}"
    )

    return db_enrollment


@app.put(
    "/api/v1/enrollments/{enrollment_id}",
    response_model=schemas.EnrollmentResponse,
    tags=["Enrollments"]
)
async def update_enrollment(
    enrollment_id: int,
    enrollment: schemas.EnrollmentCreate,
    db: AsyncSession = Depends(get_db)
):
    updated = await crud.update_enrollment(
        db,
        enrollment_id,
        enrollment
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return updated


@app.patch(
    "/api/v1/enrollments/{enrollment_id}",
    response_model=schemas.EnrollmentResponse,
    tags=["Enrollments"]
)
async def patch_enrollment(
    enrollment_id: int,
    enrollment: schemas.EnrollmentUpdate,
    db: AsyncSession = Depends(get_db)
):
    updated = await crud.patch_enrollment(
        db,
        enrollment_id,
        enrollment
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return updated


@app.delete(
    "/api/v1/enrollments/{enrollment_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Enrollments"]
)
async def delete_enrollment(
    enrollment_id: int,
    db: AsyncSession = Depends(get_db)
):
    deleted = await crud.delete_enrollment(
        db,
        enrollment_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)


# =====================================================
# JOIN API
# =====================================================

@app.get(
    "/api/v1/courses/{course_id}/students",
    response_model=list[schemas.StudentResponse],
    tags=["Courses"]
)
async def students_in_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await crud.get_students_by_course(
        db,
        course_id
    )


# =====================================================
# AUTHENTICATION
# =====================================================

@app.post(
    "/api/v1/auth/register",
    response_model=schemas.UserResponse,
    status_code=201,
    tags=["Authentication"]
)
async def register(
    user: schemas.UserCreate,
    db: AsyncSession = Depends(get_db)
):
    existing = await crud.get_user_by_email(
        db,
        user.email
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Email already registered"
        )

    return await crud.create_user(
        db,
        user
    )


@app.post(
    "/api/v1/auth/login",
    response_model=schemas.Token,
    tags=["Authentication"]
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):
    user = await crud.authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect email or password"
        )

    access_token = create_access_token(
        data={"sub": user.email},
        expires_delta=timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }