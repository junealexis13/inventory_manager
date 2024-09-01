document.addEventListener('DOMContentLoaded', (event) => {
    const element = document.getElementById('message_alert');
    if (element) {
        setTimeout(() => {
            element.remove(); // Remove the element after 5 seconds
        }, 5000);
    }
});

