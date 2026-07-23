import { useState, useEffect } from "react";

function StudentProfile() {

  const [profile, setProfile] = useState({

    name: "Harshitha",

    email: "harshitha@example.com",

    semester: "7"

  });

  function handleChange(event) {

    const { name, value } = event.target;

    setProfile({

      ...profile,

      [name]: value

    });

  }

  useEffect(() => {

    console.log("Profile Updated");

  }, [profile]);

  return (

    <section className="profile-section">

      <h2>Student Profile</h2>

      <form className="profile-form">

        <label>

          Name

        </label>

        <input

          type="text"

          name="name"

          value={profile.name}

          onChange={handleChange}

        />

        <label>

          Email

        </label>

        <input

          type="email"

          name="email"

          value={profile.email}

          onChange={handleChange}

        />

        <label>

          Semester

        </label>

        <input

          type="text"

          name="semester"

          value={profile.semester}

          onChange={handleChange}

        />

      </form>

      <div className="profile-preview">

        <h3>Preview</h3>

        <p>

          <strong>Name:</strong> {profile.name}

        </p>

        <p>

          <strong>Email:</strong> {profile.email}

        </p>

        <p>

          <strong>Semester:</strong> {profile.semester}

        </p>

      </div>

    </section>

  );

}

export default StudentProfile;