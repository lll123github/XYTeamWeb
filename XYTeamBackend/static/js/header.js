
function toggleSidebar() {
    const sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('hidden');
}
document.querySelector('.toggle-sidebar').addEventListener('click', toggleSidebar);