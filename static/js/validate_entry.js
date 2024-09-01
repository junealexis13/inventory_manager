document.addEventListener('DOMContentLoaded', function() {
    function toggleDeleteButton() {
        const checkboxes = document.querySelectorAll('input[type="checkbox"]');
        const deleteButton = document.querySelector('.btn-danger[data-toggle="modal"]');
        const anyChecked = Array.from(checkboxes).some(checkbox => checkbox.checked);
        console.log("Any checkbox checked:", anyChecked);
        deleteButton.disabled = !anyChecked;
    }

    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', toggleDeleteButton);
    });
});
