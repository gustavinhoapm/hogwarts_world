const changeThemeBtn = document.querySelector('#change-theme');

function toggleDarkMode() {
    document.body.classList.toggle('dark');
}

function loadTheme() {
    const theme = localStorage.getItem('theme');
    if (theme === 'dark') {
        toggleDarkMode();
    }
}

loadTheme();

changeThemeBtn.addEventListener('change', () => {
    toggleDarkMode();

    localStorage.setItem('theme', document.body.classList.contains('dark') ? 'dark' : 'light');
});