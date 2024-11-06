document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.getElementById('registerForm');
    const successMessageRegistro = document.getElementById('successMessageRegistro'); // Elemento para mensaje de éxito
    const errorMessage = document.getElementById('errorMessage'); // Elemento para mensaje de error
    let errorTimeout;

    if (registerForm) {
        registerForm.addEventListener('submit', async (event) => {
            event.preventDefault(); // Prevenir el envío normal del formulario

            // Crear objeto de datos desde el formulario
            const formData = new FormData(registerForm);
            const formDataObj = {};
            formData.forEach((value, key) => (formDataObj[key] = value));

            try {
                // Hacer la solicitud al backend
                const response = await fetch('/register', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formDataObj)
                });

                if (response.ok) {
                    const result = await response.json();
                    if (result.success) {
                        // Mostrar mensaje de éxito
                        registerForm.style.display = 'none';
                        if (successMessageRegistro) {
                            successMessageRegistro.style.display = 'block';
                            successMessageRegistro.querySelector('p').textContent = result.message || '¡Registro exitoso!';
                        }
                        if (errorMessage) errorMessage.style.display = 'none'; // Ocultar mensaje de error
                    } else {
                        // Mostrar mensaje de error si el resultado no es exitoso
                        if (errorTimeout) clearTimeout(errorTimeout);
                        if (errorMessage) {
                            errorMessage.textContent = result.message || 'Hubo un error en el registro.';
                            errorMessage.style.display = 'block';
                            errorTimeout = setTimeout(() => {
                                errorMessage.style.display = 'none';
                            }, 3000);
                        }
                    }
                } else {
                    // Manejo del error en caso de que la respuesta del servidor no sea OK (status diferente de 200)
                    console.error('Error en la respuesta del servidor');
                    if (errorMessage) {
                        errorMessage.textContent = 'Error en la respuesta del servidor. Intente nuevamente.';
                        errorMessage.style.display = 'block';
                        if (errorTimeout) clearTimeout(errorTimeout);
                        errorTimeout = setTimeout(() => {
                            errorMessage.style.display = 'none';
                        }, 3000);
                    }
                }
            } catch (error) {
                // Manejo de errores de red o problemas en la solicitud
                console.error('Error en la solicitud:', error);
                if (errorMessage) {
                    errorMessage.textContent = 'Error en la solicitud. Verifique su conexión e intente de nuevo.';
                    errorMessage.style.display = 'block';
                    if (errorTimeout) clearTimeout(errorTimeout);
                    errorTimeout = setTimeout(() => {
                        errorMessage.style.display = 'none';
                    }, 3000);
                }
            }
        });
    } else {
        console.error('El formulario de registro no se encontró en el DOM.');
    }
});

function togglePassword(fieldId) {
    const passwordField = document.getElementById(fieldId);
    const fieldType = passwordField.getAttribute("type");
    
    if (fieldType === "password") {
        passwordField.setAttribute("type", "text");
    } else {
        passwordField.setAttribute("type", "password");
    }
}



