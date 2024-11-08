// Función para cargar categorías (solo si es necesario y tienes una API para obtenerlas)
async function cargarCategorias() {
    try {
        const response = await fetch('/api/obtener_categorias'); // Cambia esta URL según tu API
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

// Función para cargar subservicios basados en la categoría seleccionada
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

        // Muestra el contenedor del tratamiento solo si hay subservicios
        document.getElementById("tratamiento-container").style.display = subservicios.length > 0 ? 'block' : 'none';
        
    } catch (error) {
        console.error("Error al cargar subservicios:", error);
    }
}

// Función para manejar el día de la semana a partir de una fecha
function obtenerDiaDeLaSemana(fecha) {
    const diasSemana = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"];
    const date = new Date(fecha);
    return diasSemana[date.getDay()];
}

// Función para cargar horarios basados en el servicio y la fecha seleccionada
async function cargarHorarios(fecha) {
    const servicioId = document.getElementById("subservicio-corporal-select").value; // Cambiado a subservicio
    const horaSelect = document.getElementById("hora");

    console.log("Servicio ID:", servicioId);
    console.log("Fecha seleccionada:", fecha);

    if (!servicioId) {
        horaSelect.innerHTML = '<option value="">Seleccione un servicio primero</option>';
        return;
    }

    const diaSeleccionado = obtenerDiaDeLaSemana(fecha);
    console.log("Día de la semana seleccionado:", diaSeleccionado);

    // Limpiar las opciones actuales y mostrar mensaje de carga
    horaSelect.innerHTML = '<option value="">Cargando horarios...</option>';

    try {
        // Llamada al servidor para obtener horarios para el servicio y el día de la semana seleccionados
        const response = await fetch(`/api/obtener_horarios?servicio_id=${servicioId}&dia=${diaSeleccionado}`);

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

// Función para seleccionar servicio y subservicio
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

// Función para limpiar selectores
function limpiarSelector(selectorId) {
    const selector = document.getElementById(selectorId);
    selector.innerHTML = '<option value="">Seleccione una opción</option>';
}

// Limpiar selectores de horarios y subservicios cuando cambia la categoría o subservicio
document.getElementById("servicio").addEventListener("change", function() {
    limpiarSelector("hora");
    limpiarSelector("subservicio-corporal-select");
    cargarSubserviciosAsync(); // Cargar subservicios al cambiar la categoría
});

document.getElementById("subservicio-corporal-select").addEventListener("change", function() {
    limpiarSelector("hora");
});

// Inicializar el calendario y cargar categorías al cargar la página
document.addEventListener("DOMContentLoaded", function() {
    cargarCategorias(); // Llama a cargarCategorias al cargar la página

    // Inicializa el calendario
    flatpickr("#fecha", {
        locale: "es",
        enableTime: false,
        dateFormat: "Y-m-d",
        minDate: "today",
        onChange: function(selectedDates, dateStr) {
            const servicioId = document.getElementById("subservicio-corporal-select").value;
            cargarHorarios(dateStr);
        }
    });

    document.getElementById("servicio").addEventListener("change", function() {
        const categoriaId = this.value;
        console.log("Categoría ID seleccionada:", categoriaId);
    });
});

// Calendario 1
const currentDate = new Date();
let currentMonth = currentDate.getMonth();
let currentYear = currentDate.getFullYear();

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

// Calendario 2
let currentMonth2 = currentDate.getMonth() + 1;
let currentYear2 = currentDate.getFullYear();

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
                servicio: document.getElementById('subservicio-corporal-select').value, // Cambiado a subservicio
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

// Función para cerrar el modal de confirmación de reserva
function cerrarConfirmacion() {
    document.getElementById('confirmationModal').style.display = 'none';
    window.location.reload();
}








