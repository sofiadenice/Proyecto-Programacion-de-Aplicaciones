from flask import render_template, redirect, request, session, flash
from logic.tratamiento_logic import TratamientoLogic
from logic.cita_logic import CitaLogic
from datetime import timedelta
import requests


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

                citaDic = {"user":user, "correo":correo, "nombre":nombre, "apellido":apellido, "telefono":telefono, "motivo":motivo, "fecha":fecha, "hora":hora}
                url2 = f"{templateFolder}pago.html"
                return render_template(url2, citaDic=citaDic)
        
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
                        return render_template(url)
                    elif dataJson['response'] == '05':
                        flash("Error de código de seguridad")
                        url = f"{templateFolder}cita.html"
                        return render_template(url)
                    elif dataJson['response'] == '07':
                        flash("Error de fecha de vencimiento")
                        url = f"{templateFolder}cita.html"
                        return render_template(url)
                    elif dataJson['response'] == '08':
                        flash("Error de nombre de titular")
                        url = f"{templateFolder}cita.html"
                        return render_template(url)
                    elif dataJson['response'] == '14':
                        flash("Error en el número de la tarjeta")
                        url = f"{templateFolder}cita.html"
                        return render_template(url)
                    elif dataJson['response'] == '41':
                        flash("Tarjeta está reportada como perdida")
                        url = f"{templateFolder}cita.html"
                        return render_template(url)
                    elif dataJson['response'] == '43':
                        flash("Tarjeta está reportada como robada")
                        url = f"{templateFolder}cita.html"
                        return render_template(url)
                    elif dataJson['response'] == '51':
                        flash("Saldo insuficiente")
                        url = f"{templateFolder}cita.html"
                        return render_template(url)
                    elif dataJson['response'] == '54':
                        flash("Tarjeta está inactiva")
                        url = f"{templateFolder}cita.html"
                        return render_template(url)
                    elif dataJson['response'] == '61':
                        flash("Excede el límite de la tarjeta")
                        url = f"{templateFolder}cita.html"
                        return render_template(url)
                    elif dataJson['response'] == 'QY':
                        flash("Tipo de tarjeta inválido")
                        url = f"{templateFolder}cita.html"
                        return render_template(url)
                    else:
                        flash("La cita no pudo ser agendada")
                        url = f"{templateFolder}cita.html"
                        return render_template(url)

        @app.route("/micuenta")
        def micuenta():
            logic = CitaLogic()
            user = session["login_user"]
            currentCita1 = logic.getCitaByUser(user)
            print(currentCita1)
            url = f"{templateFolder}micuenta.html"
            return render_template(url, citaObj1=currentCita1)
