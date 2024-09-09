document.addEventListener("DOMContentLoaded", function () {
  const profileName = localStorage.getItem("profileName");
  if (profileName) {
    const welcomeText = document.getElementById("welcome");
    welcomeText.innerHTML = `WELCOME ${profileName}!`;
  }
});
