(function() {
    'use strict';
    window.addEventListener('load', function() {
        var forms = document.getElementsByClassName('needs-validation');
        var validation = Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();

$(document).ready(function() {
    $('#login-trigger').click(function() {
        $(this).next('#login-content').slideToggle();
        $(this).toggleClass('active');
        if ($(this).hasClass('active')) $(this).find('span').html('&#x25B2;')
        else $(this).find('span').html('&#x25BC;')
    })
});


function verificarPasswords() {

    pass1 = document.getElementById('pass1');
    pass2 = document.getElementById('pass2');

    if (pass1.value != pass2.value) {
        document.getElementById("error").classList.add("mostrar");
        return false;
    } else {
        document.getElementById("error").classList.remove("mostrar");
        document.getElementById("ok").classList.remove("ocultar");
        document.getElementById("Registrar").disabled = true;
        setTimeout(function() {
            location.reload();
        }, 3000);
        return true;
    }
}

function verificar() {
    if ($("#nombre-input").val().trim().length > 0) {
        alert("usuario valido");
    } else {
        alert("El campo nombre contiene espacios y está vacío");
    }
}

function verificar() {
    if ($("#contra-input").val().trim().length > 0) {
        alert("usuario valido");
    } else {
        alert("El campo contrasena contiene espacios y está vacío");
    }
}

function addList() {
    alert("añadido al carrito");
    document.getElementById("nomemp").classList.remove("ocultar");
    setTimeout(function() {
        location.reload();
    }, 3000);
    return true;


}