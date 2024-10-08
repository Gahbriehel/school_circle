const loginApiUrl = "https://schoolcircle.gahbriehel.tech/api/admins/login";

document.addEventListener("DOMContentLoaded", function () {
  const loginForm = document.getElementById("admin-login-form");
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
          console.log(response);
          return response.json();
        } else if (response.status == 401) {
          throw new Error("Invalid credentials");
        } else {
          throw new Error("Server Error");
        }
      })
      .then((userData) => {
        localStorage.setItem("adminName", userData.admin.first_name);
        console.log(userData);

        window.location.href = "./admin-dashboard.html";
      })
      .catch((error) => {
        console.log(error);
        loginError.style.display = "block";
      });
  });
});
