document.addEventListener("DOMContentLoaded", function () {
  const optionButtons = document.querySelectorAll(".selection-btn");
  const continueButton = document.getElementById("continue-btnn");
  let selectedOption = null;
  let selectedTag;

  optionButtons.forEach((button) => {
    button.addEventListener("click", function () {
      optionButtons.forEach((btn) => btn.classList.remove("selected"));
      this.classList.add("selected");

      selectedOption = this.id;
      selectedTag = this.name;

      continueButton.classList.add("enabled");
      continueButton.disabled = false;
    });
  });

  continueButton.addEventListener("click", function () {
    if (selectedOption == "student-btnn") {
      // alert(`You are signing in as a ${selectedTag}`);
      window.location.href = "./student-sign-in.html";
    } else if (selectedOption == "teacher-btnn") {
      // alert(`You are signing in as a ${selectedTag}`);
      window.location.href = "./teacher-sign-in.html";
    } else {
      // alert(`You are signing in as an ${selectedTag}`);
      window.location.href = "./admin-sign-in.html";
    }
  });
});
