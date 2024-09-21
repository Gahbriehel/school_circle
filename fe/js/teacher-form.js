document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("form-id-teacher");
  const password = document.getElementById("password");
  const confirmPassword = document.getElementById("confirm_password");
  const fname = document.getElementById("fname");
  const classId = document.getElementById("class_id");

  form.addEventListener("submit", function (event) {
    if (password.value !== confirmPassword.value) {
      event.preventDefault();
      alert("Passwords do not match. Please try again.");
    }
  });

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    const formData = new FormData(form);

    // Convert form data to JSON object
    const data = Object.fromEntries(formData.entries());

    fetch("http://localhost:5000/api/teachers", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then(async (response) => {
        if (response.status === 200 || response.status === 201) {
          let teacherProfileName = fname.value;
          localStorage.setItem("teacherName", teacherProfileName);
          let teacherClass = classId.value;
          localStorage.setItem("profileClass", teacherClass);
          let data = await response.json();
          console.log("sent teacher id: ", data.teacher.id);
          let teacherId = data.teacher.id;
          localStorage.setItem("retrievedTeacherId", teacherId);
          window.location.href = "./teacher-dashboard.html";
        } else {
          alert("Oops! There was a problem submitting the form");
          return response.json().then((errorData) => {
            console.error("Error:", errorData);
          });
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("An unexpected error occurred. Please try again.");
      });
  });
});
