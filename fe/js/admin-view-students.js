const students = document.querySelector("#data");

document.addEventListener("DOMContentLoaded", function () {
  const welcomeText = document.getElementById("welcome");
  const adminName = localStorage.getItem("adminName");
  // const adminClass = document.getElementById("class");

  if (adminName) {
    welcomeText.innerHTML = `${adminName.toUpperCase()}`;
    // adminClass.innerHTML = `CLASS: `;
  }
});

const itemForm = document.getElementById("itemsForm");
const url = "http://localhost:5000/api/students";

// GET students
fetch(url)
  .then((res) => res.json())
  .then((data) => {
    console.log(data);
    console.log(data.students);
    if (data.students) {
      let student = "";
      data.students.forEach((students) => {
        student += `<tr class="trow">`;
        student += `<td class="table-row">${students.first_name}</td>`;
        student += `<td class="table-row">${students.last_name}</td>`;
        student += `<td class="table-row">${students.class_d}</td>`;
        student += `<td class="table-row">${students.gender}</td>`;
        student += `<td class="table-row">${students.street}, ${students.city}, ${students.country}</td>`;
        student += `<td> <a href="#" student-id="${students.id}" class="fa-regular fa-pen-to-square" style="color: grey;"></a>  </td>`;
        student += `<td> <a href="#" student-id="${students.id}" class="deleteBtn fa-solid fa-trash" style="color: grey;"></a>  </td>`;
        student += "</tr>";
      });
      document.getElementById("data").innerHTML = student;
      console.log("Data inserted into table.");
    } else {
      console.log("No data found.");
    }
  })
  .catch((error) => {
    console.error("Error fetching data:", error);
  });

// DELETE student by id

students.addEventListener("click", (e) => {
  e.preventDefault();
  if (e.target.classList.contains("deleteBtn")) {
    const studentId = e.target.getAttribute("student-id");

    fetch(`${url}/${studentId}`, {
      method: "DELETE",
    })
      .then((res) => {
        if (res.ok) {
          console.log(`Student with id ${studentId} deleted successfully.`);
        } else {
          console.error(`Failed to delete Student with id ${studentId}.`);
        }
        console.log("Student Deleted Successfully! Refresh Page");
      })
      .catch((error) => {
        console.error("Error:", error);
      });
    window.alert("Student Deleted Successfully!\nRefresh Page");
  }
});
