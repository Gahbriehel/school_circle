const itemForm = document.getElementById("itemsForm");
const url = "http://localhost:5000/api/students";

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
        student += `<td> <a href="#" student-id="${students.id}" class="fa-regular fa-pen-to-square" style="color: grey;"></a>  </td>`;
        student += `<td> <a href="#" student-id="${students.id}" class="deleteBtn fa-solid fa-trash" style="color: grey;"></a>  </td>`;
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
