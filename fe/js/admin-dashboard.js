document.addEventListener("DOMContentLoaded", function () {
  const welcomeText = document.getElementById("welcome");
  const adminName = localStorage.getItem("adminName");

  // const adminClass = document.getElementById("class");

  if (welcomeText) {
    if (adminName) {
      welcomeText.innerHTML = `WELCOME ${adminName.toUpperCase()}`;
      // adminClass.innerHTML = `CLASS: `;
    } else {
      welcomeText.innerHTML = `WELCOME 'unknown'`;
    }
  }
  const viewStudents = document.getElementById("view-students-btn");
  viewStudents.addEventListener("click", function () {
    window.location.href = "./admin-view-students.html";
  });

  const viewTeachers = document.getElementById("view-teachers-btn");
  viewTeachers.addEventListener("click", function () {
    window.location.href = "./admin-view-teachers.html";
  });
});
