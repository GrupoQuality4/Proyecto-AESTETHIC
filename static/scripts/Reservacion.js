function cargarSubservicios() {
    const categorias = document.getElementById("servicio").value;
    if (!categorias) {
        console.error("No se seleccionó ninguna categoría.");
        return;
    }

    const subservicioSelect = document.getElementById("subservicio-corporal-select");

    fetch(`/api/obtener_subservicios?categorias=${categorias}`)
        .then(response => response.json())
        .then(data => {
            subservicioSelect.innerHTML = '<option value="">Seleccione un tratamiento</option>';
            data.forEach(subservicio => {
                const option = document.createElement("option");
                option.value = subservicio.id;
                option.textContent = subservicio.nombre;
                subservicioSelect.appendChild(option);
            });
        })
        .catch(error => console.error("Error al cargar subservicios:", error));
}

function seleccionarServicio(categoria, servicio) {
    const categoriaSelect = document.getElementById("servicio");
    const subservicioSelect = document.getElementById("subservicio-corporal-select");

    for (let i = 0; i < categoriaSelect.options.length; i++) {
        if (categoriaSelect.options[i].text === categoria) {
            categoriaSelect.selectedIndex = i;
            break;
        }
    }
    cargarSubservicios();
    setTimeout(() => {
        for (let i = 0; i < subservicioSelect.options.length; i++) {
            if (subservicioSelect.options[i].text === servicio) {
                subservicioSelect.selectedIndex = i;
                break;
            }
        }
    }, 500);
}

document.addEventListener("DOMContentLoaded", function() {
    flatpickr("#fecha", {
        locale: "es",
        enableTime: false,
        dateFormat: "Y-m-d",
        minDate: "today"
    });
});






