import CourseCard from "../components/CourseCard";
import courses from "../data/courses";

function CoursesPage() {
  return (
    <div>
      <h2>Available Courses</h2>

      <div className="course-container">
        {courses.map((course) => (
          <CourseCard
            key={course.id}
            course={course}
          />
        ))}
      </div>
    </div>
  );
}

export default CoursesPage;