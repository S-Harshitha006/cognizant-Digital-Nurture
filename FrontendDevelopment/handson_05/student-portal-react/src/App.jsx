import { useState, useEffect } from "react";
import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";
import StudentProfile from "./components/StudentProfile";
import "./App.css";

function App() {
  const [courses, setCourses] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [enrolledCourses, setEnrolledCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/posts")
      .then((res) => res.json())
      .then((data) => {
        const courseData = data.slice(0, 5).map((post, index) => ({
          id: post.id,
          name: post.title,
          code: `CS30${index + 1}`,
          credits: 3,
          grade: "A",
        }));
        setCourses(courseData);
        setLoading(false);
      })
      .catch(() => {
        setError("Failed to load courses.");
        setLoading(false);
      });
  }, []);

  // Runs whenever courses state changes
  useEffect(() => {
    console.log("Courses updated");
  }, [courses]);

  const handleEnroll = (course) => {
    if (!enrolledCourses.find((c) => c.id === course.id)) {
      setEnrolledCourses([...enrolledCourses, course]);
    }
  };

  const filteredCourses = courses.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="App">
      <Header
        siteName="Student Portal"
        enrolledCount={enrolledCourses.length}
      />

      <div className="container">
        <input
          type="text"
          placeholder="Search Courses..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />

        {loading && <h3>Loading...</h3>}
        {error && <h3>{error}</h3>}

        {!loading &&
          !error &&
          filteredCourses.map((course) => (
            <CourseCard
              key={course.id}
              {...course}
              onEnroll={() => handleEnroll(course)}
            />
          ))}

        <StudentProfile />
      </div>

      <Footer />
    </div>
  );
}

export default App;