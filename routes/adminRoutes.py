from flask import render_template, redirect, request, session
from logic.tratamiento_logic import TratamientoLogic
from logic.cita_logic import CitaLogic
import requests

class AdminRoutes:
    @staticmethod
    def configure_routes(app, templateFolder=""):

        @app.route("/citasCRUD")
        def citasCRUD():
            logic = CitaLogic()
            citaList = logic.selectAllCita()
            url = f"{templateFolder}citasCRUD.html"
            return render_template(url, citaList=citaList)

        @app.route("/citasForm", methods=["GET", "POST"])
        def citasForm():
            if request.method == "GET":
                currentCita = None
                url = f"{templateFolder}citasForm.html"
                if request.args.get("type") == "update":
                    logic = CitaLogic()
                    id = int(request.args.get("id"))
                    currentCita = logic.getCitaById(id)
                return render_template(url, citaObj=currentCita)

            elif request.method == "POST":
                if request.args.get("type") == "update":
                    logic = CitaLogic()
                    
                    id = request.form["idshow"]
                    motivo = request.form["motivo"]
                    fecha = request.form["fecha"]
                    hora = request.form["hora"]
                    
                    rows = logic.update(id, motivo, fecha, hora)

                """
                elif request.args.get("type") == "new":
                    logic = CitaLogic()

                    id = request.form["id"]
                    motivo = request.form["motivo"]
                    fecha = request.form["fecha"]
                    hora = request.form["hora"]

                    rows = logic.insert(size)
                """

                return redirect("citasCRUD")

        @app.route("/citasDELETE", methods=["POST"])
        def citasDELETE():
            if request.method == "POST":
                logic = CitaLogic()
                id = request.form["id"]
                rows = logic.deleteCita(id)
                return redirect("citasCRUD")

        @app.route("/addTratamientos")
        def addTratamientos():
            return render_template("citasCRUD")

        @app.route("/modTratamientos")
        def modTratamientos():
            return render_template("citasCRUD")

        @app.route("/addAdmin")
        def addAdmin():
            return render_template("citasCRUD")