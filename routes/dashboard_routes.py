from flask import render_template, redirect, request, session, flash
from logic.tratamiento_logic import TratamientoLogic
from logic.cita_logic import CitaLogic
from datetime import timedelta
import requests


class DashboardRoutes:
    @staticmethod
    def configure_routes(app, templateFolder=""):

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
                
                insertar = logic.insertCita(
                    user, correo, nombre, apellido, telefono, motivo, fecha, hora
                )
                
                return redirect("micuenta")

        @app.route("/micuenta")
        def micuenta():
            logic = CitaLogic()
            user = session["login_user"]
            currentCita1 = logic.getCitaByUser(user)
            print(currentCita1)
            url = f"{templateFolder}micuenta.html"
            return render_template(url, citaObj1 = currentCita1)
            