const toggleButton = document.getElementsByClassName('menu-desplegable')[0]
const navbarLinks = document.getElementsByClassName('nav')[0]

w3.includeHTML()
toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active')
    })


// Resize reCAPTCHA to fit width of container
// Since it has a fixed width, we're scaling
// using CSS3 transforms
// ------------------------------------------
// captchaScale = containerWidth / elementWidth

function scaleCaptcha(elementWidth) {
    // Width of the reCAPTCHA element, in pixels
    var reCaptchaWidth = 304;
    // Get the containing element's width
      var containerWidth = $('.container').width();
    
    // Only scale the reCAPTCHA if it won't fit
    // inside the container
    if(reCaptchaWidth > containerWidth) {
      // Calculate the scale
      var captchaScale = containerWidth / reCaptchaWidth;
      // Apply the transformation
      $('.g-recaptcha').css({
        'transform':'scale('+captchaScale+')'
      });
    }
  }
  
  $(function() { 

    //initialize scaling
    scaleCaptcha();

    //Update scaling on window resize
    //Uses jQuery throttle plugin to limit strain on the browser
    $(window).resize( $.throttle( 100, scaleCaptcha )
    );

  });






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