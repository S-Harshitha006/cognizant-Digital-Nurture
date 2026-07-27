function CourseCard({ name, code, credits, grade, onEnroll }) {
  return (
    <div
      style={{
        border: "1px solid #ccc",
        borderRadius: "8px",
        padding: "15px",
        margin: "15px 0",
        boxShadow: "2px 2px 8px #ddd",
      }}
    >
      <h2>{name}</h2>
      <p><strong>Code:</strong> {code}</p>
      <p><strong>Credits:</strong> {credits}</p>
      <p><strong>Grade:</strong> {grade}</p>

      <button onClick={onEnroll}>Enroll</button>
    </div>
  );
}

export default CourseCard;