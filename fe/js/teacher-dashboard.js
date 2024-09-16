document.addEventListener("DOMContentLoaded", function () {
  const welcomeText = document.getElementById("welcome");
  const teacherName = localStorage.getItem("teacherName");
  const teacherClass = document.getElementById("class");
  const teacherProfileClass = localStorage.getItem("profileClass");

  if (welcomeText) {
    if (teacherName) {
      welcomeText.innerHTML = `WELCOME ${teacherName.toUpperCase()}`;
      teacherClass.innerHTML = `CLASS: ${teacherProfileClass}`;
    } else {
      welcomeText.innerHTML = `WELCOME 'unknown'`;
    }
  }
  const viewStudents = document.getElementById("view-students-btn");
  viewStudents.addEventListener("click", function () {
    alert("You are being redirected to view your students");
    window.location.href = "./teacher-view-students.html";
  });
  
});
