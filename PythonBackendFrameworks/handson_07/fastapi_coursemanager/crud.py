from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

import models
import schemas


# =====================================================
# COURSE CRUD
# =====================================================

async def get_courses(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 10,
    department_id: int | None = None
):

    query = select(models.Course).options(
        selectinload(models.Course.department)
    )

    if department_id is not None:
        query = query.where(
            models.Course.department_id == department_id
        )

    query = query.offset(skip).limit(limit)

    result = await db.execute(query)

    return result.scalars().all()


async def get_course(
    db: AsyncSession,
    course_id: int
):

    result = await db.execute(
        select(models.Course)
        .options(
            selectinload(models.Course.department)
        )
        .where(models.Course.id == course_id)
    )

    return result.scalar_one_or_none()


async def create_course(
    db: AsyncSession,
    course: schemas.CourseCreate
):

    db_course = models.Course(**course.model_dump())

    db.add(db_course)

    await db.commit()

    await db.refresh(db_course)

    return db_course


async def update_course(
    db: AsyncSession,
    course_id: int,
    course: schemas.CourseUpdate
):

    db_course = await get_course(
        db,
        course_id
    )

    if db_course is None:
        return None

    values = course.model_dump(
        exclude_unset=True
    )

    for key, value in values.items():
        setattr(db_course, key, value)

    await db.commit()

    await db.refresh(db_course)

    return db_course


async def delete_course(
    db: AsyncSession,
    course_id: int
):

    db_course = await get_course(
        db,
        course_id
    )

    if db_course is None:
        return None

    await db.delete(db_course)

    await db.commit()

    return db_course


# =====================================================
# STUDENT CRUD
# =====================================================

async def get_students(
    db: AsyncSession
):

    result = await db.execute(
        select(models.Student)
    )

    return result.scalars().all()


async def get_student(
    db: AsyncSession,
    student_id: int
):

    result = await db.execute(
        select(models.Student)
        .where(models.Student.id == student_id)
    )

    return result.scalar_one_or_none()


async def create_student(
    db: AsyncSession,
    student: schemas.StudentCreate
):

    db_student = models.Student(
        **student.model_dump()
    )

    db.add(db_student)

    await db.commit()

    await db.refresh(db_student)

    return db_student


async def update_student(
    db: AsyncSession,
    student_id: int,
    student: schemas.StudentUpdate
):

    db_student = await get_student(
        db,
        student_id
    )

    if db_student is None:
        return None

    values = student.model_dump(
        exclude_unset=True
    )

    for key, value in values.items():
        setattr(db_student, key, value)

    await db.commit()

    await db.refresh(db_student)

    return db_student


async def delete_student(
    db: AsyncSession,
    student_id: int
):

    db_student = await get_student(
        db,
        student_id
    )

    if db_student is None:
        return None

    await db.delete(db_student)

    await db.commit()

    return db_student

# =====================================================
# ENROLLMENT CRUD
# =====================================================

async def get_enrollments(
    db: AsyncSession
):

    result = await db.execute(
        select(models.Enrollment).options(
            selectinload(models.Enrollment.student),
            selectinload(models.Enrollment.course)
        )
    )

    return result.scalars().all()


async def get_enrollment(
    db: AsyncSession,
    enrollment_id: int
):

    result = await db.execute(
        select(models.Enrollment)
        .options(
            selectinload(models.Enrollment.student),
            selectinload(models.Enrollment.course)
        )
        .where(models.Enrollment.id == enrollment_id)
    )

    return result.scalar_one_or_none()


async def create_enrollment(
    db: AsyncSession,
    enrollment: schemas.EnrollmentCreate
):

    db_enrollment = models.Enrollment(
        **enrollment.model_dump()
    )

    db.add(db_enrollment)

    await db.commit()

    await db.refresh(db_enrollment)

    return db_enrollment


async def update_enrollment(
    db: AsyncSession,
    enrollment_id: int,
    enrollment: schemas.EnrollmentUpdate
):

    db_enrollment = await get_enrollment(
        db,
        enrollment_id
    )

    if db_enrollment is None:
        return None

    values = enrollment.model_dump(
        exclude_unset=True
    )

    for key, value in values.items():
        setattr(db_enrollment, key, value)

    await db.commit()

    await db.refresh(db_enrollment)

    return db_enrollment


async def delete_enrollment(
    db: AsyncSession,
    enrollment_id: int
):

    db_enrollment = await get_enrollment(
        db,
        enrollment_id
    )

    if db_enrollment is None:
        return None

    await db.delete(db_enrollment)

    await db.commit()

    return db_enrollment


# =====================================================
# JOIN QUERY
# GET STUDENTS ENROLLED IN A COURSE
# =====================================================

async def get_students_by_course(
    db: AsyncSession,
    course_id: int
):

    result = await db.execute(
        select(models.Student)
        .join(
            models.Enrollment,
            models.Student.id == models.Enrollment.student_id
        )
        .where(
            models.Enrollment.course_id == course_id
        )
    )

    return result.scalars().all()