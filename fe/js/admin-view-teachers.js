const teachers = document.querySelector("#data");
const editTeacher = document.querySelector("#data");
const addTeacher = document.querySelector("#teacherForm");
const url = "http://localhost:5000/api/teachers";

document.addEventListener("DOMContentLoaded", function () {
  const welcomeText = document.getElementById("welcome");
  const adminName = localStorage.getItem("adminName");

  if (adminName) {
    welcomeText.innerHTML = `${adminName.toUpperCase()}`;
  }
});

// GET teachers
fetch(url)
  .then((res) => res.json())
  .then((data) => {
    console.log(data.teachers);
    if (data.teachers) {
      let teacher = "";
      data.teachers.forEach((teachers) => {
        teacher += `<tr class="trow">`;
        teacher += `<td class="table-row">${teachers.first_name}</td>`;
        teacher += `<td class="table-row">${teachers.last_name}</td>`;
        teacher += `<td class="table-row">${teachers.gender}</td>`;
        teacher += `<td class="table-row">${teachers.class_d}</td>`;
        teacher += `<td class="table-row">${teachers.street}, ${teachers.city}, ${teachers.country}</td>`;
        teacher += `<td> <a href="#" teacher-id="${teachers.id}" class="editBtn fa-regular fa-pen-to-square" style="color: grey;"></a>  </td>`;
        teacher += `<td> <a href="#" teacher-id="${teachers.id}" class="deleteBtn fa-solid fa-trash" style="color: grey;"></a>  </td>`;
      });
      teachers.innerHTML = teacher;
      console.log("Data inserted into table");
    } else {
      console.log("No data found.");
    }
  })
  .catch((error) => {
    console.log("Error fetching data");
  });

teachers.addEventListener("click", (e) => {
  e.preventDefault();
  if (e.target.classList.contains("deleteBtn")) {
    const teacherId = e.target.getAttribute("teacher-id");

    fetch(`${url}/${teacherId}`, {
      method: "DELETE",
    })
      .then((res) => {
        if (res.ok) {
          console.log(`Teacher with id ${teacherId} deleted successfully.`);
        } else {
          console.error(`Failed to delete teacher with id ${teacherId}.`);
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
    window.alert("Teacher Deleted Successfully!\nRefresh Page");
  }
});
