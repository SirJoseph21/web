// Detectar el evento de scroll y agregar/eliminar la clase "scrolled"
document.addEventListener("scroll", function() {
    const body = document.body;
    const scrollPosition = window.scrollY;

    if (scrollPosition > 50) {
        body.classList.add("scrolled");
    } else {
        body.classList.remove("scrolled");
    }
});
