import { useSelector, useDispatch } from "react-redux";
import { unenroll } from "../redux/enrollmentSlice";

function ProfilePage() {
  const dispatch = useDispatch();

  const enrolledCourses = useSelector(
    (state) => state.enrollment.enrolledCourses
  );

  return (
    <div className="profile-page">
      <h2>Student Profile</h2>

      <h3>Enrolled Courses</h3>

      {enrolledCourses.length === 0 ? (
        <p>No courses enrolled yet.</p>
      ) : (
        enrolledCourses.map((course) => (
          <div key={course.id} className="course-card">
            <h3>{course.name}</h3>

            <p>
              <strong>Course Code:</strong> {course.code}
            </p>

            <p>
              <strong>Credits:</strong> {course.credits}
            </p>

            <p>
              <strong>Grade:</strong> {course.grade}
            </p>

            <button
              onClick={() => dispatch(unenroll(course.id))}
            >
              Remove
            </button>
          </div>
        ))
      )}
    </div>
  );
}

export default ProfilePage;