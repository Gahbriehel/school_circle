document.addEventListener("DOMContentLoaded", function () {
  const welcomeText = document.getElementById("welcome");
  const teacherName = localStorage.getItem("teacherName");

  if (welcomeText) {
    if (teacherName) {
      welcomeText.innerHTML = `WELCOME ${teacherName.toUpperCase()}`;
    } else {
      welcomeText.innerHTML = `WELCOME 'unknown'`;
    }
  }
});
