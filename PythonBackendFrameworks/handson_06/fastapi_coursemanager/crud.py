from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

import models
import schemas


async def get_courses(
    db: AsyncSession,
    skip: int = 0,
    limit: int = 10,
    department_id: int | None = None
):

    query = select(models.Course)

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
        select(models.Course).where(
            models.Course.id == course_id
        )
    )

    return result.scalar_one_or_none()


async def create_course(
    db: AsyncSession,
    course: schemas.CourseCreate
):

    db_course = models.Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )

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

    if course.name is not None:
        db_course.name = course.name

    if course.code is not None:
        db_course.code = course.code

    if course.credits is not None:
        db_course.credits = course.credits

    if course.department_id is not None:
        db_course.department_id = course.department_id

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