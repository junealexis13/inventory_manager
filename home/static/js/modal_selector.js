// document.addEventListener('DOMContentLoaded', function() {
//     // Show selected items in the modal
//     document.querySelector('[data-toggle="modal"]').addEventListener('click', function() {
//         const selectedItems = [];
//         document.querySelectorAll('#deleteForm input[type="checkbox"]:checked').forEach(function(checkbox) {
//             selectedItems.push(checkbox.closest('label').textContent.trim());
//         });
//         const selectedItemsList = document.getElementById('selectedItemsList');
//         selectedItemsList.innerHTML = '';
//         selectedItems.forEach(function(item) {
//             const listItem = document.createElement('li');
//             listItem.textContent = item;
//             selectedItemsList.appendChild(listItem);
//         });
//     });

//     // Submit the form when the user confirms deletion
//     document.getElementById('confirmDelete').addEventListener('click', function() {
//         document.getElementById('deleteForm').submit();
//     });
// });

// Version 2
document.addEventListener('DOMContentLoaded', function() {
    // show selected items in the modal
    document.querySelector('[data-toggle="modal"]').addEventListener('click', function() {
        const selectedItems = [];
        document.querySelectorAll('.item_container').forEach(function(container) {
            const containerLabel = container.querySelector('p > label').textContent.trim();
            container.querySelectorAll('input[type="checkbox"]:checked').forEach(function(checkbox) {
                selectedItems.push({
                    label: containerLabel,
                    item: checkbox.closest('label').textContent.trim()
                });
            });
        });
        
        const selectedItemsList = document.getElementById('selectedItemsList');
        selectedItemsList.innerHTML = '';
        selectedItems.forEach(function(item) {
            const listItem = document.createElement('li');
            listItem.textContent = `${item.label} ${item.item}`;
            selectedItemsList.appendChild(listItem);
        });
    });

    // form submit then delete
    document.getElementById('confirmDelete').addEventListener('click', function() {
        document.getElementById('deleteForm').submit();
    });
});
