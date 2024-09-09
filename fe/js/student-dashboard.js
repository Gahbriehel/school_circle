document.addEventListener("DOMContentLoaded", function () {
  const welcomeText = document.getElementById("welcome");
  const studentName = localStorage.getItem("studentName");

  if (welcomeText) {
    if (studentName) {
      welcomeText.innerHTML = `WELCOME ${studentName.toUpperCase()}`;
    } else {
      welcomeText.innerHTML = `WELCOME 'unknown'`;
    }
  }
});
