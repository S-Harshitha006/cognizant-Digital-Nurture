import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import CourseCard from "../components/CourseCard";
import {
  fetchAllCourses,
  selectCourses,
  selectCoursesLoading,
  selectCoursesError,
} from "../redux/enrollmentSlice";

function CoursesPage() {
  const dispatch = useDispatch();

  const courses = useSelector(selectCourses);
  const loading = useSelector(selectCoursesLoading);
  const error = useSelector(selectCoursesError);

  // Task 145 - Dispatch Async Thunk
  useEffect(() => {
    dispatch(fetchAllCourses());
  }, [dispatch]);

  if (loading) {
    return <h2>Loading courses...</h2>;
  }

  if (error) {
    return (
      <h2 style={{ color: "red" }}>
        Error: {error}
      </h2>
    );
  }

  return (
    <div className="courses-page">
      <h2>Available Courses</h2>

      <div className="course-grid">
        {courses.map((course) => (
          <CourseCard
            key={course.id}
            course={{
              id: course.id,
              name: course.title,
              code: `CS${course.id}`,
              credits: 3,
              grade: "N/A",
            }}
          />
        ))}
      </div>
    </div>
  );
}

export default CoursesPage;