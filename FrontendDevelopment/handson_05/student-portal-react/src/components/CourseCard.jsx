function CourseCard({

  id,
  name,
  code,
  credits,
  grade,
  onEnroll

}) {

  function handleClick() {

    onEnroll({

      id,
      name,
      code,
      credits,
      grade

    });

  }

  return (

    <div className="course-card">

      <h3>{name}</h3>

      <p>

        <strong>Code:</strong> {code}

      </p>

      <p>

        <strong>Credits:</strong> {credits}

      </p>

      <p>

        <strong>Grade:</strong> {grade}

      </p>

      <button

        className="enroll-btn"

        onClick={handleClick}

      >

        Enroll

      </button>

    </div>

  );

}

export default CourseCard;