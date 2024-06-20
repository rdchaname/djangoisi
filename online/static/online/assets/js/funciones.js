function mostrarErrores(idformulario, errores) {
    const campos_con_errores = Object.keys(errores)

    // reseteando los mensajes de error
    const formulario = document.getElementById(idformulario);
    const campos_formulario = formulario.elements;
    for (let i = 0; i < campos_formulario.length; i++) {
        campos_formulario[i].classList.remove('is-invalid')
    }

    // se muestren los errores
    campos_con_errores.map(function (item) {
        const campo = $('#' + idformulario + ' [name=' + item + ']');
        if (campo.length) {
            campo.addClass('is-invalid');
            let div_error = $('#div_error_' + idformulario + '_' + item);
            if (div_error.length) {
                const mensajes_error = errores[item] // array
                let lista_errores = '';
                mensajes_error.map(function (mensaje) {
                    lista_errores = lista_errores + `<li>${mensaje}</li>`
                })
                div_error.html(`<ul>${lista_errores}</ul>`)
            } else {
                const mensajes_error = errores[item] // array
                let lista_errores = '';
                mensajes_error.map(function (mensaje) {
                    lista_errores = lista_errores + `<li>${mensaje}</li>`
                })
                div_error = `<div id='div_error_${idformulario}_${item}' class="invalid-feedback">
                                  <ul>${lista_errores}</ul>
                              </div>`
                campo.parent().append(div_error);
            }
        }
    });
}


function limpiarErrores(idformulario) {
    // reseteando los mensajes de error
    const formulario = document.getElementById(idformulario);
    const campos_formulario = formulario.elements;
    for (let i = 0; i < campos_formulario.length; i++) {
        campos_formulario[i].classList.remove('is-invalid')
    }
}
