from typing import Optional

from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    BackgroundTasks,
    status,
    Response,
)

from sqlalchemy.ext.asyncio import AsyncSession

import crud
import schemas

from database import Base, engine, get_db


app = FastAPI(
    title="Course Management API",
    description="FastAPI application for managing departments, courses, students and enrollments.",
    version="2.0",
    contact={
        "name": "Cognizant Digital Nurture",
        "email": "support@example.com",
    },
)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def root():
    return {"message": "Course Management API Running"}


# =====================================================
# COURSE ENDPOINTS
# =====================================================

@app.get(
    "/api/courses/",
    tags=["Courses"],
    response_model=list[schemas.CourseResponse],
)
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db),
):
    return await crud.get_courses(
        db,
        skip,
        limit,
        department_id,
    )


@app.get(
    "/api/courses/{course_id}",
    tags=["Courses"],
    response_model=schemas.CourseResponse,
)
async def get_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):

    course = await crud.get_course(
        db,
        course_id,
    )

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found",
        )

    return course


@app.post(
    "/api/courses/",
    tags=["Courses"],
    response_model=schemas.CourseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create Course",
    response_description="Course created successfully",
)
async def create_course(
    course: schemas.CourseCreate,
    db: AsyncSession = Depends(get_db),
):

    return await crud.create_course(
        db,
        course,
    )


@app.put(
    "/api/courses/{course_id}",
    tags=["Courses"],
    response_model=schemas.CourseResponse,
)
async def update_course(
    course_id: int,
    course: schemas.CourseUpdate,
    db: AsyncSession = Depends(get_db),
):

    db_course = await crud.update_course(
        db,
        course_id,
        course,
    )

    if db_course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found",
        )

    return db_course


@app.delete(
    "/api/courses/{course_id}",
    tags=["Courses"],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):

    course = await crud.delete_course(
        db,
        course_id,
    )

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found",
        )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )

# =====================================================
# STUDENTS ENROLLED IN A COURSE (JOIN)
# =====================================================

@app.get(
    "/api/courses/{course_id}/students",
    tags=["Courses"],
    response_model=list[schemas.StudentResponse],
)
async def get_students_by_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):

    return await crud.get_students_by_course(
        db,
        course_id,
    )


# =====================================================
# STUDENT ENDPOINTS
# =====================================================

@app.get(
    "/api/students/",
    tags=["Students"],
    response_model=list[schemas.StudentResponse],
)
async def get_students(
    db: AsyncSession = Depends(get_db),
):

    return await crud.get_students(db)


@app.post(
    "/api/students/",
    tags=["Students"],
    response_model=schemas.StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_student(
    student: schemas.StudentCreate,
    db: AsyncSession = Depends(get_db),
):

    return await crud.create_student(
        db,
        student,
    )


@app.put(
    "/api/students/{student_id}",
    tags=["Students"],
    response_model=schemas.StudentResponse,
)
async def update_student(
    student_id: int,
    student: schemas.StudentUpdate,
    db: AsyncSession = Depends(get_db),
):

    db_student = await crud.update_student(
        db,
        student_id,
        student,
    )

    if db_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return db_student


@app.delete(
    "/api/students/{student_id}",
    tags=["Students"],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_student(
    student_id: int,
    db: AsyncSession = Depends(get_db),
):

    db_student = await crud.delete_student(
        db,
        student_id,
    )

    if db_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )


# =====================================================
# BACKGROUND TASK
# =====================================================

def send_confirmation_email(student_email: str):
    print(f"Sending confirmation to {student_email}")


# =====================================================
# ENROLLMENT ENDPOINTS
# =====================================================

@app.get(
    "/api/enrollments/",
    tags=["Enrollments"],
    response_model=list[schemas.EnrollmentResponse],
)
async def get_enrollments(
    db: AsyncSession = Depends(get_db),
):

    return await crud.get_enrollments(db)


@app.post(
    "/api/enrollments/",
    tags=["Enrollments"],
    response_model=schemas.EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_enrollment(
    enrollment: schemas.EnrollmentCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
):

    db_enrollment = await crud.create_enrollment(
        db,
        enrollment,
    )

    student = await crud.get_student(
        db,
        enrollment.student_id,
    )

    if student:
        background_tasks.add_task(
            send_confirmation_email,
            student.email,
        )

    return db_enrollment


@app.delete(
    "/api/enrollments/{enrollment_id}",
    tags=["Enrollments"],
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_enrollment(
    enrollment_id: int,
    db: AsyncSession = Depends(get_db),
):

    enrollment = await crud.delete_enrollment(
        db,
        enrollment_id,
    )

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found",
        )

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )