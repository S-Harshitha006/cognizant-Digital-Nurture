from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func, or_

import models
import schemas


# =====================================================
# COURSE CRUD
# =====================================================

async def get_courses(
    db: AsyncSession,
    page: int = 1,
    page_size: int = 5,
    search: str | None = None
):
    query = select(models.Course)

    if search:
        query = query.where(
            or_(
                models.Course.name.ilike(f"%{search}%"),
                models.Course.code.ilike(f"%{search}%")
            )
        )

    total = await db.execute(
        select(func.count()).select_from(query.subquery())
    )

    count = total.scalar()

    result = await db.execute(
        query.offset((page - 1) * page_size).limit(page_size)
    )

    courses = result.scalars().all()

    return {
        "count": count,
        "results": courses
    }


async def get_course(db: AsyncSession, course_id: int):
    result = await db.execute(
        select(models.Course).where(
            models.Course.id == course_id
        )
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
    course: schemas.CourseCreate
):
    db_course = await get_course(db, course_id)

    if not db_course:
        return None

    data = course.model_dump()

    for key, value in data.items():
        setattr(db_course, key, value)

    await db.commit()
    await db.refresh(db_course)

    return db_course


async def patch_course(
    db: AsyncSession,
    course_id: int,
    course: schemas.CourseUpdate
):
    db_course = await get_course(db, course_id)

    if not db_course:
        return None

    updates = course.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(db_course, key, value)

    await db.commit()
    await db.refresh(db_course)

    return db_course

# =====================================================
# DELETE COURSE
# =====================================================

async def delete_course(db: AsyncSession, course_id: int):
    db_course = await get_course(db, course_id)

    if not db_course:
        return None

    await db.delete(db_course)
    await db.commit()

    return db_course


# =====================================================
# STUDENT CRUD
# =====================================================

async def get_students(db: AsyncSession):
    result = await db.execute(
        select(models.Student)
    )
    return result.scalars().all()


async def get_student(db: AsyncSession, student_id: int):
    result = await db.execute(
        select(models.Student).where(
            models.Student.id == student_id
        )
    )
    return result.scalar_one_or_none()


async def create_student(
    db: AsyncSession,
    student: schemas.StudentCreate
):
    db_student = models.Student(**student.model_dump())

    db.add(db_student)

    await db.commit()
    await db.refresh(db_student)

    return db_student


async def update_student(
    db: AsyncSession,
    student_id: int,
    student: schemas.StudentCreate
):
    db_student = await get_student(db, student_id)

    if not db_student:
        return None

    data = student.model_dump()

    for key, value in data.items():
        setattr(db_student, key, value)

    await db.commit()
    await db.refresh(db_student)

    return db_student


async def patch_student(
    db: AsyncSession,
    student_id: int,
    student: schemas.StudentUpdate
):
    db_student = await get_student(db, student_id)

    if not db_student:
        return None

    updates = student.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(db_student, key, value)

    await db.commit()
    await db.refresh(db_student)

    return db_student


async def delete_student(
    db: AsyncSession,
    student_id: int
):
    db_student = await get_student(db, student_id)

    if not db_student:
        return None

    await db.delete(db_student)
    await db.commit()

    return db_student


# =====================================================
# ENROLLMENT CRUD
# =====================================================

async def get_enrollments(db: AsyncSession):
    result = await db.execute(
        select(models.Enrollment)
    )
    return result.scalars().all()


async def get_enrollment(
    db: AsyncSession,
    enrollment_id: int
):
    result = await db.execute(
        select(models.Enrollment).where(
            models.Enrollment.id == enrollment_id
        )
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
    enrollment: schemas.EnrollmentCreate
):
    db_enrollment = await get_enrollment(db, enrollment_id)

    if not db_enrollment:
        return None

    data = enrollment.model_dump()

    for key, value in data.items():
        setattr(db_enrollment, key, value)

    await db.commit()
    await db.refresh(db_enrollment)

    return db_enrollment


async def patch_enrollment(
    db: AsyncSession,
    enrollment_id: int,
    enrollment: schemas.EnrollmentUpdate
):
    db_enrollment = await get_enrollment(db, enrollment_id)

    if not db_enrollment:
        return None

    updates = enrollment.model_dump(exclude_unset=True)

    for key, value in updates.items():
        setattr(db_enrollment, key, value)

    await db.commit()
    await db.refresh(db_enrollment)

    return db_enrollment


async def delete_enrollment(
    db: AsyncSession,
    enrollment_id: int
):
    db_enrollment = await get_enrollment(db, enrollment_id)

    if not db_enrollment:
        return None

    await db.delete(db_enrollment)
    await db.commit()

    return db_enrollment


# =====================================================
# JOIN QUERY
# =====================================================

async def get_students_by_course(
    db: AsyncSession,
    course_id: int
):
    result = await db.execute(
        select(models.Student)
        .join(models.Enrollment)
        .where(models.Enrollment.course_id == course_id)
    )

    return result.scalars().all()