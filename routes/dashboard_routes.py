from flask import render_template, redirect, request, session
from logic.tratamiento_logic import TratamientoLogic
from logic.cita_logic import CitaLogic
import requests


class DashboardRoutes:
    @staticmethod
    def configure_routes(app, templateFolder=""):

        @app.route("/inicio")
        def inicio():
            url = f"{templateFolder}inicio.html"
            return render_template(url)

        @app.route("/tratamientos")
        def tratamientos():
            logic = TratamientoLogic()
            session["tratamientoList"] = logic.selectAllTratamiento()
            url = f"{templateFolder}tratamientos.html"
            return render_template(url)

        @app.route("/about")
        def about():
            url = f"{templateFolder}about.html"
            return render_template(url)

        @app.route("/contacto")
        def contacto():
            url = f"{templateFolder}contacto.html"
            return render_template(url)

        @app.route("/cita", methods=["GET", "POST"])
        def cita():
            if request.method == "GET":
                if session["loggedIn"] is True:
                    url = f"{templateFolder}cita.html"
                    return render_template(url)
                else:
                    return render_template("login.html")
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
                return render_template("dashboard.html")