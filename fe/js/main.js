// alert("Welcome!!!")
const nav = document.querySelector(".nav_links");
const signupBtn = document.getElementById("get-started-btn");

window.addEventListener("scroll", () => {
  document
    .querySelector("nav")
    .classList.toggle("window-scrolled", window.scrollY > 0);
});

//
//
// Button selection script
//
//

document.addEventListener("DOMContentLoaded", function () {
  const optionButtons = document.querySelectorAll(".select-btn");
  const continueButton = document.getElementById("continue-btn");
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
    if (selectedOption == "student-btn") {
      alert(`You have chosen to register as a ${selectedTag}`);
      window.location.href = "./signup-student.html";
    } else {
      alert(`You have chosen to register as a ${selectedTag}`);
      window.location.href = "./signup-teacher.html";
    }
  });
});

//
//
//
//

const tourBtn = document.getElementById("tour-btn");

const goTour = () => {
  window.location.href = "tour.html";
};

const goSignup = () => {
  window.location.href = "./signup.html";
};

signupBtn.onclick = goSignup;
tourBtn.onclick = goTour;
