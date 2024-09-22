document.addEventListener("DOMContentLoaded", function () {
  const welcomeText = document.getElementById("welcome");
  const teacherName = localStorage.getItem("teacherName");
  const teacherClass = document.getElementById("class");
  const teacherProfileClass = localStorage.getItem("profileClass");

  if (teacherName) {
    welcomeText.innerHTML = `${teacherName.toUpperCase()}`;
    teacherClass.innerHTML = `CLASS: ${teacherProfileClass}`;
  }
});
const teacherId = localStorage.getItem("retrievedTeacherId");
const itemForm = document.getElementById("itemsForm");

const url = `https://schoolcircle.gahbriehel.tech/api/teachers/${teacherId}/students`;
console.log("Fetching data from URL:", url);

// Get request
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
        student += `<td class="table-row">${students.street}, ${students.city}, ${students.country}</td>`;
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
