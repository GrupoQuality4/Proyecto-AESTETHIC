document.addEventListener('DOMContentLoaded', () => {
    const registerForm = document.getElementById('registerForm');
    const successMessageRegistro = document.getElementById('successMessageRegistro'); // Agrega esta línea
    const errorMessage = document.getElementById('errorMessage');
    let errorTimeout;

    registerForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const formData = new FormData(registerForm);
        const formDataObj = {};
        formData.forEach((value, key) => (formDataObj[key] = value));

        try {
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
                    registerForm.style.display = 'none';
                    successMessageRegistro.style.display = 'block'; // Modifica esta línea
                    errorMessage.style.display = 'none';
                } else {
                    if (errorTimeout) clearTimeout(errorTimeout);
                    errorMessage.textContent = result.message || 'Hubo un error en el registro.';
                    errorMessage.style.display = 'block';
                    errorTimeout = setTimeout(() => {
                        errorMessage.style.display = 'none';
                    }, 3000);
                }
            } else {
                console.error('Error en la respuesta del servidor');
            }
        } catch (error) {
            console.error('Error en la solicitud:', error);
        }
    });
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



