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
  const viewStudents = document.getElementById("view-students-btn");
  viewStudents.addEventListener("click", function () {
    alert("You are being redirected to view your students");
    window.location.href = "./students.html";
  });
});
