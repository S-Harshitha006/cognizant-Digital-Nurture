USE college_db;

-- ============================================
-- Hands-On 3
-- Task 1 : Subqueries
-- ============================================

-- Question 35
-- Students enrolled in more courses than the average

SELECT
    s.student_id,
    s.first_name,
    s.last_name,
    COUNT(e.course_id) AS total_courses
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(e.course_id) >
(
    SELECT AVG(course_count)
    FROM
    (
        SELECT COUNT(*) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) AS avg_table
);

-- ============================================

-- Question 36
-- Courses where every enrolled student scored A

SELECT
    c.course_name,
    c.course_code
FROM courses c
WHERE NOT EXISTS
(
    SELECT *
    FROM enrollments e
    WHERE e.course_id = c.course_id
    AND e.grade <> 'A'
);

-- ============================================

-- Question 37
-- Highest paid professor in each department

SELECT
    p.prof_name,
    p.salary,
    d.dept_name
FROM professors p
JOIN departments d
ON p.department_id = d.department_id
WHERE salary =
(
    SELECT MAX(salary)
    FROM professors p2
    WHERE p2.department_id = p.department_id
);

-- ============================================

-- Question 38
-- Departments with average professor salary
-- greater than 85000

SELECT *
FROM
(
    SELECT
        d.dept_name,
        AVG(p.salary) AS average_salary
    FROM departments d
    JOIN professors p
    ON d.department_id = p.department_id
    GROUP BY d.dept_name
) AS dept_salary
WHERE average_salary > 85000;

-- ============================================
-- Task 2 : Creating and Using Views
-- ============================================

-- Remove old views if they already exist

DROP VIEW IF EXISTS vw_course_stats;
DROP VIEW IF EXISTS vw_student_enrollment_summary;

-- ============================================
-- Question 39
-- Student Enrollment Summary View

CREATE VIEW vw_student_enrollment_summary AS
SELECT
    s.student_id,
    CONCAT(s.first_name,' ',s.last_name) AS student_name,
    d.dept_name,
    COUNT(e.course_id) AS total_courses,
    ROUND(
        AVG(
            CASE
                WHEN e.grade='A' THEN 4
                WHEN e.grade='B' THEN 3
                WHEN e.grade='C' THEN 2
                WHEN e.grade='D' THEN 1
                WHEN e.grade='F' THEN 0
                ELSE NULL
            END
        ),2
    ) AS gpa
FROM students s
JOIN departments d
ON s.department_id = d.department_id
LEFT JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY
s.student_id,
s.first_name,
s.last_name,
d.dept_name;

-- ============================================
-- Question 40
-- Course Statistics View

CREATE VIEW vw_course_stats AS
SELECT
    c.course_name,
    c.course_code,
    COUNT(e.student_id) AS total_enrollments,
    ROUND(
        AVG(
            CASE
                WHEN e.grade='A' THEN 4
                WHEN e.grade='B' THEN 3
                WHEN e.grade='C' THEN 2
                WHEN e.grade='D' THEN 1
                WHEN e.grade='F' THEN 0
                ELSE NULL
            END
        ),2
    ) AS avg_gpa
FROM courses c
LEFT JOIN enrollments e
ON c.course_id = e.course_id
GROUP BY
c.course_name,
c.course_code;

-- ============================================
-- Question 41
-- Students with GPA greater than 3

SELECT *
FROM vw_student_enrollment_summary
WHERE gpa > 3;

-- ============================================
-- Question 42
-- Try updating the multi-table view.
-- MySQL will throw an error because this
-- view is not updatable.

UPDATE vw_student_enrollment_summary
SET student_name = 'Test Student'
WHERE student_id = 1;

-- Expected:
-- Error: The target table is not updatable.

-- ============================================
-- Question 43
-- Drop both views

DROP VIEW vw_course_stats;
DROP VIEW vw_student_enrollment_summary;

-- Recreate a single-table view
-- with CHECK OPTION

CREATE VIEW vw_student_enrollment_summary AS
SELECT
    student_id,
    first_name,
    last_name,
    department_id
FROM students
WHERE department_id = 1
WITH CHECK OPTION;
-- ============================================
-- Task 3 : Stored Procedures & Transactions
-- ============================================

-- Question 44
-- Stored Procedure to enroll a student

DROP PROCEDURE IF EXISTS sp_enroll_student;

DELIMITER $$

CREATE PROCEDURE sp_enroll_student(
    IN p_student_id INT,
    IN p_course_id INT,
    IN p_enrollment_date DATE
)
BEGIN

    IF EXISTS (
        SELECT 1
        FROM enrollments
        WHERE student_id = p_student_id
        AND course_id = p_course_id
    ) THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Student is already enrolled in this course';

    ELSE

        INSERT INTO enrollments
        (
            student_id,
            course_id,
            enrollment_date,
            grade
        )
        VALUES
        (
            p_student_id,
            p_course_id,
            p_enrollment_date,
            NULL
        );

    END IF;

END$$

DELIMITER ;

-- Test Procedure

CALL sp_enroll_student(2,2,'2022-07-01');



-- ============================================
-- Question 45
-- Department Transfer Transaction
-- ============================================

DROP TABLE IF EXISTS department_transfer_log;

CREATE TABLE department_transfer_log
(
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    old_department INT,
    new_department INT,
    transfer_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP PROCEDURE IF EXISTS sp_transfer_student;

DELIMITER $$

CREATE PROCEDURE sp_transfer_student
(
    IN p_student_id INT,
    IN p_new_department INT
)

BEGIN

DECLARE old_dept INT;

START TRANSACTION;

SELECT department_id
INTO old_dept
FROM students
WHERE student_id = p_student_id;

UPDATE students
SET department_id = p_new_department
WHERE student_id = p_student_id;

INSERT INTO department_transfer_log
(
student_id,
old_department,
new_department
)
VALUES
(
p_student_id,
old_dept,
p_new_department
);

COMMIT;

END$$

DELIMITER ;

-- Test

CALL sp_transfer_student(2,2);



-- ============================================
-- Question 46
-- Rollback Demonstration
-- ============================================

START TRANSACTION;

UPDATE students
SET department_id = 99
WHERE student_id = 3;

ROLLBACK;

SELECT *
FROM students
WHERE student_id = 3;



-- ============================================
-- Question 47
-- Savepoint Demonstration
-- ============================================

START TRANSACTION;

INSERT INTO enrollments
(student_id,course_id,enrollment_date,grade)
VALUES
(3,2,'2022-07-01',NULL);

SAVEPOINT first_insert;

INSERT INTO enrollments
(student_id,course_id,enrollment_date,grade)
VALUES
(999,2,'2022-07-01',NULL);

ROLLBACK TO first_insert;

COMMIT;

SELECT *
FROM enrollments
WHERE student_id = 3;
-- Verify

SELECT *
FROM vw_student_enrollment_summary;