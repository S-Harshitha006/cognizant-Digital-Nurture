import { useState, useEffect } from "react";

import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";
import StudentProfile from "./components/StudentProfile";

import { coursesData } from "./data/courses";

function App() {

  const [courses, setCourses] = useState(coursesData);

  const [searchTerm, setSearchTerm] = useState("");

  const [enrolledCourses, setEnrolledCourses] = useState([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  useEffect(() => {

    async function loadCourses() {

      try {

        const response = await fetch(
          "https://jsonplaceholder.typicode.com/posts?_limit=5"
        );

        if (!response.ok) {
          throw new Error("Unable to fetch courses.");
        }

        const data = await response.json();

        const apiCourses = data.map((post, index) => ({
          id: post.id,
          name: post.title.substring(0, 20),
          code: `CS10${index + 1}`,
          credits: (index % 4) + 2,
          grade: "A"
        }));

        setCourses(apiCourses);

      } catch (err) {

        setError(err.message);

      } finally {

        setLoading(false);

      }

    }

    loadCourses();

  }, []);

  /*
     Dependency array ensures this effect
     runs only when courses changes.
  */

  useEffect(() => {

    console.log("Courses updated");

  }, [courses]);

  function handleEnroll(course) {

    const exists = enrolledCourses.find(
      c => c.id === course.id
    );

    if (!exists) {

      setEnrolledCourses([
        ...enrolledCourses,
        course
      ]);

    }

  }

  const filteredCourses = courses.filter(course =>

    course.name
      .toLowerCase()
      .includes(searchTerm.toLowerCase())

  );

  return (

    <>

      <Header

        siteName="Student Portal"

        enrolledCount={enrolledCourses.length}

      />

      <main className="container">

        <h2>Available Courses</h2>

        <input

          type="text"

          placeholder="Search Course"

          value={searchTerm}

          onChange={(e) =>
            setSearchTerm(e.target.value)
          }

        />

        <br />

        <br />

        {loading && <h3>Loading...</h3>}

        {error && (
          <h3 className="error">
            {error}
          </h3>
        )}

        <div className="course-grid">

          {!loading &&
            !error &&
            filteredCourses.map(course => (

              <CourseCard

                key={course.id}

                {...course}

                onEnroll={handleEnroll}

              />

            ))}

        </div>

        <StudentProfile />

      </main>

      <Footer />

    </>

  );

}

export default App;