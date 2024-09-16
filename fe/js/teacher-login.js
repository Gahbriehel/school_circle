const loginApiUrl = "http://localhost:5000/api/teachers/login";

document.addEventListener("DOMContentLoaded", function () {
  const loginForm = document.getElementById("teacher-login-form");
  const loginError = document.getElementById("login-error");

  loginForm.addEventListener("submit", function (e) {
    e.preventDefault();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const loginData = { email, password };

    fetch(loginApiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(loginData),
    })
      .then((response) => {
        if (response.status == 200) {
          return response.json();
        } else if (response.status == 401) {
          throw new Error("Invalid credentials");
        } else {
          throw new Error("Server Error");
        }
      }) 
      .then((userData) => {
        localStorage.setItem("teacherName", userData.Teacher.first_name);
        window.location.href = "./teacher-dashboard.html";
      })
      .catch((error) => {
        console.log(error);
        loginError.style.display = "block";
      });
  });
});
