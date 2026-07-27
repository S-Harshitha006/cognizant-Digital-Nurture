import { Link } from "react-router-dom";

function HomePage() {
  return (
    <div className="home-page">
      <h1>🎓 Welcome to Student Portal</h1>

      <p>
        Manage your courses, view course details, and enroll in courses
        using React Router and Redux Toolkit.
      </p>

      <Link to="/courses">
        <button>Explore Courses</button>
      </Link>
    </div>
  );
}

export default HomePage;