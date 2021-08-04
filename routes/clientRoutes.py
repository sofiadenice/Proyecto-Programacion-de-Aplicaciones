from flask import render_template, redirect, request, session
from logic.tratamiento_logic import TratamientoLogic
from logic.cita_logic import CitaLogic
import requests

class ClientRoutes:
    @staticmethod
    def configure_routes(app, templateFolder=""):
        @app.route("/")
        def home():
            return render_template("index.html")