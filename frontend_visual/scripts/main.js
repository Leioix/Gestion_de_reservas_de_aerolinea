document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");

    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Evita que la página se recargue

        const origen = document.getElementById("origen").value;
        const destino = document.getElementById("destino").value;
        const fecha = document.getElementById("fecha").value;

        if (origen && destino && fecha) {
            alert(`Buscando vuelos de ${origen} a ${destino} el ${fecha}`);
        } else {
            alert("Por favor, complete todos los campos.");
        }
    });
});
