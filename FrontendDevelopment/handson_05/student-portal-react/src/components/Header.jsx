function Header({ siteName, enrolledCount }) {
  return (
    <header style={{ background: "#1976d2", color: "white", padding: "15px" }}>
      <h1>{siteName}</h1>

      <nav>
        <a href="#" style={{ color: "white", marginRight: "15px" }}>Home</a>
        <a href="#" style={{ color: "white", marginRight: "15px" }}>Courses</a>
        <a href="#" style={{ color: "white" }}>Profile</a>
      </nav>

      <h3>Enrolled Courses: {enrolledCount}</h3>
    </header>
  );
}

export default Header;