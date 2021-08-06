const toggleButton = document.getElementsByClassName('menu-desplegable')[0]
const navbarLinks = document.getElementsByClassName('nav')[0]

w3.includeHTML()
toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active')
    })



function sendMail() {
    var nombre = document.getElementById("nombre").value
    var correo = document.getElementById("email").value
    var telefono = document.getElementById("phone").value
    var mensaje = document.getElementById("message").value
    cleanFormMail()
    //alert("Abriendo correo")
    
    window.open('mailto:clidente@gmail.com?subject='+ 'Consulta de ' + nombre +'&body=' + mensaje +'\x250D\u00250A'+'Correo de contacto: ' + correo +'\x250D\u00250A'+ 'Teléfono de contacto: ' + telefono);
}

function cleanFormMail() {
    document.getElementById("nombre").value = ""
    document.getElementById("email").value = ""
    document.getElementById("phone").value = ""
    document.getElementById("message").value = ""
}