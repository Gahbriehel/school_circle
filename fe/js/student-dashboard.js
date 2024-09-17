document.addEventListener("DOMContentLoaded", function () {
  const welcomeText = document.getElementById("welcome");
  const studentName = localStorage.getItem("studentName");
  const studentClass = document.getElementById("class");
  const profileClass = localStorage.getItem("studentClass");

  if (welcomeText) {
    if (studentName) {
      welcomeText.innerHTML = `WELCOME ${studentName.toUpperCase()}`;
      studentClass.innerHTML = `CLASS: ${profileClass.toUpperCase()}`;
    } else {
      welcomeText.innerHTML = `WELCOME 'unknown'`;
    }
  }
});
