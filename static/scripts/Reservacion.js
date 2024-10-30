const horariosPorSubservicio = {
    "Exfoliación corporal": {
        "Lunes": ["09:00 - 10:00", "14:00 - 15:00", "17:00 - 18:00"],
        "Miércoles": ["09:00 - 10:00", "17:00 - 18:00", "20:00 - 21:00"],
        "Jueves": ["13:00 - 14:00", "19:00 - 20:00"],
        "Viernes": ["09:00 - 10:00", "17:00 - 18:00"],
        "Sábado": ["14:00 - 15:00"]
    },
    "Limpieza facial profunda": {
        "Lunes": ["10:00 - 11:00"],
        "Martes": ["18:00 - 19:00"],
        "Miércoles": ["20:00 - 21:00"],
        "Viernes": ["10:00 - 11:00"],
        "Sábado": ["16:00 - 17:00"]
    },
    "Depilación con cera": {
        "Lunes": ["11:00 - 12:00"],
        "Viernes": ["11:00 - 12:00"]
    },
    "Masaje relajante con aromaterapia": {
        "Lunes": ["12:00 - 13:00"],
        "Jueves": ["16:00 - 17:00"],
        "Viernes": ["12:00 - 13:00"],
        "Sábado": ["18:00 - 19:00"]
    },
    "Envoltura de algas o barro": {
        "Martes": ["09:00 - 10:00", "14:00 - 15:00"],
        "Miércoles": ["18:00 - 19:00"],
        "Sábado": ["09:00 - 10:00"]
    },
    "Peeling químico": {
        "Martes": ["10:00 - 11:00", "17:00 - 18:00"],
        "Miércoles": ["14:00 - 15:00"],
        "Jueves": ["17:00 - 18:00"],
        "Sábado": ["10:00 - 11:00"]
    },
    "Depilación láser": {
        "Martes": ["11:00 - 12:00", "19:00 - 20:00"],
        "Miércoles": ["19:00 - 20:00"],
        "Viernes": ["19:00 - 20:00"],
        "Sábado": ["11:00 - 12:00"]
    },
    "Masaje descontracturante": {
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
    "Depilación con hilo": {
        "Martes": ["16:00 - 17:00"],
        "Miércoles": ["11:00 - 12:00"],
        "Jueves": ["15:00 - 16:00"]
    },
    "Masaje con piedras calientes": {
        "Lunes": ["16:00 - 17:00"],
        "Miércoles": ["12:00 - 13:00"],
        "Jueves": ["14:00 - 15:00"],
        "Sábado": ["20:00 - 21:00"]
    },
    "Tratamiento de drenaje linfático": {
        "Martes": ["15:00 - 16:00"],
        "Miércoles": ["13:00 - 14:00"],
        "Jueves": ["09:00 - 10:00"],
        "Viernes": ["14:00 - 15:00"],
        "Sábado": ["19:00 - 20:00"]
    },
    "Tratamiento con ácido hialurónico": {
        "Lunes": ["18:00 - 19:00"],
        "Miércoles": ["16:00 - 17:00"],
        "Jueves": ["10:00 - 11:00", "13:00 - 14:00"],
        "Viernes": ["13:00 - 14:00", "18:00 - 19:00"]
    },
    "Depilación con crema depilatoria": {
        "Martes": ["20:00 - 21:00"],
        "Jueves": ["11:00 - 12:00"],
        "Sábado": ["17:00 - 18:00"]
    },
    "Reflexología": {
        "Miércoles": ["17:00 - 18:00"],
        "Jueves": ["12:00 - 13:00", "20:00 - 21:00"]
    }
};

function mostrarOpcionesSubservicio() {
    document.getElementById("subservicio-corporal").style.display = "none";

    const servicioSeleccionado = document.getElementById("servicio").value;
    if (servicioSeleccionado === "corporal") {
        document.getElementById("subservicio-corporal").style.display = "block";
    }

    configurarCalendario();
}
function obtenerSubservicioSeleccionado() {
    if (document.getElementById("subservicio-corporal").style.display === "block") {
        return document.getElementById("subservicio-corporal-select").value;
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
        onChange: function(selectedDates, dateStr, instance) {
            const fechaSeleccionada = new Date(dateStr);
            const diaSemanaCapitalizado = obtenerNombreDiaSemana(fechaSeleccionada);

            const subservicioSeleccionado = obtenerSubservicioSeleccionado();
            console.log("Subservicio seleccionado:", subservicioSeleccionado);
            console.log("Día de la semana seleccionado:", diaSemanaCapitalizado);

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



