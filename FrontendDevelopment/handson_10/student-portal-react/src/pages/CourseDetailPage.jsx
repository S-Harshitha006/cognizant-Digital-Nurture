import { useParams, Link } from "react-router-dom";
import courses from "../data/courses";

function CourseDetailPage() {
  const { courseId } = useParams();

  const course = courses.find(
    (c) => c.id === Number(courseId)
  );

  if (!course) {
    return (
      <div>
        <h2>Course Not Found</h2>
        <Link to="/courses">
          <button>Back to Courses</button>
        </Link>
      </div>
    );
  }

  return (
    <div className="course-details">
      <h2>{course.name}</h2>

      <p>
        <strong>Course ID:</strong> {course.id}
      </p>

      <p>
        <strong>Course Code:</strong> {course.code}
      </p>

      <p>
        <strong>Credits:</strong> {course.credits}
      </p>

      <p>
        <strong>Grade:</strong> {course.grade}
      </p>

      <Link to="/courses">
        <button>Back to Courses</button>
      </Link>
    </div>
  );
}

export default CourseDetailPage;