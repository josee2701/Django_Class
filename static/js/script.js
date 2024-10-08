// script.js

document.addEventListener('DOMContentLoaded', function() {
    var modal = document.getElementById('myModal');
    var btn = document.getElementById('openModal');
    var span = document.getElementsByClassName('close')[0];

    // Cuando el usuario hace clic en el botón, abre el modal
    btn.onclick = function() {
        modal.style.display = 'block';
    }

    // Cuando el usuario hace clic en la X, cierra el modal
    span.onclick = function() {
        modal.style.display = 'none';
    }

    // Cuando el usuario hace clic fuera del modal, cierra el modal
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
});
