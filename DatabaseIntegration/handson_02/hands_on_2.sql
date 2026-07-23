USE college_db;

INSERT INTO students
(first_name,last_name,email,date_of_birth,department_id,enrollment_year)
VALUES
('Harshitha','Sugumar','harshitha.sugumar@college.edu','2004-04-06',1,2023),
('Rahul','Kumar','rahul.kumar@college.edu','2003-10-15',2,2022);

UPDATE enrollments
SET grade='B'
WHERE student_id=5
AND course_id=1;

SELECT *
FROM enrollments
WHERE grade IS NULL;

DELETE FROM enrollments
WHERE grade IS NULL;

SELECT COUNT(*) AS total_students
FROM students;

SELECT COUNT(*) AS total_enrollments
FROM enrollments;

SELECT *
FROM students
WHERE enrollment_year=2022
ORDER BY last_name;

SELECT *
FROM courses
WHERE credits>3
ORDER BY credits DESC;

SELECT *
FROM professors
WHERE salary BETWEEN 80000 AND 95000;

SELECT *
FROM students
WHERE email LIKE '%@college.edu';

SELECT enrollment_year,
COUNT(*) AS total_students
FROM students
GROUP BY enrollment_year;

SELECT
CONCAT(first_name,' ',last_name) AS student_name,
dept_name
FROM students
INNER JOIN departments
ON students.department_id=departments.department_id;

SELECT
CONCAT(first_name,' ',last_name) AS student_name,
course_name,
grade
FROM enrollments
INNER JOIN students
ON enrollments.student_id=students.student_id
INNER JOIN courses
ON enrollments.course_id=courses.course_id;

SELECT
CONCAT(first_name,' ',last_name) AS student_name
FROM students
LEFT JOIN enrollments
ON students.student_id=enrollments.student_id
WHERE enrollments.student_id IS NULL;

SELECT
courses.course_name,
COUNT(enrollments.student_id) AS total_students
FROM courses
LEFT JOIN enrollments
ON courses.course_id=enrollments.course_id
GROUP BY courses.course_id,courses.course_name;

SELECT
departments.dept_name,
professors.prof_name,
professors.salary
FROM departments
LEFT JOIN professors
ON departments.department_id=professors.department_id;

SELECT
course_name,
COUNT(enrollments.student_id) AS enrollment_count
FROM courses
LEFT JOIN enrollments
ON courses.course_id=enrollments.course_id
GROUP BY course_name;

SELECT
dept_name,
ROUND(AVG(salary),2) AS average_salary
FROM departments
LEFT JOIN professors
ON departments.department_id=professors.department_id
GROUP BY dept_name;

SELECT
dept_name,
budget
FROM departments
WHERE budget>600000;

SELECT
grade,
COUNT(*) AS total
FROM enrollments
INNER JOIN courses
ON enrollments.course_id=courses.course_id
WHERE course_code='CS101'
GROUP BY grade;

SELECT
dept_name,
COUNT(student_id) AS total_students
FROM departments
INNER JOIN students
ON departments.department_id=students.department_id
GROUP BY dept_name
HAVING COUNT(student_id)>2;