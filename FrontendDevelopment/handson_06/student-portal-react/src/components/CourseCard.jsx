import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { enroll } from "../redux/enrollmentSlice";

function CourseCard({ course }) {
  const navigate = useNavigate();
  const dispatch = useDispatch();

  const handleEnroll = () => {
    dispatch(enroll(course));
    navigate("/profile");
  };

  const handleViewDetails = () => {
    navigate(`/courses/${course.id}`);
  };

  return (
    <div className="course-card">
      <h3>{course.title}</h3>

      <p>
        <strong>Instructor:</strong> {course.instructor}
      </p>

      <p>
        <strong>Duration:</strong> {course.duration}
      </p>

      <div className="button-group">
        <button onClick={handleViewDetails}>
          View Details
        </button>

        <button onClick={handleEnroll}>
          Enroll
        </button>
      </div>
    </div>
  );
}

export default CourseCard;