// static/js/main.js
document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Manejo Automático de Mensajes (Django Messages) -> SweetAlert2
    const messageContainer = document.getElementById('django-messages');
    if (messageContainer) {
        const messages = JSON.parse(messageContainer.textContent || "[]");
        messages.forEach(msg => {
            // Mapeo básico de Tags Django a iconos SweetAlert2
            let iconType = 'info';
            if (msg.tags.includes('success')) iconType = 'success';
            if (msg.tags.includes('error')) iconType = 'error';
            if (msg.tags.includes('warning')) iconType = 'warning';

            Swal.fire({
                title: iconType.charAt(0).toUpperCase() + iconType.slice(1),
                text: msg.message,
                icon: iconType,
                confirmButtonColor: 'var(--accent-purple)',
                background: 'var(--bg-surface)',
                color: 'var(--text-primary)'
            });
        });
    }

    // 2. SweetAlert2 para botones de Borrar (Confirmación Preventiva)
    const deleteButtons = document.querySelectorAll('.btn-delete-confirm');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const formObj = this.closest('form');
            if(formObj) {
                Swal.fire({
                    title: '¿Estás seguro?',
                    text: '¡No podrás revertir esto!',
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: 'var(--accent-red)',
                    cancelButtonColor: 'var(--border-color)',
                    confirmButtonText: 'Sí, borrar',
                    cancelButtonText: 'Cancelar',
                    background: 'var(--bg-surface)',
                    color: 'var(--text-primary)'
                }).then((result) => {
                    if (result.isConfirmed) {
                        formObj.submit();
                    }
                });
            }
        });
    });

});
