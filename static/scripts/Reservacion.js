const horariosPorSubservicio = {
    "Exfoliación Corporal": {
        "Lunes": ["09:00 - 10:00", "14:00 - 15:00", "17:00 - 18:00"],
        "Miércoles": ["09:00 - 10:00", "17:00 - 18:00", "20:00 - 21:00"],
        "Jueves": ["13:00 - 14:00", "19:00 - 20:00"],
        "Viernes": ["09:00 - 10:00", "17:00 - 18:00"],
        "Sábado": ["14:00 - 15:00"]
    },
    "Limpieza Facial Profunda": {
        "Lunes": ["10:00 - 11:00"],
        "Martes": ["18:00 - 19:00"],
        "Miércoles": ["20:00 - 21:00"],
        "Viernes": ["10:00 - 11:00"],
        "Sábado": ["16:00 - 17:00"]
    },
    "Depilación con Cera": {
        "Lunes": ["11:00 - 12:00"],
        "Viernes": ["11:00 - 12:00"]
    },
    "Masaje Relajante con Aromaterapia": {
        "Lunes": ["12:00 - 13:00"],
        "Jueves": ["16:00 - 17:00"],
        "Viernes": ["12:00 - 13:00"],
        "Sábado": ["18:00 - 19:00"]
    },
    "Envoltura de Algas o Barro": {
        "Martes": ["09:00 - 10:00", "14:00 - 15:00"],
        "Miércoles": ["18:00 - 19:00"],
        "Sábado": ["09:00 - 10:00"]
    },
    "Peeling Químico": {
        "Martes": ["10:00 - 11:00", "17:00 - 18:00"],
        "Miércoles": ["14:00 - 15:00"],
        "Jueves": ["17:00 - 18:00"],
        "Sábado": ["10:00 - 11:00"]
    },
    "Depilación Láser": {
        "Martes": ["11:00 - 12:00", "19:00 - 20:00"],
        "Miércoles": ["19:00 - 20:00"],
        "Viernes": ["19:00 - 20:00"],
        "Sábado": ["11:00 - 12:00"]
    },
    "Masaje Descontracturante": {
        "Martes": ["12:00 - 13:00"],
        "Miércoles": ["15:00 - 16:00"],
        "Viernes": ["20:00 - 21:00"],
        "Sábado": ["12:00 - 13:00"]
    },
    "Microdermoabrasión": {
        "Lunes": ["15:00 - 16:00"],
        "Martes": ["13:00 - 14:00", "19:00 - 20:00"],
        "Miércoles": ["10:00 - 11:00"],
        "Jueves": ["18:00 - 19:00"],
        "Sábado": ["15:00 - 16:00"]
    },
    "Depilación con Hilo": {
        "Martes": ["16:00 - 17:00"],
        "Miércoles": ["11:00 - 12:00"],
        "Jueves": ["15:00 - 16:00"]
    },
    "Masaje con Piedras Calientes": {
        "Lunes": ["16:00 - 17:00"],
        "Miércoles": ["12:00 - 13:00"],
        "Jueves": ["14:00 - 15:00"],
        "Sábado": ["20:00 - 21:00"]
    },
    "Tratamiento de Drenaje Linfático": {
        "Martes": ["15:00 - 16:00"],
        "Miércoles": ["13:00 - 14:00"],
        "Jueves": ["09:00 - 10:00"],
        "Viernes": ["14:00 - 15:00"],
        "Sábado": ["19:00 - 20:00"]
    },
    "Tratamiento con Ácido Hialurónico": {
        "Lunes": ["18:00 - 19:00"],
        "Miércoles": ["16:00 - 17:00"],
        "Jueves": ["10:00 - 11:00", "13:00 - 14:00"],
        "Viernes": ["13:00 - 14:00", "18:00 - 19:00"]
    },
    "Depilación con Crema Depilatoria": {
        "Martes": ["20:00 - 21:00"],
        "Jueves": ["11:00 - 12:00"],
        "Sábado": ["17:00 - 18:00"]
    },
    "Reflexología": {
        "Miércoles": ["17:00 - 18:00"],
        "Jueves": ["12:00 - 13:00", "20:00 - 21:00"]
    },
    "Exfoliación e Hidratación Profunda de Manos": {
        "Lunes": ["13:00 - 14:00"],
        "Miércoles": ["15:00 - 16:00"],
        "Viernes": ["16:00 - 17:00"],
        "Sábado": ["09:00 - 10:00"]
    },
    "Masaje de Manos": {
        "Martes": ["12:00 - 13:00"],
        "Jueves": ["18:00 - 19:00"],
        "Viernes": ["15:00 - 16:00"]
    },
    "Tratamiento de Parafina": {
        "Lunes": ["17:00 - 18:00"],
        "Miércoles": ["12:00 - 13:00"],
        "Viernes": ["14:00 - 15:00"]
    },
    "Manicura Completa": {
        "Martes": ["09:00 - 10:00"],
        "Jueves": ["16:00 - 17:00"],
        "Sábado": ["10:00 - 11:00"]
    },
    "Masaje de Reflexología de Pies": {
        "Lunes": ["20:00 - 21:00"],
        "Miércoles": ["18:00 - 19:00"],
        "Viernes": ["19:00 - 20:00"]
    }
};


function mostrarOpcionesSubservicio() {
    const servicioSeleccionado = document.getElementById("servicio").value;

    ["subservicio-corporal", "subservicio-facial", "subservicio-depilacion", "subservicio-manos", "subservicio-masaje"]
        .forEach(id => document.getElementById(id).style.display = "none");

    if (servicioSeleccionado) {
        document.getElementById(`subservicio-${servicioSeleccionado}`).style.display = "block";
    }

    configurarCalendario();
}

function obtenerSubservicioSeleccionado() {
    const servicioSeleccionado = document.getElementById("servicio").value;

    if (servicioSeleccionado) {
        const subservicioSelect = document.getElementById(`subservicio-${servicioSeleccionado}-select`);
        return subservicioSelect ? subservicioSelect.value : null;
    }
    return null;
}

function obtenerNombreDiaSemana(fecha) {
    const diasSemana = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"];
    return diasSemana[fecha.getUTCDay()];
}

function configurarCalendario() {
    flatpickr("#fecha", {
        dateFormat: "Y-m-d",
        locale: "es",
        onChange: function(selectedDates, dateStr) {
            const fechaSeleccionada = new Date(dateStr);
            const diaSemanaCapitalizado = obtenerNombreDiaSemana(fechaSeleccionada);

            const subservicioSeleccionado = obtenerSubservicioSeleccionado();
            if (subservicioSeleccionado) {
                actualizarHorarios(subservicioSeleccionado, diaSemanaCapitalizado);
            }
        }
    });
}

function actualizarHorarios(subservicio, diaSemana) {
    const horarioSelect = document.getElementById("hora");
    horarioSelect.innerHTML = "";

    if (horariosPorSubservicio[subservicio] && horariosPorSubservicio[subservicio][diaSemana]) {
        const horarios = horariosPorSubservicio[subservicio][diaSemana];
        horarios.forEach(hora => {
            const option = document.createElement("option");
            option.value = hora;
            option.text = hora;
            horarioSelect.appendChild(option);
        });
    } else {
        const option = document.createElement("option");
        option.text = "No hay horarios disponibles para este día";
        horarioSelect.appendChild(option);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    // Inicializa las opciones de subservicio y calendario en el inicio
    mostrarOpcionesSubservicio();
    configurarCalendario();

    // Actualiza los horarios cuando se cambia el subservicio
    ["subservicio-corporal-select", "subservicio-facial-select", "subservicio-depilacion-select", "subservicio-manos-select", "subservicio-masaje-select"]
        .forEach(id => {
            const element = document.getElementById(id);
            if (element) {
                element.addEventListener("change", () => {
                    const fechaSeleccionada = document.getElementById("fecha").value;
                    if (fechaSeleccionada) {
                        const fechaObj = new Date(fechaSeleccionada);
                        const diaSemana = obtenerNombreDiaSemana(fechaObj);
                        const subservicioSeleccionado = obtenerSubservicioSeleccionado();
                        if (subservicioSeleccionado) {
                            actualizarHorarios(subservicioSeleccionado, diaSemana);
                        }
                    }
                });
            }
        });
});
document.addEventListener("DOMContentLoaded", function () {
    const servicioSelect = document.getElementById("servicio");
    const calendarioDias = document.getElementById("calendario-dias");
    const calendarioTurnos = document.getElementById("calendario-turnos");

    servicioSelect.addEventListener("change", function () {
        const servicioSeleccionado = servicioSelect.value;
        if (servicioSeleccionado) {
            actualizarCalendarioPorDiaSemana(servicioSeleccionado);
        }
    });

    function actualizarCalendarioPorDiaSemana(servicio) {
        fetch(`/api/obtener_disponibilidad_semanal?servicio=${servicio}`)
            .then(response => response.json())
            .then(data => {
                const diasDisponibles = [];
                const diasOcupados = [];

                // Convertir la disponibilidad semanal en días de la semana
                Object.keys(data).forEach(diaSemana => {
                    const turnos = data[diaSemana];
                    if (turnos.ocupados < turnos.total_turnos) {
                        diasDisponibles.push(diaSemana);
                    } else {
                        diasOcupados.push(diaSemana);
                    }
                });

                configurarCalendarioDias(diasDisponibles, diasOcupados);
            });
    }

    function configurarCalendarioDias(diasDisponibles, diasOcupados) {
        flatpickr(calendarioDias, {
            dateFormat: "Y-m-d",
            locale: "es",
            inline: true,
            onDayCreate: function(dObj, dStr, fp, dayElem) {
                const diaSemana = dayElem.dateObj.toLocaleDateString("es-ES", { weekday: "long" });

                if (diasDisponibles.includes(diaSemana)) {
                    dayElem.style.backgroundColor = "green";
                    dayElem.style.color = "white";
                    dayElem.classList.add("disponible");
                } else if (diasOcupados.includes(diaSemana)) {
                    dayElem.style.backgroundColor = "red";
                    dayElem.style.color = "white";
                    dayElem.classList.add("ocupado");
                }
            },
            onChange: function(selectedDates, dateStr) {
                const diaSeleccionado = selectedDates[0].toLocaleDateString("es-ES", { weekday: "long" });
                mostrarTurnosDisponibles(diaSeleccionado);
            }
        });
    }

    function mostrarTurnosDisponibles(diaSemana) {
        fetch(`/api/obtener_disponibilidad_semanal?servicio=${servicioSelect.value}`)
            .then(response => response.json())
            .then(data => {
                calendarioTurnos.innerHTML = ''; // Limpiar el calendario de turnos
                const disponibilidad = data[diaSemana];

                if (disponibilidad && disponibilidad.ocupados < disponibilidad.total_turnos) {
                    const turnosDisponibles = disponibilidad.total_turnos - disponibilidad.ocupados;
                    for (let i = 1; i <= turnosDisponibles; i++) {
                        const option = document.createElement("div");
                        option.className = "turno-disponible";
                        option.textContent = `Turno ${i} disponible`;
                        calendarioTurnos.appendChild(option);
                    }
                } else {
                    const option = document.createElement("div");
                    option.className = "turno-ocupado";
                    option.textContent = "No hay turnos disponibles";
                    calendarioTurnos.appendChild(option);
                }
            });
    }
});





