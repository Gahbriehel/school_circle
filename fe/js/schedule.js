// document.addEventListener("DOMContentLoaded", function () {
//     const welcomeText = document.getElementById("welcome");
//     const teacherName = localStorage.getItem("teacherName");
//     const teacherClass = document.getElementById("class");
//     const teacherProfileClass = localStorage.getItem("profileClass");
  
//     if (teacherName) {
//       welcomeText.innerHTML = `${teacherName.toUpperCase()}`;
//       teacherClass.innerHTML = `CLASS: ${teacherProfileClass}`;
//     }
//   });
  
  const itemForm = document.getElementById("itemsForm");
  const url = "https://schoolcircle.gahbriehel.tech/api/students";
  
  // Get request
  fetch(url)
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      console.log(data.students);
      console.log(data.students[0].first_name);
      if (data.students) {
        let student = ""; // Initialize the table rows string
        data.students.forEach((students) => {
          // Create table row for each student
          student += `<tr class="trow">`;
          student += `<td class="table-row">${students.first_name}</td>`;
          student += `<td class="table-row">${students.last_name}</td>`;
          student += `<td class="table-row">${students.class_d}</td>`;
          student += `<td class="table-row">${students.gender}</td>`;
          student += `<td class="table-row">${students.street}, ${students.city}, ${students.country}</td>`;
          student += "</tr>";
        });
        // Insert the generated rows into the table body
        document.getElementById("data").innerHTML = student;
        console.log("Data inserted into table.");
      } else {
        console.log("No data found.");
      }
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
  