import { Link } from "react-router-dom";
import { useSelector } from "react-redux";

function Header() {
  const enrolledCourses = useSelector(
    (state) => state.enrollment.enrolledCourses
  );

  return (
    <header className="header">
      <div className="logo">
        <h2>🎓 Student Portal</h2>
      </div>

      <nav>
        <ul className="nav-links">
          <li>
            <Link to="/">Home</Link>
          </li>

          <li>
            <Link to="/courses">Courses</Link>
          </li>

          <li>
            <Link to="/profile">
              Profile ({enrolledCourses.length})
            </Link>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default Header;