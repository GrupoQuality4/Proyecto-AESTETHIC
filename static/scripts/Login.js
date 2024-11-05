document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        const flashMessages = document.querySelectorAll('.flash-message.danger');
        flashMessages.forEach(function (message) {
            message.style.opacity = '0';
            setTimeout(() => { message.remove(); }, 500);
        });
    }, 3000);
});
