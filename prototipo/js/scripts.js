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






window.sr = ScrollReveal({ reset: true});

sr.reveal('.intro',{
duration: 1700

});


sr.reveal('.houses',{
    rotate: {x: 0, y: 80, z:0},
    duration:1800
});


sr.reveal('.cards',{

    duration:1800
});

sr.reveal('.caracters',{

    duration:1800
});



sr.reveal('.grifinoria_persona_section',{
    rotate: {x: 2, y: 80, z:2},
    duration:1800
});

sr.reveal('.sonserina_persona_section',{
    rotate: {x: 3, y: 80, z:3},
    duration:1800
});


sr.reveal('.lufa_lufa_persona_section',{
    rotate: {x: 3, y: 80, z:3},
    duration:1800
});


sr.reveal('.corvinal_persona_section',{
    rotate: {x: 3, y: 80, z:3},
    duration:1800
});

sr.reveal('.corvinal_persona_section',{
    rotate: {x: 3, y: 80, z:3},
    duration:1800
});


sr.reveal('.creatures',{
    rotate: {x: 3, y: 80, z:3},
    duration:1800
});

sr.reveal('.section_rodape',{
    rotate: {x: 3, y: 80, z:3},
    duration:1800
});

function togglePlay() {
    var musica = document.getElementById("minhaMusica");
    if (musica.paused) {
      musica.play();
    } else {
      musica.pause();
    }
}
  























