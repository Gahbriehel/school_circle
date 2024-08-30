document.addEventListener("DOMContentLoaded", function () {
  const togglePassword = document.getElementById("togglePassword");
  const password = document.getElementById("password");
  const toggleConfirmPassword = document.getElementById(
    "toggleConfirmPassword"
  );
  const confirmPassword = document.getElementById("confirm_password");

  togglePassword.addEventListener("click", function () {
    // Toggle the type attribute
    const type =
      password.getAttribute("type") === "password" ? "text" : "password";
    password.setAttribute("type", type);

    // Toggle the eye icon
    this.classList.toggle("fa-eye-slash");
  });

  toggleConfirmPassword.addEventListener("click", function () {
    const type =
      confirmPassword.getAttribute("type") === "password" ? "text" : "password";
    confirmPassword.setAttribute("type", type);

    this.classList.toggle("fa-eye-slash");
  });
});
