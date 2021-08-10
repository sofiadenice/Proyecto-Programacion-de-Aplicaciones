from flask import render_template, redirect, request, session, flash
from logic.tratamiento_logic import TratamientoLogic
from logic.cita_logic import CitaLogic
from logic.user_logic import UserLogic
from logic.addAdmin_logic import AddAdminLogic
from logic.dbInsertLogic import ValidarDatos
from datetime import timedelta
import requests
import bcrypt


class DashboardRoutes:
    @staticmethod
    def configure_routes(app, templateFolder=""):
        @app.route("/productos")
        def productos():
            if session.get("loggedIn") is None:
                session["loggedIn"] = False
            if session["loggedIn"] is True:
                url = "https://apicarbonohelio.herokuapp.com/local/0"
                response = requests.get(url)
                if response.status_code == 200:
                    dataJson = response.json()
                    url1 = f"{templateFolder}productos.html"
                    return render_template(url1, productList=dataJson)
            else:
                flash("Debe iniciar sesión para continuar")
                return redirect("login")

        @app.route("/inicio")
        def inicio():
            if session.get("loggedIn") is None:
                session["loggedIn"] = False
            if session["loggedIn"] is True:
                url = f"{templateFolder}inicio.html"
                return render_template(url)
            else:
                flash("Debe iniciar sesión para continuar")
                return redirect("login")

        @app.route("/tratamientos")
        def tratamientos():
            if session.get("loggedIn") is None:
                session["loggedIn"] = False
            if session["loggedIn"] is True:
                logic = TratamientoLogic()
                session["tratamientoList"] = logic.selectAllTratamiento()
                url = f"{templateFolder}tratamientos.html"
                return render_template(url)
            else:
                flash("Debe iniciar sesión para continuar")
                return redirect("login")

        @app.route("/about")
        def about():
            if session.get("loggedIn") is None:
                session["loggedIn"] = False
            if session["loggedIn"] is True:
                url = f"{templateFolder}about.html"
                return render_template(url)
            else:
                flash("Debe iniciar sesión para continuar")
                return redirect("login")

        @app.route("/contacto")
        def contacto():
            if session.get("loggedIn") is None:
                session["loggedIn"] = False
            if session["loggedIn"] is True:
                url = f"{templateFolder}contacto.html"
                return render_template(url)
            else:
                flash("Debe iniciar sesión para continuar")
                return redirect("login")

        @app.route("/cita", methods=["GET", "POST"])
        def cita():
            if session.get("loggedIn") is None:
                session["loggedIn"] = False
            if request.method == "GET":
                if session["loggedIn"] is True:
                    url = f"{templateFolder}cita.html"
                    return render_template(url)
                else:
                    flash("Debe iniciar sesión para continuar")
                    return redirect("login")
            elif request.method == "POST":
                logic = CitaLogic()

                fecha = request.form["fecha"]
                nombre = request.form["nombre"]
                apellido = request.form["apellido"]
                correo = request.form["correo"]
                telefono = request.form["telefono"]
                motivo = request.form["motivo"]
                hora = request.form["hora"]
                user = session["login_user"]

                citaList = [user, correo, nombre, apellido, telefono, motivo]
                validar = ValidarDatos(citaList)
                result = validar.verificador()

                if result:
                    citaDic = {"user":user, "correo":correo, "nombre":nombre, "apellido":apellido, "telefono":telefono, "motivo":motivo, "fecha":fecha, "hora":hora}
                    url2 = f"{templateFolder}pago.html"
                    return render_template(url2, citaDic=citaDic)
                else:
                    flash("Los datos deben tener una longitud entre 3 y 45 caracteres")
                    return redirect("cita")
        
        @app.route("/pago", methods=["GET", "POST"])
        def pago():
            if session.get("loggedIn") is None:
                session["loggedIn"] = False
            if request.method == "GET":
                if session["loggedIn"] is True:
                    url = f"{templateFolder}pago.html"
                    return render_template(url)
                else:
                    flash("Debe iniciar sesión para continuar")
                    return redirect("login")
            elif request.method == "POST":
                tarjeta = request.form["tarjeta"]
                codigo = request.form["codigo"]
                vencimiento = request.form["vencimiento"]
                titular = request.form["titular"]
                fecha = request.form["fecha"]
                nombre = request.form["nombre"]
                apellido = request.form["apellido"]
                correo = request.form["correo"]
                telefono = request.form["telefono"]
                motivo = request.form["motivo"]
                hora = request.form["hora"]
                user = request.form["user"]

                restapi     = "https://credit-card-auth-api-cerberus.herokuapp.com"
                endpoint    = "/verify"

                url = f"{restapi}{endpoint}"

                data = {
                    "name": titular,
                    "number": tarjeta,
                    "date": vencimiento,
                    "code": codigo,
                    "balance": 10 # el valor de la transaccion
                }

                response = requests.post(url, data=data)
                print(response)
                if response.status_code == 200:
                    dataJson = response.json()
                    if dataJson['response'] == '00':
                        logic = CitaLogic()
                        insertar = logic.insertCita(user, correo, nombre, apellido, telefono, motivo, fecha, hora)
                        flash("Cita agendada correctamente")
                        url = f"{templateFolder}cita.html"
                        return redirect("cita")
                    elif dataJson['response'] == '05':
                        flash("Error de código de seguridad")
                        url = f"{templateFolder}cita.html"
                        return redirect("cita")
                    elif dataJson['response'] == '07':
                        flash("Error de fecha de vencimiento")
                        url = f"{templateFolder}cita.html"
                        return redirect("cita")
                    elif dataJson['response'] == '08':
                        flash("Error de nombre de titular")
                        url = f"{templateFolder}cita.html"
                        return redirect("cita")
                    elif dataJson['response'] == '14':
                        flash("Error en el número de la tarjeta")
                        url = f"{templateFolder}cita.html"
                        return redirect("cita")
                    elif dataJson['response'] == '41':
                        flash("Tarjeta está reportada como perdida")
                        url = f"{templateFolder}cita.html"
                        return redirect("cita")
                    elif dataJson['response'] == '43':
                        flash("Tarjeta está reportada como robada")
                        url = f"{templateFolder}cita.html"
                        return redirect("cita")
                    elif dataJson['response'] == '51':
                        flash("Saldo insuficiente")
                        url = f"{templateFolder}cita.html"
                        return redirect("cita")
                    elif dataJson['response'] == '54':
                        flash("Tarjeta está inactiva")
                        url = f"{templateFolder}cita.html"
                        return redirect("cita")
                    elif dataJson['response'] == '61':
                        flash("Excede el límite de la tarjeta")
                        url = f"{templateFolder}cita.html"
                        return redirect("cita")
                    elif dataJson['response'] == 'QY':
                        flash("Tipo de tarjeta inválido")
                        url = f"{templateFolder}cita.html"
                        return redirect("cita")
                    else:
                        flash("La cita no pudo ser agendada")
                        url = f"{templateFolder}cita.html"
                        return redirect("cita")

        @app.route("/micuenta")
        def micuenta():
            logic = CitaLogic()
            user = session["login_user"]
            currentCita1 = logic.getCitaByUser(user)
            print(currentCita1)
            url = f"{templateFolder}micuenta.html"
            return render_template(url, citaObj1=currentCita1)
        
        @app.route("/contraForm", methods=["GET", "POST"])
        def contraForm():
            if request.method == "GET":
                url = f"{templateFolder}contraForm.html"
                return render_template(url)

            elif request.method == "POST":
                    
                    logic = UserLogic()
                    username = session["login_user"]
                    userDict = logic.getRowByUser(username)
                    id = session["id"]

                    contrasenaA = request.form["contrasenaVieja"]
                    passwordN = request.form["contrasenaNueva"]
                    confirmPassword = request.form["confirmarContra"]

                    # verificar que el password sea igual al confirm password
                    salt = userDict["salt"].encode("utf-8")
                    strPassword = contrasenaA.encode("utf-8")
                    hashPassword = bcrypt.hashpw(strPassword, salt)
                    dbPassword = userDict["password"].encode("utf-8")
                    if hashPassword == dbPassword:
                        
                    
                        if passwordN == confirmPassword:

                            lista = [passwordN, confirmPassword]
                            validar = ValidarDatos(lista)
                            result = validar.verificador()

                            if result:
                                # generar el salt , hacer el hash de la passw y insertar en bd
                                useremail = session["email"]
                                salt = bcrypt.gensalt(rounds=14)
                                strSalt = salt.decode("utf-8")
                                encPassword = passwordN.encode("utf-8")
                                hashPassword = bcrypt.hashpw(encPassword, salt)
                                strPassword = hashPassword.decode("utf-8")
                                logicAdd =  AddAdminLogic()
                                rows = logicAdd.updateUser(id, useremail, strPassword, strSalt)
                                return redirect("micuenta")
                                # return "register validRecaptcha uniqueUser Passw==ConfPassw post"

                            else:
                                flash("Los datos deben tener una longitud entre 3 y 45 caracteres")
                                return redirect("micuenta")
                            
                        else:
                            flash("Las contraseñas nuevas no coinciden")
                            return redirect("micuenta")

                    else:
                        flash("La contraseña actual no coincide")
                        return redirect("micuenta")

