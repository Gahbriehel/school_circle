document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("form-id-teacher");
  const password = document.getElementById("password");
  const confirmPassword = document.getElementById("confirm_password");

  form.addEventListener("submit", function (event) {
    if (password.value !== confirmPassword.value) {
      event.preventDefault();
      alert("Passwords do not match. Please try again.");
    }
  });
});

document
  .getElementById("form-id-teacher")
  .addEventListener("submit", function (e) {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);

    const data = Object.fromEntries(formData.entries());

    fetch("http://localhost:5000/api/teachers", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (response.status == 200 || response.status == 201) {
          alert("Registration successful");
          window.location.href = "./teacher-dashboard.html";
        } else {
          alert("Oops!! Something went wrong");
          throw new Error("Response response was not okay!");
        }
      })
      .then((result) => {
        console.log("Success:", result);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
