const students = document.querySelector("#data");
const editStudent = document.querySelector("#data");
const addStudent = document.querySelector("#studentForm");
const url = "https://schoolcircle.gahbriehel.tech/api/students";

document.addEventListener("DOMContentLoaded", function () {
  const welcomeText = document.getElementById("welcome");
  const adminName = localStorage.getItem("adminName");
  const adminClass = document.getElementById("class");

  if (adminName) {
    welcomeText.innerHTML = `${adminName.toUpperCase()}`;
    adminClass.innerHTML = `sudo`;
  }
});

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
        student += `<td class="table-row">${students.gender}</td>`;
        const dob = students.dob ? students.dob : null;
        if (dob) {
          const dobYear = dob.slice(0, 4);
          const presentAge = 2024 - dobYear;
          student += `<td class="table-row">${presentAge}</td>`;
        } else {
          student += `<td class="table-row">N/A</td>`;
        }
        student += `<td class="table-row">${students.class_d}</td>`;
        student += `<td class="table-row">${students.street}, ${students.city}, ${students.country}</td>`;
        student += `<td> <a href="#" student-id="${students.id}" class="editBtn fa-regular fa-pen-to-square" style="color: grey;"></a>  </td>`;
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

// POST student
addStudent.addEventListener("submit", (button) => {
  button.preventDefault();
  if (
    !first_name.value ||
    !last_name.value ||
    !email.value ||
    !username.value ||
    !password.value ||
    !confirm_password.value
  ) {
    alert("Please fill all fields before submitting!");
    return;
  }
  fetch(url, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      first_name: first_name.value,
      last_name: last_name.value,
      email: email.value,
      username: username.value,
      password: password.value,
      confirm_password: confirm_password.value,
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      window.location.reload(true);
    });
});

const editingForm = document.getElementById("itemsForm");

// PUT student
editStudent.addEventListener("click", (e) => {
  e.preventDefault();
  if (e.target.classList.contains("editBtn")) {
    const studentId = e.target.getAttribute("student-id");

    fetch(`${url}/${studentId}`)
      .then((res) => res.json())
      .then((studentData) => {
        console.log("Fetched student data:", studentData);
        first_name.value = studentData.Student.first_name;
        last_name.value = studentData.Student.last_name;
        email.value = studentData.Student.email;
        username.value = studentData.Student.username;
      })
      .catch((error) => {
        console.error("Error fetching item data:", error);
      });

    if (editingForm) {
      editingForm.classList.add("visible");
    }

    if (editingForm) {
      editingForm.addEventListener("submit", (event) => {
        event.preventDefault();

        const updatedData = {
          first_name: first_name.value,
          last_name: last_name.value,
          email: email.value,
          username: username.value,
          password: password.value,
          confirm_password: confirm_password.value,
        };

        fetch(`${url}/${studentId}`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(updatedData),
        })
          .then((res) => res.json())
          .then((data) => {
            console.log(data);
            window.location.reload(true);
          })
          .catch((error) => {
            console.error("Error:", error);
          });

        if (editingForm) {
          editingForm.classList.remove("visible");
        }
      });
    }
  }
});
