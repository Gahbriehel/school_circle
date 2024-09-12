document.addEventListener("DOMContentLoaded", function () {
  const welcomeText = document.getElementById("welcome");
  const studentName = localStorage.getItem("studentName");
  const studentClass = document.getElementById("class");

  if (welcomeText) {
    if (studentName) {
      welcomeText.innerHTML = `WELCOME ${studentName.toUpperCase()}`;
      studentClass.innerHTML = `CLASS: `;
    } else {
      welcomeText.innerHTML = `WELCOME 'unknown'`;
    }
  }
});
