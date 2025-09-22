// Typewriter effect
const text = "What would you like to learn today?";
let index = 0;
const speed = 30;
const typewriterElement = document.getElementById("typewriter");
typewriterElement.innerHTML = "";

function typeWriter() {
  if (index < text.length) {
    typewriterElement.innerHTML += text.charAt(index);
    index++;
    setTimeout(typeWriter, speed);
  }
}
window.onload = typeWriter;

// Sidebar toggle
const sidebar = document.getElementById("sidebar");
const toggle = document.getElementById("sidebar-toggle");
const content = document.getElementById("content");
let sidebarOpen = false;

toggle.addEventListener("click", () => {
  sidebarOpen = !sidebarOpen;
  if (sidebarOpen) {
    sidebar.style.left = "0";
    toggle.innerHTML = "❮"; // left arrow
    content.classList.add("blurred");
  } else {
    sidebar.style.left = "-220px";
    toggle.innerHTML = "❯"; // right arrow
    content.classList.remove("blurred");
  }
});
