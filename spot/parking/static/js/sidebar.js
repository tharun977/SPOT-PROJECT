document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("toggleSidebar");
    const sidebar = document.getElementById("sidebar");
    const mainContent = document.getElementById("main-content");

    toggleBtn.addEventListener("click", function () {
        sidebar.classList.toggle("w-64");
        sidebar.classList.toggle("w-20");
        mainContent.classList.toggle("ml-64");
        mainContent.classList.toggle("ml-20");
    });
});
