document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("form-id");
  const password = document.getElementById("password");
  const confirmPassword = document.getElementById("confirm_password");

  form.addEventListener("submit", function (event) {
    if (password.value !== confirmPassword.value) {
      event.preventDefault();
      alert("Passwords do not match. Please try again.");
    }
  });
});

document.getElementById("form-id").addEventListener("submit", function (e) {
  e.preventDefault();
  const form = e.target;
  const formData = new FormData(form);

  // Convert form data to JSON object
  const data = Object.fromEntries(formData.entries());

  fetch("http://localhost:5000/api/students", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data), // Send JSON data
  })
    .then((response) => {
      if (response.status == 200 || response.status == 201) {
        window.location.href = "./student-dashboard.html";
      } else {
        alert("Oops! There was a problem submitting the form");
        return response.json().then((errorData) => {
          console.error("Error:", errorData);
        });
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      // Handle error (show error message, etc.)
      alert("An unexpected error occurred. Please try again.");
    });
});
