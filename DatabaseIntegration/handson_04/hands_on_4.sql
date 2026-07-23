USE college_db;

-- Query Optimization
-- Baseline Performance

EXPLAIN FORMAT=JSON
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
    ON s.student_id = e.student_id
JOIN courses c
    ON c.course_id = e.course_id
WHERE s.enrollment_year = 2022;

-- Remove duplicate enrollment records

SELECT
    enrollment_id,
    student_id,
    course_id
FROM enrollments
WHERE student_id = 3
AND course_id = 2;

DELETE FROM enrollments
WHERE enrollment_id IN (16,17,20);

DROP INDEX idx_students_enrollment_year ON students;

DROP INDEX idx_course_code ON courses;

DROP INDEX idx_enrollment_grade ON enrollments;

DROP INDEX idx_enrollment_student_course ON enrollments;

-- Create Indexes

CREATE INDEX idx_students_enrollment_year
ON students(enrollment_year);

CREATE UNIQUE INDEX idx_enrollment_student_course
ON enrollments(student_id,course_id);

CREATE INDEX idx_course_code
ON courses(course_code);

CREATE INDEX idx_enrollment_grade
ON enrollments(grade);

-- Compare Query Plan

EXPLAIN FORMAT=JSON
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
    ON s.student_id=e.student_id
JOIN courses c
    ON c.course_id=e.course_id
WHERE s.enrollment_year=2022;

-- Verify Indexes

SHOW INDEX FROM students;

SHOW INDEX FROM enrollments;

SHOW INDEX FROM courses;
