async function cargarSubserviciosAsync() {
    const categorias = document.getElementById("servicio").value;
    if (!categorias) {
        console.error("No se seleccionó ninguna categoría.");
        return;
    }

    const subservicioSelect = document.getElementById("subservicio-corporal-select");

    try {
        const response = await fetch(`/api/obtener_subservicios?categorias=${categorias}`);
        const data = await response.json();

        subservicioSelect.innerHTML = '<option value="">Seleccione un tratamiento</option>';
        data.forEach(subservicio => {
            const option = document.createElement("option");
            option.value = subservicio.id;
            option.textContent = subservicio.nombre;
            subservicioSelect.appendChild(option);
        });
    } catch (error) {
        console.error("Error al cargar subservicios:", error);
    }
}

async function seleccionarServicioAsync(categoria, servicio) {
    const categoriaSelect = document.getElementById("servicio");
    const subservicioSelect = document.getElementById("subservicio-corporal-select");

    // Selección de la categoría
    for (let i = 0; i < categoriaSelect.options.length; i++) {
        if (categoriaSelect.options[i].text === categoria) {
            categoriaSelect.selectedIndex = i;
            break;
        }
    }
    await cargarSubserviciosAsync();
    for (let i = 0; i < subservicioSelect.options.length; i++) {
        if (subservicioSelect.options[i].text === servicio) {
            subservicioSelect.selectedIndex = i;
            break;
        }
    }
}

function limpiarSelector(selectorId) {
    const selector = document.getElementById(selectorId);
    selector.innerHTML = '<option value="">Seleccione una opción</option>';
}

// Limpiar selectores de horarios y subservicios cuando cambia la categoría o subservicio
document.getElementById("servicio").addEventListener("change", function() {
    limpiarSelector("hora");
    limpiarSelector("subservicio-corporal-select");
});

document.getElementById("subservicio-corporal-select").addEventListener("change", function() {
    limpiarSelector("hora");
});

document.addEventListener("DOMContentLoaded", function() {
    // Inicializa el calendario
    flatpickr("#fecha", {
        locale: "es",
        enableTime: false,
        dateFormat: "Y-m-d",
        minDate: "today",
        onChange: function(selectedDates, dateStr) {
            cargarHorarios(dateStr);
        }
    });

    // Añadir evento para el cambio de servicio
    document.getElementById("servicio").addEventListener("change", function() {
        const servicioId = this.value;
        console.log("Servicio ID seleccionado:", servicioId);
    });
});

// Función para cargar los horarios basados en la fecha y servicio seleccionado
async function cargarHorarios(fecha) {
    const servicioId = document.getElementById("servicio").value;
    const horaSelect = document.getElementById("hora");

    console.log("Servicio ID:", servicioId);
    console.log("Fecha seleccionada:", fecha);

    if (!servicioId) {
        horaSelect.innerHTML = '<option value="">Seleccione un servicio primero</option>';
        return;
    }

    // Limpiar las opciones actuales y mostrar mensaje de carga
    horaSelect.innerHTML = '<option value="">Cargando horarios...</option>';

    try {
        // Llamada al servidor para obtener horarios para el servicio y la fecha seleccionados
        const response = await fetch(`/api/obtener_horarios?servicio_id=${servicioId}&fecha=${fecha}`);

        // Verificar que la respuesta sea válida
        if (!response.ok) {
            throw new Error('Error en la respuesta del servidor: ' + response.statusText);
        }

        const data = await response.json(); // Procesar la respuesta como JSON
        console.log(data); // Para ver la respuesta del servidor

        // Limpiar y agregar las opciones de horario
        horaSelect.innerHTML = '<option value="">Seleccione un horario</option>';
        if (data.horarios && data.horarios.length > 0) {
            data.horarios.forEach(horario => {
                const option = document.createElement("option");
                option.value = horario.id;
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

document.getElementById("servicio").addEventListener("change", function() {
    document.getElementById("hora").innerHTML = '<option value="">Seleccione un horario</option>';
});

document.getElementById("subservicio-corporal-select").addEventListener("change", function() {
    document.getElementById("hora").innerHTML = '<option value="">Seleccione un horario</option>';
});

document.getElementById("servicio").addEventListener("change", function() {
    const tratamientoContainer = document.getElementById("tratamiento-container");
    const categoriaSeleccionada = this.value;
    if (categoriaSeleccionada) {
        tratamientoContainer.style.display = "block";
    } else {
        tratamientoContainer.style.display = "none";
    }
});

const currentDate = new Date();
let currentMonth = currentDate.getMonth();
let currentYear = currentDate.getFullYear();
let currentMonth2 = currentDate.getMonth() + 1;
let currentYear2 = currentDate.getFullYear();

const calendarBody = document.getElementById('calendarBody');
const currentMonthElement = document.getElementById('currentMonth');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

prevBtn.addEventListener('click', () => {
    currentMonth--;
    renderCalendar();
});
nextBtn.addEventListener('click', () => {
    currentMonth++;
    renderCalendar();
});

const occupiedDates = [
    new Date(currentYear, currentMonth, 5).toDateString(),
    new Date(currentYear, currentMonth, 12).toDateString(),
    new Date(currentYear, currentMonth, 20).toDateString(),
];

const daysOfWeek = ["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"];

function getDayClassName(date, isSecondCalendar = false) {
    const dateString = date.toDateString();
    const dayOfWeek = date.getDay();
    if (dayOfWeek === 0) {
        return 'sunday';
    }
    if (isSecondCalendar || occupiedDates.includes(dateString)) {
        return 'occupied';
    }
    return 'available';
}

function renderCalendar() {
    const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();
    const firstDayIndex = new Date(currentYear, currentMonth, 1).getDay();

    currentMonthElement.textContent = new Date(currentYear, currentMonth).toLocaleDateString('default', { month: 'long', year: 'numeric' });

    let days = daysOfWeek.map(day => `<div class="day-header">${day}</div>`).join('');

    for (let i = 0; i < firstDayIndex; i++) {
        days += `<div class="calendar-day"></div>`;
    }

    for (let i = 1; i <= daysInMonth; i++) {
        const date = new Date(currentYear, currentMonth, i);
        const className = getDayClassName(date);
        days += `<div class="calendar-day ${className}">${i}</div>`;
    }

    calendarBody.innerHTML = days;
}

const calendarBody2 = document.getElementById('calendarBody2');
const currentMonthElement2 = document.getElementById('currentMonth2');
const prevBtn2 = document.getElementById('prevBtn2');
const nextBtn2 = document.getElementById('nextBtn2');

prevBtn2.addEventListener('click', () => {
    currentMonth2--;
    renderSecondCalendar();
});

nextBtn2.addEventListener('click', () => {
    currentMonth2++;
    renderSecondCalendar();
});

function renderSecondCalendar() {
    const daysInMonth = new Date(currentYear2, currentMonth2 + 1, 0).getDate();
    const firstDayIndex = new Date(currentYear2, currentMonth2, 1).getDay();

    currentMonthElement2.textContent = new Date(currentYear2, currentMonth2).toLocaleDateString('default', { month: 'long', year: 'numeric' });

    let days = daysOfWeek.map(day => `<div class="day-header">${day}</div>`).join('');

    for (let i = 0; i < firstDayIndex; i++) {
        days += `<div class="calendar-day"></div>`;
    }

    for (let i = 1; i <= daysInMonth; i++) {
        const date = new Date(currentYear2, currentMonth2, i);
        const className = getDayClassName(date, true);
        days += `<div class="calendar-day ${className}">${i}</div>`;
    }

    calendarBody2.innerHTML = days;
}

renderCalendar();
renderSecondCalendar();

document.addEventListener('DOMContentLoaded', function() {
    const submitButton = document.querySelector('.submit-button');
    if (submitButton) {
        submitButton.addEventListener('click', function(event) {
            event.preventDefault();

            const reservaData = {
                nombre_cliente: document.getElementById('nombre').value,
                servicio: document.getElementById('servicio').value,
                fecha_reserva: document.getElementById('fecha').value,
                fecha_uso: document.getElementById('fecha').value
            };

            console.log("Datos de reserva enviados:", reservaData);

            fetch('/api/reserva', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(reservaData)
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

function cerrarConfirmacion() {
    document.getElementById('confirmationModal').style.display = 'none';
    window.location.reload();
}









