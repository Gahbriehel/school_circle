document.getElementById("form-id").addEventListener("submit", function (e) {
  e.preventDefault();

  const form = e.target;
  const formData = new FormData(form); // Create FormData object from form

  // Convert form data to JSON object
  const data = Object.fromEntries(formData.entries());

  fetch("http://localhost:5000/api/teachers", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data), // Send JSON data
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((result) => {
      console.log("Success:", result);
      // Handle success (show message, redirect, etc.)
    })
    .catch((error) => {
      console.error("Error:", error);
      // Handle error (show error message, etc.)
    });
});
