from flask import render_template, redirect, request, session
from logic.tratamiento_logic import TratamientoLogic
from logic.cita_logic import CitaLogic
import requests

class MainRoutes:
    @staticmethod
    def configure_routes(app, templateFolder=""):
        @app.route("/")
        def home():
            url = f"{templateFolder}inicioNotLogged.html"
            return render_template(url)

        @app.route("/main")
        def inicioNotLogged():
            url = f"{templateFolder}inicioNotLogged.html"
            return render_template(url)

        @app.route("/tratamientosNL")
        def tratamientosNL():
            logic = TratamientoLogic()
            session["tratamientoList"] = logic.selectAllTratamiento()
            url = f"{templateFolder}tratamientosNotLogged.html"
            return render_template(url)

        @app.route("/aboutNL")
        def aboutNL():
            url = f"{templateFolder}aboutNotLogged.html"
            return render_template(url)
        
