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

// Nav behaviour for responsiveness
const openNavBtn = document.querySelector("#nav_toggle-open");
const closeNavBtn = document.querySelector("#nav_toggle-close");

const openNav = () => {
  nav.style.display = "flex";
  openNavBtn.style.display = "none";
  closeNavBtn.style.display = "inline-block";
};

openNavBtn.addEventListener("click", openNav);

const closeNav = () => {
  nav.style.display = "none";
  openNavBtn.style.display = "inline-block";
  closeNavBtn.style.display = "none";
};

closeNavBtn.addEventListener("click", closeNav);

nav.querySelectorAll("li a").forEach((navLink) => {
  navLink.addEventListener("click", closeNav);
});
