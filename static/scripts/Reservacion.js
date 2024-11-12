async function cargarCategorias() {
    try {
        const response = await fetch('/api/obtener_categorias');
        const categorias = await response.json();
        
        const categoriaSelect = document.getElementById("servicio");
        categoriaSelect.innerHTML = '<option value="">Seleccione una categoría</option>';
        
        categorias.forEach(categoria => {
            const option = document.createElement("option");
            option.value = categoria.id;
            option.textContent = categoria.nombre;
            categoriaSelect.appendChild(option);
        });
        
    } catch (error) {
        console.error("Error al cargar categorías:", error);
    }
}

async function cargarSubserviciosAsync() {
    const categoriaId = document.getElementById("servicio").value;
    if (!categoriaId) {
        console.error("No se seleccionó ninguna categoría.");
        return;
    }

    const subservicioSelect = document.getElementById("subservicio-corporal-select");

    try {
        const response = await fetch(`/api/obtener_subservicios?categorias=${categoriaId}`);
        const subservicios = await response.json();

        subservicioSelect.innerHTML = '<option value="">Seleccione un tratamiento</option>';
        subservicios.forEach(subservicio => {
            const option = document.createElement("option");
            option.value = subservicio.id;
            option.textContent = subservicio.nombre;
            subservicioSelect.appendChild(option);
        });

        document.getElementById("tratamiento-container").style.display = subservicios.length > 0 ? 'block' : 'none';
        
    } catch (error) {
        console.error("Error al cargar subservicios:", error);
    }
}

function obtenerDiaDeLaSemana(fecha) {
    const diasSemana = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"];
    const date = new Date(fecha);
    return diasSemana[date.getUTCDay()];
}

async function cargarHorarios(fecha) {
    const servicioId = document.getElementById("subservicio-corporal-select").value;
    const horaSelect = document.getElementById("hora");

    if (!servicioId) {
        horaSelect.innerHTML = '<option value="">Seleccione un servicio primero</option>';
        return;
    }

    const [day, month, year] = fecha.split("-");
    const formattedDate = `${year}-${month}-${day}`;
    const diaSeleccionado = obtenerDiaDeLaSemana(formattedDate);

    horaSelect.innerHTML = '<option value="">Cargando horarios...</option>';

    try {
        const response = await fetch(`/api/obtener_horarios?servicio_id=${servicioId}&dia=${diaSeleccionado}`);
        if (!response.ok) throw new Error('Error en la respuesta del servidor: ' + response.statusText);

        const data = await response.json();
        horaSelect.innerHTML = '<option value="">Seleccione un horario</option>';

        if (data.horarios && data.horarios.length > 0) {
            data.horarios.forEach(horario => {
                const option = document.createElement("option");
                option.value = horario.hora_inicio;
                option.textContent = `${horario.hora_inicio} - ${horario.hora_fin}`;
                horaSelect.appendChild(option);
            });
        } else {
            horaSelect.innerHTML = '<option value="">No hay horarios disponibles</option>';
        }
    } catch (error) {
        console.error("Error al cargar horarios:", error);
        horaSelect.innerHTML = '<option value="">Error al cargar horarios</option>';
    }
}

function limpiarSelector(selectorId) {
    const selector = document.getElementById(selectorId);
    selector.innerHTML = '<option value="">Seleccione una opción</option>';
}

document.addEventListener("DOMContentLoaded", function() {
    cargarCategorias();

    // Configuración de flatpickr para el campo de fecha
    flatpickr("#fecha", {
        locale: "es",
        enableTime: false,
        dateFormat: "d-m-Y",
        minDate: "today",
        onChange: function(selectedDates, dateStr) {
            cargarHorarios(dateStr);
        }
    });

    document.getElementById("servicio").addEventListener("change", function() {
        limpiarSelector("hora");
        limpiarSelector("subservicio-corporal-select");
        cargarSubserviciosAsync();
        console.log("Categoría ID seleccionada:", this.value);
    });

    document.getElementById("subservicio-corporal-select").addEventListener("change", function() {
        limpiarSelector("hora");
    });

    const submitButton = document.querySelector('.submit-button');
    if (submitButton) {
        submitButton.addEventListener('click', function(event) {
            event.preventDefault();

            // Convertir la fecha a formato ISO antes de enviar al backend
            const fechaReserva = document.getElementById('fecha').value;
            const [day, month, year] = fechaReserva.split("-");
            const fechaReservaFormatoISO = `${year}-${month}-${day}`;

            const reservaData = {
                nombre_cliente: document.getElementById('nombre').value,
                servicio: document.getElementById('subservicio-corporal-select').value,
                fecha_reserva: fechaReservaFormatoISO,
                fecha_uso: fechaReservaFormatoISO,
                hora_turno: document.getElementById('hora').value
            };

            console.log("Datos de reserva enviados:", reservaData);

            fetch('/api/reserva', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(reservaData),
                credentials: 'same-origin'
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    document.getElementById('confirmationModal').style.display = 'flex';
                } else {
                    alert(data.error || 'Hubo un problema con la reserva. Intente nuevamente.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Ocurrió un error al procesar su reserva. Intente nuevamente más tarde.');
            });
        });
    } else {
        console.error("El botón con clase 'submit-button' no se encontró en el DOM.");
    }
});

function mostrarConfirmacion() {
    document.getElementById("confirmationModal").classList.add("show");
}

function cerrarConfirmacion() {
    document.getElementById("confirmationModal").classList.remove("show");
    window.location.href = carritoUrl;
}
