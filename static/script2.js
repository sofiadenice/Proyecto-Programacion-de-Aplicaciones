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
                window.location.href = "http://localhost:5000/dashboard";
                //window.location.href = "http://heroku:5000/dashboard";
            } else {
                alert("user or password are not correct");
            }

        } else {
            alert("password must not be empty");
        }
    } else {
        alert("user must not be empty");
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

/*
************* login functionality end 
*/


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

    window.location.href = "http://localhost:5000/login"
    //window.location.href = "http://heroku:5000/login";
}

/*
************* register functionality end
*/


/*
************* dashboard functionality begin
*/



if (window.location.href.includes("dashboard")) {
    //un if general para el dashboard y asi podemos poner todos los metodos que necesitemos
    checkForValidLoginSession()
    setUserNameOnDashboard()
    w3.includeHTML()
}

function checkForValidLoginSession() {
    /*
    tengo que ir a buscar el elemento wUserArray, si no esta vacio
    entonces dejo pasar al dashboard si no es el caso entonces debo redirigir
    hacia el login
    */

    if (sessionStorage.getItem("loggedUser") == null) {
        window.location.href = "http://localhost:5000/login"
        //window.location.href = "http://heroku:5000/login";
    }
}

function setUserNameOnDashboard() {
    var userArray = getCurrentLoggedUser()
    var currentUser = userArray.user
    var currentRole = userArray.role

    var userSpan = document.getElementById("user")
    userSpan.innerText = "Hello, " + currentRole + " " + currentUser

    modifyDashboardForRole(currentRole)
}

function getCurrentLoggedUser() {
    var currentLoggedUser = JSON.parse(sessionStorage.getItem("loggedUser"))
    return currentLoggedUser
}

function modifyDashboardForRole(pCurrentRole) {
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
    window.location.href = "http://localhost:5000/"
    //window.location.href = "http://heroku:5000/";
}

/*
************* dashboard functionality end
*/

/*
************* dashboard functionality add admin
*/
if (window.location.href.includes("dashboard")) {
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

function loadAddDataFromAllUsers() {
    var addResultArray
    if (localStorage.getItem("lAddResultArray") !== null) {
        addResultArray = JSON.parse(localStorage.getItem("lAddResultArray"));
    }

    var userTableAdmin = document.getElementById("userTableAdmin")
    var row
    var index = 0;
    //var tableIndex = addResultArray

    for (var addResult of addResultArray) {
        row = userTableAdmin.insertRow(1)

        row.insertCell(0).innerHTML = addResult.user;
        row.insertCell(1).innerHTML = addResult.num1;
        row.insertCell(2).innerHTML = addResult.num2;
        row.insertCell(3).innerHTML = addResult.result;
        row.insertCell(4).innerHTML = "<button onclick='modifyOnElementByIndex(" + index + ")'>modify</button><input type='hidden' id='" + index + "'>";
        row.insertCell(5).innerHTML = "<button onclick='deleteElementByIndex(" + index + ")'>delete</button><input type='hidden' id='" + index + "'>";
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
    var addResultArray = JSON.parse(localStorage.getItem("lAddResultArray"))
    addResultArray.splice(pIndex, 1)
    localStorage.setItem("lAddResultArray", JSON.stringify(addResultArray))
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
    children[1].innerHTML = "<input type='number' id='inpNum" + pIndex + "' value='" + children[1].innerText + "'>"
    children[2].innerHTML = "<input type='number' id='inpNum" + pIndex + "' value='" + children[2].innerText + "'>"
    children[4].innerHTML = "<button onclick='modifyOffElementByIndex(" + pIndex + ",1)'>save</button><button onclick='modifyOffElementByIndex(" + pIndex + ",0)'>modify off</button><input type='hidden' id='" + pIndex + "'>"
}

function modifyOffElementByIndex(pIndex, pSave) {

}

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
if (window.location.href.includes("dashboard")) {
    var currentLoggedUser = getCurrentLoggedUser()
    var currentUser = currentLoggedUser.user
    if (currentLoggedUser.role === "client") {

        const elementToObserve = document.getElementById("client")

        const observer = new MutationObserver(function () {
            loadAddDataByUser(currentUser)
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

function addResultToTable(pNum1, pNum2, pResult) {
    var myTable = document.getElementById("userTableClient")

    var row = myTable.insertRow(1)

    row.insertCell(0).innerHTML = pNum1;
    row.insertCell(1).innerHTML = pNum2;
    row.insertCell(2).innerHTML = pResult;
}

function addResultToStorage(pNum1, pNum2, pResult) {
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

/*
************* dashboard functionality add client
*/
