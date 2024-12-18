document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('feedback-form');

    if (form) {
        form.addEventListener('submit', async function(event) {
            event.preventDefault();

            const formData = new FormData(form);
            const response = await fetch('/feedback', {
                method: 'POST',
                body: formData,
                headers: {
                    'Accept': 'application/json'
                }
            });

            const existingMessages = document.querySelectorAll('.feedback-section .alert');
            existingMessages.forEach(msg => msg.remove());

            if (response.ok) {
                const result = await response.json();
                displayMessage('success', result.message);
                form.reset();
            } else {
                const errorResult = await response.json();
                displayMessage('error', errorResult.detail || 'Ocorreu um erro ao enviar o feedback.');
            }
        });
    }

    function displayMessage(type, text) {
        const messageContainer = document.querySelector('.feedback-section');
        if (messageContainer) {
            const alertDiv = document.createElement('div');
            alertDiv.classList.add('alert', type);
            alertDiv.textContent = text;
            messageContainer.insertBefore(alertDiv, form);

            setTimeout(() => {
                alertDiv.classList.add('fade-out');
                alertDiv.addEventListener('transitionend', () => {
                    alertDiv.remove();
                });
            }, 3000);
        }
    }
});
