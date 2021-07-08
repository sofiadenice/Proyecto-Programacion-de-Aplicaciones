const toggleButton = document.getElementsByClassName('menu-desplegable')[0]
const navbarLinks = document.getElementsByClassName('nav')[0]

w3.includeHTML()
toggleButton.addEventListener('click', () => {
    navbarLinks.classList.toggle('active')
    })



/*
************* register functionality begin
*/

function registerNewUser() {
    var reg_user = document.getElementById("user_reg").value;
    var reg_password = document.getElementById("passw_reg").value;
    var reg_role = "client";

    //alert(reg_user);
    var userArray = [];

    if (localStorage.getItem("lUserArray") !== null) {
        userArray = JSON.parse(localStorage.getItem("lUserArray"));
    }

    var current_reg = {
        user: reg_user,
        password: reg_password,
        role: reg_role
    };

    userArray.push(current_reg);

    localStorage.setItem("lUserArray", JSON.stringify(userArray));

    window.location.href = "http://127.0.0.1:5000/login"
    // window.location.href = "https://proyecto-progra-2-final.herokuapp.com/login";
}

function agregarAdmin() {
    var reg_user = document.getElementById("nombreA").value;
    var reg_password = document.getElementById("contraA").value;
    var reg_role = "admin";

    //alert(reg_user);
    var userArray = [];

    if (localStorage.getItem("lUserArray") !== null) {
        userArray = JSON.parse(localStorage.getItem("lUserArray"));
    }

    var current_reg = {
        user: reg_user,
        password: reg_password,
        role: reg_role
    };

    userArray.push(current_reg);

    localStorage.setItem("lUserArray", JSON.stringify(userArray));

}
/*
************* login functionality begin
*/
function checkLogin() {

    var user = document.getElementById("user").value;
    var password = document.getElementById("passw").value;

    var userArray = JSON.parse(localStorage.getItem("lUserArray"));

    if (user !== null && user !== "") {
        if (password !== null && password !== "") {

            var canLogin = checkLoginInfo(user, password, userArray);
            if (canLogin === true) {
                //need a method to get the role and send it into createSessionUser below
                var role = getUserRole(user, password, userArray)
                createSessionUser(user, password, role)
                window.location.href = "http://127.0.0.1:5000/dashboard";
                //window.location.href = "https://proyecto-progra-2-final.herokuapp.com/dashboard";
            } else {
                alert("Usuario o contraseña no son correctos");
            }

        } else {
            alert("El campo de contraseña no debe estar vacío");
        }
    } else {
        alert("El campo de usuario no debe estar vacío");
    }

}

function checkLoginInfo(user, password, userArray) {
    if (userArray !== null && userArray.length > 0) {
        for (var i = 0; i < userArray.length; i++) {
            if (userArray[i].user === user && userArray[i].password === password) {
                return true;
            }
        }
    }
    return false;
}

function getUserRole(pUser, pPassword, pUserArray) {
    var role = ""
    if (pUserArray !== null && pUserArray.length > 0) {
        var length = pUserArray.length
        for (var i = 0; i < length; i++) {
            if (pUserArray[i].user === pUser && pUserArray[i].password === pPassword) {
                role = pUserArray[i].role
                break
            }
        }
    }
    return role
}

function createSessionUser(user, password, role) {
    var logged_user = {
        user: user,
        password: password,
        role: role
    };

    sessionStorage.setItem("loggedUser", JSON.stringify(logged_user));
}


if (window.location.href.includes("dashboard")) {
    //un if general para el dashboard y asi podemos poner todos los metodos que necesitemos
    //checkForValidLoginSession()
    //setUserNameOnDashboard()
    w3.includeHTML()
}

if (window.location.href.includes("registro")) {
    //un if general para el dashboard y asi podemos poner todos los metodos que necesitemos
    checkForValidLoginSession()
    setUserNameOnRegistro()
}

function checkForValidLoginSession() {
    /*
    tengo que ir a buscar el elemento wUserArray, si no esta vacio
    entonces dejo pasar al dashboard si no es el caso entonces debo redirigir
    hacia el login
    */

    if (sessionStorage.getItem("loggedUser") == null) {
        alert("Debe iniciar sesión para acceder a la página");
        window.location.href = "http://127.0.0.1:5000/login";
        //window.location.href = "https://proyecto-progra-2-final.herokuapp.com/login";
    }
}

function setUserNameOnDashboard() {
    var userArray = getCurrentLoggedUser()
    var currentUser = userArray.user
    var currentRole = userArray.role

    var userSpan = document.getElementById("user")
    userSpan.innerText = "Hello, " + currentRole + " " + currentUser

    //modifyDashboardForRole(currentRole)
}

function setUserNameOnRegistro() {
    var userArray = getCurrentLoggedUser()
    var currentUser = userArray.user
    var currentRole = userArray.role

    var userSpan = document.getElementById("user")
    userSpan.innerText = "Hello, " + currentRole + " " + currentUser

    modifyRegistroForRole(currentRole)
}

function getCurrentLoggedUser() {
    var currentLoggedUser = JSON.parse(sessionStorage.getItem("loggedUser"))
    return currentLoggedUser
}

function modifyRegistroForRole(pCurrentRole) {
    var add_admin = document.getElementById("admin")
    var add_client = document.getElementById("client")
    if (pCurrentRole === "admin") {
        //modifcar el dashboard para admin
        add_admin.style.display = "block"
        add_client.style.display = "none"
    } else {
        //modifcar el dashboard para client
        add_admin.style.display = "none"
        add_client.style.display = "block"
    }
}

function logout() {
    sessionStorage.removeItem("loggedUser")
    window.location.href = "http://127.0.0.1:5000/"
    //window.location.href = "https://proyecto-progra-2-final.herokuapp.com/";
}

function goToIndex() {
    window.location.href = "http://127.0.0.1:5000/"
    //window.location.href = "https://proyecto-progra-2-final.herokuapp.com/";
}

/*
************* dashboard functionality end
*/

/*
************* dashboard functionality add admin
*/
if (window.location.href.includes("registro")) {
    var currentLoggedUser = getCurrentLoggedUser()
    if (currentLoggedUser.role === "admin") {

        const elementToObserve = document.getElementById("admin")

        const observer = new MutationObserver(function () {
            var currentLoggedUser = getCurrentLoggedUser()
            loadAddDataFromAllUsers()
            observer.disconnect()
        });

        observer.observe(elementToObserve, { subtree: true, childList: true });
    }
}

if (window.location.href.includes("registro")) {
    var currentLoggedUser = getCurrentLoggedUser()
    if (currentLoggedUser.role === "admin") {

        const elementToObserve = document.getElementById("admin")

        const observer = new MutationObserver(function () {
            var currentLoggedUser = getCurrentLoggedUser()
            loadAddDataFromTratamiento()
            observer.disconnect()
        });

        observer.observe(elementToObserve, { subtree: true, childList: true });
    }
}

function loadAddDataFromAllUsers() {
    var addResultArray
    if (localStorage.getItem("lAddCitaArray") !== null) {
        addResultArray = JSON.parse(localStorage.getItem("lAddCitaArray"));
    }

    var userTableAdmin = document.getElementById("userTableAdmin")
    var row
    var index = 0;
    //var tableIndex = addResultArray

    for (var addResult of addResultArray) {
        row = userTableAdmin.insertRow(1)

        row.insertCell(0).innerHTML = addResult.user;
        row.insertCell(1).innerHTML = addResult.fecha;
        row.insertCell(2).innerHTML = addResult.nombre;
        row.insertCell(3).innerHTML = addResult.apellido;
        row.insertCell(4).innerHTML = addResult.correo;
        row.insertCell(5).innerHTML = addResult.telefono;
        row.insertCell(6).innerHTML = addResult.motivo;
        row.insertCell(7).innerHTML = addResult.hora;
        row.insertCell(8).innerHTML = "<button onclick='modifyOnElementByIndex(" + index + ")'>modify</button><input type='hidden' id='" + index + "'>";
        row.insertCell(9).innerHTML = "<button onclick='deleteElementByIndex(" + index + ")'>delete</button><input type='hidden' id='" + index + "'>";
        index++
    }
}

function deleteElementByIndex(pIndex) {
    //que es lo que implica eliminar un elemento?
    //1. quitarlo del local storage
    deleteElementFromLocalStorage(pIndex)
    //2. quitarlo de la tabla
    deleteElementFromTable(pIndex)

}

function deleteElementFromLocalStorage(pIndex) {
    var addResultArray = JSON.parse(localStorage.getItem("lAddCitaArray"))
    addResultArray.splice(pIndex, 1)
    localStorage.setItem("lAddCitaArray", JSON.stringify(addResultArray))
}

function deleteElementFromTable(pIndex) {
    var element = document.getElementById(pIndex)
    var parent = getElementParent(element, 3)
    var child = getElementParent(element, 2)
    parent.removeChild(child)
}

function modifyOnElementByIndex(pIndex) {
    var element = document.getElementById(pIndex)
    var parent = getElementParent(element, 2)
    console.log(parent.children)
    var children = parent.children
    children[1].innerHTML = "<input type='text' id='fecha" + pIndex + "' value='" + children[1].innerText + "'>"
    children[2].innerHTML = "<input type='text' id='nombre" + pIndex + "' value='" + children[2].innerText + "'>"
    children[3].innerHTML = "<input type='text' id='apellido" + pIndex + "' value='" + children[3].innerText + "'>"
    children[4].innerHTML = "<input type='text' id='correo" + pIndex + "' value='" + children[4].innerText + "'>"
    children[5].innerHTML = "<input type='text' id='telefono" + pIndex + "' value='" + children[5].innerText + "'>"
    children[6].innerHTML = "<input type='text' id='motivo" + pIndex + "' value='" + children[6].innerText + "'>"
    children[7].innerHTML = "<input type='text' id='hora" + pIndex + "' value='" + children[7].innerText + "'>"
    children[8].innerHTML = "<button onclick='modifyOffElementByIndex(" + pIndex + ",1)'>save</button><button onclick='modifyOffElementByIndex(" + pIndex + ",0)'>modify off</button><input type='hidden' id='" + pIndex + "'>"
}





/* ----------------------------------------------------------------*/
function modifyOffElementByIndex(pIndex, pSave) {
    var addResultArray
    if (localStorage.getItem("lAddCitaArray") !== null) {
        addResultArray = JSON.parse(localStorage.getItem("lAddCitaArray"));
    }

    var element = document.getElementById(pIndex)
    var parent = getElementParent(element, 2)
    var children = parent.children

    if(pSave===0){
        //modify off
        children[1].innerHTML = addResultArray[pIndex].fecha
        children[2].innerHTML = addResultArray[pIndex].nombre
        children[3].innerHTML = addResultArray[pIndex].apellido
        children[4].innerHTML = addResultArray[pIndex].correo
        children[5].innerHTML = addResultArray[pIndex].telefono
        children[6].innerHTML = addResultArray[pIndex].motivo
        children[7].innerHTML = addResultArray[pIndex].hora
        children[8].innerHTML = "<button onclick='modifyOnElementByIndex(" + pIndex + ")'>modify</button><input type='hidden' id='" + pIndex + "'>";

    } else {
        //save
        var input1 = document.getElementById("fecha"+pIndex).value
        var input2 = document.getElementById("nombre"+pIndex).value
        var input3 = document.getElementById("apellido"+pIndex).value
        var input4 = document.getElementById("correo"+pIndex).value
        var input5 = document.getElementById("telefono"+pIndex).value
        var input6 = document.getElementById("motivo"+pIndex).value
        var input7 = document.getElementById("hora"+pIndex).value
       

        addResultArray[pIndex].fecha = input1
        addResultArray[pIndex].nombre = input2
        addResultArray[pIndex].apellido = input3
        addResultArray[pIndex].correo = input4
        addResultArray[pIndex].telefono = input5
        addResultArray[pIndex].motivo = input6
        addResultArray[pIndex].hora = input7


        children[1].innerHTML = input1
        children[2].innerHTML = input2
        children[3].innerHTML = input3
        children[4].innerHTML = input4
        children[5].innerHTML = input5
        children[6].innerHTML = input6
        children[7].innerHTML = input7
        children[8].innerHTML = "<button onclick='modifyOnElementByIndex(" + pIndex + ")'>modify</button><input type='hidden' id='" + pIndex + "'>";

        localStorage.setItem("lAddCitaArray", JSON.stringify(addResultArray))
    }
}





/*------------------------------------------------------------------*/


function getElementParent(pElement, pGen) {
    var parent = pElement
    for (var i = 0; i < pGen; i++) {
        parent = parent.parentNode
    }
    return parent
}


/*
************* dashboard functionality add admin
*/


/*
************* dashboard functionality add client
*/
if (window.location.href.includes("registro")) {
    var currentLoggedUser = getCurrentLoggedUser()
    var currentUser = currentLoggedUser.user
    if (currentLoggedUser.role === "client") {

        const elementToObserve = document.getElementById("client")

        const observer = new MutationObserver(function () {
            loadCitaDataByUser(currentUser)
            observer.disconnect()
        });

        observer.observe(elementToObserve, { subtree: true, childList: true });
    }
}

function loadAddDataByUser(pCurrentUser) {
    var addResultArray
    if (localStorage.getItem("lAddResultArray") !== null) {
        addResultArray = JSON.parse(localStorage.getItem("lAddResultArray"));
    }

    var userTableClient = document.getElementById("userTableClient")
    var row

    for (var addResult of addResultArray) {
        if (addResult.user === pCurrentUser) {
            row = userTableClient.insertRow(1)

            row.insertCell(0).innerHTML = addResult.num1;
            row.insertCell(1).innerHTML = addResult.num2;
            row.insertCell(2).innerHTML = addResult.result;
        }
    }
}

function loadCitaDataByUser(pCurrentUser) {
    var citaArray
    if (localStorage.getItem("lAddCitaArray") !== null) {
        citaArray = JSON.parse(localStorage.getItem("lAddCitaArray"));
    } else {
        citaArray = []
    }

    var userTableClient = document.getElementById("userTableClient")
    var row

    for (var cita of citaArray) {
        if (cita.user === pCurrentUser) {
            row = userTableClient.insertRow(1)

            row.insertCell(0).innerHTML = cita.fecha;
            row.insertCell(1).innerHTML = cita.hora;
            row.insertCell(2).innerHTML = cita.motivo;
            
            
        }
    }
}

function agregarCita(){
    var fecha = document.getElementById("fecha").value
    var nombre = document.getElementById("name").value
    var apellido = document.getElementById("apellido").value
    var correo = document.getElementById("correo").value
    var telefono = document.getElementById("telefono").value
    var motivo = document.getElementById("motivo").value
    var horan = document.getElementById("hora").value
    var hora = ""
    if (horan == "hora1") {
        hora = "9:00 AM - 10:00 AM"
    } else if (horan == "hora2") {
        hora = "10:00 AM - 11:00 AM"
    } else if (horan == "hora3") {
        hora = "11:00 AM - 12:00 PM"
    } else if (horan == "hora4") {
        hora = "1:00 PM - 2:00 PM"
    } else if (horan == "hora5") {
        hora = "2:00 PM - 3:00 PM"
    } else if (horan == "hora6") {
        hora = "3:00 PM - 4:00 PM"
    } else if (horan == "hora7") {
        hora = "4:00 PM - 5:00 PM"
    } 
    
    cleanFormCita()
    //alert(fecha)
    addResultToCitaTable(fecha, nombre, apellido, correo, telefono, motivo, hora)
    addResultToCitaStorage(fecha, nombre, apellido, correo, telefono, motivo, hora)
    return
    //alert("Pausa")
}

function add() {
    var num1 = parseInt(document.getElementById("number1").value)
    var num2 = parseInt(document.getElementById("number2").value)
    var result = num1 + num2
    cleanForm()
    addResultToTable(num1, num2, result)
    addResultToStorage(num1, num2, result)

}

function cleanForm() {
    document.getElementById("number1").value = ""
    document.getElementById("number2").value = ""
}

function cleanFormCita() {
    document.getElementById("fecha").value = ""
    document.getElementById("name").value = ""
    document.getElementById("apellido").value = ""
    document.getElementById("correo").value = ""
    document.getElementById("telefono").value = ""
    document.getElementById("motivo").value = ""
}

function addResultToCitaTable(fecha, nombre, apellido, correo, telefono, motivo, hora) {
    
    var myTable = document.getElementById("userTableClient")

    var row = myTable.insertRow(1)

    row.insertCell(0).innerHTML = fecha;
    row.insertCell(1).innerHTML = hora;
    row.insertCell(2).innerHTML = motivo;

    document.getElementById("proximaCita").style.display = "block"

}

function addResultToTable(pNum1, pNum2, pResult) {
    var myTable = document.getElementById("userTableClient")

    var row = myTable.insertRow(1)

    row.insertCell(0).innerHTML = pNum1;
    row.insertCell(1).innerHTML = pNum2;
    row.insertCell(2).innerHTML = pResult;
}


function addResultToStorage(num1, num2, result) {
    var addResultArray = []

    //obtener el current logged user
    var currentLoggedUser = getCurrentLoggedUser()
    //console.log(currentLoggedUser.user)

    if (localStorage.getItem("lAddResultArray") !== null) {
        addResultArray = JSON.parse(localStorage.getItem("lAddResultArray"));
    }

    var current_add_result = {
        user: currentLoggedUser.user,
        num1: pNum1,
        num2: pNum2,
        result: pResult
    }

    addResultArray.push(current_add_result)
    localStorage.setItem("lAddResultArray", JSON.stringify(addResultArray));
}

function addResultToCitaStorage(fecha, nombre, apellido, correo, telefono, motivo, hora){
    var addCitaArray = []

    //obtener el current logged user
    var currentLoggedUser = getCurrentLoggedUser()
    //console.log(currentLoggedUser.user)

    if (localStorage.getItem("lAddCitaArray") !== null) {
        addCitaArray = JSON.parse(localStorage.getItem("lAddCitaArray"));
    }

    var current_add_cita = {
        user: currentLoggedUser.user,
        fecha: fecha,
        nombre: nombre,
        apellido: apellido,
        correo: correo,
        telefono: telefono,
        motivo: motivo,
        hora: hora
    }

    addCitaArray.push(current_add_cita)
    localStorage.setItem("lAddCitaArray", JSON.stringify(addCitaArray));
}

//Funcion para mostrar contenido de pestañas de HTML
function hideDivById(divId) {
    hideAllDivW3Includes()
    var element = document.getElementById(divId)
    if (element.style.display === "none") {
        element.style.display = "block"
    }
}

//Ocultar todo el contenido de pestañas de HTML
function hideAllDivW3Includes() {
    var elementArray = document.getElementsByName("pages")
    for (var element of elementArray) {
        element.style.display = "none"
    }
}

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
//Function for adding new treatments

function agregarTratamiento(){
    var nombre = document.getElementById("nombreT").value
    var descripcion = document.getElementById("descripcionT").value
    var imagen = document.getElementById("imagenT").value
    var imagenA = "<img src='"+imagen+"'>"
    
    cleanFormTratamientos()
    //alert(fecha)
    //addResultToTratamientoTable(nombre,descripcion, imagen)
    addResultToTratamientoStorage(nombre,descripcion, imagenA)
    return
    //alert("Pausa")
}
function cleanFormTratamientos() {
    document.getElementById("nombreT").value = ""
    document.getElementById("descripcionT").value = ""
    document.getElementById("imagenT").value = ""
}

/*function addResultToTratamientoTable(nombre,descripcion, imagen) {
    
    var myTable = document.getElementById("tableTratamientos")

    var row = myTable.insertRow(1)

    row.insertCell(0).innerHTML = nombre;
    row.insertCell(1).innerHTML = descripcion;
    row.insertCell(2).innerHTML = imagen;
    row.insertCell(3).innerHTML = "<button onclick='modifyOnElementByIndexT(" + index + ")'>modify</button><input type='hidden' id='" + index + "'>";
    row.insertCell(4).innerHTML = "<button onclick='deleteElementByIndexT(" + index + ")'>delete</button><input type='hidden' id='" + index + "'>";
        

}
*/
function addResultToTratamientoStorage(nombre,descripcion, imagen){
    
    var addTratamientoArray = []

    if (localStorage.getItem("lAddTratamientoArray") !== null) {
        addTratamientoArray = JSON.parse(localStorage.getItem("lAddTratamientoArray"));
    }

    var current_add_tratamiento = {
        
        nombreT: nombre,
        descripcionT: descripcion,
        imagenT: imagen
    }

    addTratamientoArray.push(current_add_tratamiento)
    localStorage.setItem("lAddTratamientoArray", JSON.stringify(addTratamientoArray));
}

function loadAddDataFromTratamiento() {
    
    var addTratamientoArray = []
    
    if (localStorage.getItem("lAddTratamientoArray") !== null) {
        addTratamientoArray = JSON.parse(localStorage.getItem("lAddTratamientoArray"));
    }

    var tableTratamientos = document.getElementById("tableTratamientos")
    var row
    var indexT = 0;
    //var tableIndex = addResultArray

    for (var addResult of addTratamientoArray) {
        row = tableTratamientos.insertRow(1)

        row.insertCell(0).innerHTML = "<span id= 'columna1"+indexT+"'>" + addResult.nombreT+"</span>";
        row.insertCell(1).innerHTML = "<span id= 'columna2"+indexT+"'>" + addResult.descripcionT+"</span>";
        row.insertCell(2).innerHTML = "<span id= 'columna3"+indexT+"'>" + addResult.imagenT +"</span>";
        row.insertCell(3).innerHTML = "<span id= 'columna4"+indexT+"'><button onclick='modifyOnElementByIndexT(" + indexT + ")'>modify</button><input type='hidden' id='" + indexT + "'></span>";
        row.insertCell(4).innerHTML = "<button onclick='deleteElementByIndexT(" + indexT + ")'>delete</button><input type='hidden' id= 'T"+indexT+"'>";
        indexT++
    }
}

function deleteElementByIndexT(pIndexT) {
    //que es lo que implica eliminar un elemento?
    //1. quitarlo del local storage
    deleteElementFromLocalStorageT(pIndexT)
    //2. quitarlo de la tabla
    deleteElementFromTableT(pIndexT)
    location = location

}

function deleteElementFromLocalStorageT(pIndexT) {
    var addResultArrayT = JSON.parse(localStorage.getItem("lAddTratamientoArray"))
    addResultArrayT.splice(pIndexT, 1)
    localStorage.setItem("lAddTratamientoArray", JSON.stringify(addResultArrayT))
}

function deleteElementFromTableT(pIndexT) {
    var addResultArrayT = JSON.parse(localStorage.getItem("lAddTratamientoArray"))
    var logArray = addResultArrayT.length
    var rowT = -pIndexT  + logArray + 1
    document.getElementById("tableTratamientos").deleteRow(rowT);    
    /*var element = document.getElementById(pIndexT)
    var parent = getElementParent(element, 3)
    var child = getElementParent(element, 2)
   parent.removeChildT(child) */
}

function modifyOnElementByIndexT(pIndexT) {

    var addResultArrayT = JSON.parse(localStorage.getItem("lAddTratamientoArray"))
    var logArray = addResultArrayT.length
    var rowT = -pIndexT  + logArray + 1

    var element = document.getElementById("tableTratamientos").rows[rowT]
    //var parent = getElementParent(element, 2)
    //console.log(parent.children)
    //var children = parent.children


    document.getElementById("columna1"+pIndexT).innerHTML = "<input type='text' id='nombreT" + pIndexT + "' value='" + document.getElementById("columna1"+pIndexT).innerHTML+ "'>"
    document.getElementById("columna2"+pIndexT).innerHTML = "<input type='text' id='descripcionT" + pIndexT + "' value='" + document.getElementById("columna2"+pIndexT).innerHTML + "'>"
    document.getElementById("columna3"+pIndexT).innerHTML = "<input type='text' id='imagenT" + pIndexT + "' value='" +     document.getElementById("columna3"+pIndexT).innerHTML+ "'>"
    document.getElementById("columna4"+pIndexT).innerHTML = "<button onclick='modifyOffElementByIndexT(" + pIndexT + ",1)'>save</button><button onclick='modifyOffElementByIndexT(" + pIndexT + ",0)'>modify off</button><input type='hidden' id='" + pIndexT + "'>"
}





/* ----------------------------------------------------------------*/
function modifyOffElementByIndexT(pIndexT, pSave) {
    var addResultArrayT
    if (localStorage.getItem("lAddTratamientoArray") !== null) {
        addResultArrayT = JSON.parse(localStorage.getItem("lAddTratamientoArray"));
    }

    var element = document.getElementById(pIndexT)
    var parent = getElementParent(element, 2)
    var children = parent.children

    if(pSave===0){
        //modify off
        document.getElementById("columna1"+pIndexT).innerHTML = addResultArrayT[pIndexT].nombreT
        document.getElementById("columna2"+pIndexT).innerHTML = addResultArrayT[pIndexT].descripcionT
        document.getElementById("columna3"+pIndexT).innerHTML = addResultArrayT[pIndexT].imagenT
        document.getElementById("columna4"+pIndexT).innerHTML = "<button onclick='modifyOnElementByIndexT(" + pIndexT + ")'>modify</button><input type='hidden' id='" + pIndexT + "'>";

    } else {
        //save
        var input1 = document.getElementById("nombreT"+pIndexT).value
        var input2 = document.getElementById("descripcionT"+pIndexT).value
        var input3 = document.getElementById("imagenT"+pIndexT).value
     
       

        addResultArrayT[pIndexT].nombreT = input1
        addResultArrayT[pIndexT].descripcionT = input2
        addResultArrayT[pIndexT].imagenT = input3
 


        document.getElementById("columna1"+pIndexT).innerHTML = input1
        document.getElementById("columna2"+pIndexT).innerHTML = input2
        document.getElementById("columna3"+pIndexT).innerHTML = input3
        document.getElementById("columna4"+pIndexT).innerHTML = "<button onclick='modifyOnElementByIndexT(" + pIndexT + ")'>modify</button><input type='hidden' id='"+ pIndexT + "'>";

        localStorage.setItem("lAddTratamientoArray", JSON.stringify(addResultArrayT))
    }
}

//------------------------------------------------------------------------------
function loadAddDataFromTratamientoClient() {

    var addTratamientoArray = []

    if (localStorage.getItem("lAddTratamientoArray") !== null) {
        addTratamientoArray = JSON.parse(localStorage.getItem("lAddTratamientoArray"));
    }

    var tableTratamientos = document.getElementById("tableTratamientos")
    var row
    var indexT = 0;
    //var tableIndex = addResultArray


    //var addResultArrayT = JSON.parse(localStorage.getItem("lAddTratamientoArray"))
    //var longT = addResultArrayT.length

    var x = document.getElementById("tableTratamientos").rows.length;

    if (x>1){
        for (var i=1; i < x; i++ ){
            document.getElementById("tableTratamientos").deleteRow(i)
        }
    }
    for (var addResult of addTratamientoArray) {
        row = tableTratamientos.insertRow(1)

        row.insertCell(0).innerHTML = "<span id= 'columna1"+indexT+"'>" + addResult.nombreT+"</span>";
        row.insertCell(1).innerHTML = "<span id= 'columna2"+indexT+"'>" + addResult.descripcionT+"</span>";
        row.insertCell(2).innerHTML = "<span id= 'columna3"+indexT+"'>" + addResult.imagenT +"</span>";
        indexT++
    }
} 