// Static JavaScript file (static/js/scripts.js)

document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete-btn');

    deleteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const confirmDeletion = confirm("Are you sure you want to delete?");
            if (!confirmDeletion) {
                event.preventDefault(); // Prevent the deletion if not confirmed
            }
        });
    });
});
