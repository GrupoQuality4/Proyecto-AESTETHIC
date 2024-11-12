document.getElementById("buscar-servicios").addEventListener("click", function() {
    const fecha = document.getElementById("fecha-busqueda").value;
    if (!fecha) {
        alert("Por favor selecciona una fecha.");
        return;
    }
    fetch(`/buscar_servicios_fecha?fecha=${fecha}`)
        .then(response => response.json())
        .then(data => {
            const resultadoDiv = document.getElementById("resultado-servicios");
            resultadoDiv.innerHTML = "";
            if (data.servicios.length > 0) {
                data.servicios.forEach(servicio => {
                    const servicioItem = document.createElement("div");
                    servicioItem.classList.add("servicio-item");
                    servicioItem.innerHTML = `
                        <h3>${servicio.titulo}</h3>
                        <p>${servicio.descripcion}</p>
                        <span class="price">$${servicio.precio}</span>
                    `;
                    resultadoDiv.appendChild(servicioItem);
                });
            } else {
                resultadoDiv.innerHTML = "<p>No hay servicios disponibles para la fecha seleccionada.</p>";
            }
        })
        .catch(error => console.error("Error:", error));
});
