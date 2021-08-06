from flask import render_template, redirect, request, session, flash
from logic.tratamiento_logic import TratamientoLogic
from logic.cita_logic import CitaLogic
from logic.addAdmin_logic import AddAdminLogic
from logic.user_logic import UserLogic
import requests
import bcrypt


class AdminRoutes:
    @staticmethod
    def configure_routes(app, templateFolder=""):
        @app.route("/proveedor")
        def proveedor():
            if session.get("loggedIn") is None:
                session["loggedIn"] = False
            if session["loggedIn"] is True:
                url = "https://apicarbonohelio.herokuapp.com/nonlocal/0"
                response = requests.get(url)
                if response.status_code == 200:
                    dataJson = response.json()
                    url1 = f"{templateFolder}proveedor.html"
                    return render_template(url1, proveedorList=dataJson)
            else:
                flash("Debe iniciar sesión para continuar")
                return redirect("login")

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
                    citaObj = currentCita
                return render_template(url, citaObj=citaObj)

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

        @app.route("/tratamientosCRUD")
        def tratamientosCRUD():
            logic = TratamientoLogic()
            tratamientosList1 = logic.selectAllTratamiento()
            url = f"{templateFolder}tratamientosCRUD.html"
            return render_template(url, tratamientoList=tratamientosList1)

        @app.route("/tratamientosForm", methods=["GET", "POST"])
        def tratamientosForm():
            if request.method == "GET":
                currentTratamiento = None
                url = f"{templateFolder}tratamientosForm.html"
                if request.args.get("type") == "update":
                    logic = TratamientoLogic()
                    id = int(request.args.get("id"))
                    currentTratamiento = logic.getTratamientoById(id)
                return render_template(url, tratamientoObj=currentTratamiento)

            elif request.method == "POST":
                if request.args.get("type") == "update":
                    logic = TratamientoLogic()

                    id = request.form["idshow"]
                    nombre = request.form["nombre"]
                    descripcion = request.form["descripcion"]
                    imagen = request.form["imagen"]

                    rows = logic.updateTratamiento(id, nombre, descripcion, imagen)

                elif request.args.get("type") == "new":
                    logic = TratamientoLogic()

                    nombre = request.form["nombre"]
                    descripcion = request.form["descripcion"]
                    imagen = request.form["imagen"]
                    rows = logic.insertTratamiento(nombre, descripcion, imagen)

                return redirect("tratamientosCRUD")

        @app.route("/tratamientosDELETE", methods=["POST"])
        def tratamientosDELETE():
            if request.method == "POST":
                logic = TratamientoLogic()
                id = request.form["id"]
                rows = logic.deleteTratamiento(id)
                return redirect("tratamientosCRUD")

        @app.route("/addAdminCRUD")
        def addAdminCRUD():
            logic = AddAdminLogic()
            AddAdminList = logic.selectAllAddAdmin()
            url = f"{templateFolder}addAdminCRUD.html"
            return render_template(url, AddAdminList=AddAdminList)

        @app.route("/addAdminForm", methods=["GET", "POST"])
        def addAdminForm():
            if request.method == "GET":
                currentAddAdmin = None
                url = f"{templateFolder}addAdminForm.html"
                if request.args.get("type") == "update":
                    logic = AddAdminLogic()
                    id = int(request.args.get("id"))
                    currentAddAdmin = logic.getAdminById(id)
                return render_template(url, addAdminObj=currentAddAdmin)

            elif request.method == "POST":
                if request.args.get("type") == "update":
                    logicAdd = AddAdminLogic()

                    id = request.form["idshow"]
                    user_name = request.form["user_name"]
                    user_email = request.form["user_email"]
                    password = request.form["password"]
                    confPassword = request.form["confpassword"]

                    # verificar que el password sea igual al confirm password
                    password = request.form["password"]
                    confirmPassword = request.form["confpassword"]
                    if password == confirmPassword:

                        # generar el salt , hacer el hash de la passw y insertar en bd
                        useremail = request.form["user_email"]
                        salt = bcrypt.gensalt(rounds=14)
                        strSalt = salt.decode("utf-8")
                        encPassword = password.encode("utf-8")
                        hashPassword = bcrypt.hashpw(encPassword, salt)
                        strPassword = hashPassword.decode("utf-8")
                        rows = logicAdd.updateUser(id, useremail, strPassword, strSalt)
                        return redirect("addAdminCRUD")
                        # return "register validRecaptcha uniqueUser Passw==ConfPassw post"

                    else:
                        flash("No se ha podido ingresar el nuevo administrador1")
                        return redirect("addAdminCRUD")

                elif request.args.get("type") == "new":
                    logicAdd = AddAdminLogic()

                    user_name = request.form["user_name"]
                    user_email = request.form["user_email"]
                    password = request.form["password"]
                    confPassword = request.form["confpassword"]

                    logic = UserLogic()
                    username = request.form["user_name"]
                    result = logic.getRowByUser(username)
                    if len(result) == 0:

                        # verificar que el password sea igual al confirm password
                        password = request.form["password"]
                        confirmPassword = request.form["confpassword"]
                        if password == confirmPassword:

                            # generar el salt , hacer el hash de la passw y insertar en bd
                            useremail = request.form["user_email"]
                            salt = bcrypt.gensalt(rounds=14)
                            strSalt = salt.decode("utf-8")
                            encPassword = password.encode("utf-8")
                            hashPassword = bcrypt.hashpw(encPassword, salt)
                            strPassword = hashPassword.decode("utf-8")
                            rows = logicAdd.insertAdminUser(
                                username, useremail, strPassword, strSalt
                            )
                            return redirect("addAdminCRUD")
                            # return "register validRecaptcha uniqueUser Passw==ConfPassw post"

                        else:
                            flash("No se ha podido ingresar el nuevo administrador")
                            return redirect("addAdminForm")
                    else:
                        flash("No se ha podido ingresar el nuevo administrador")
                        return redirect("addAdminForm")
                flash("No se ha podido ingresar el nuevo administrador")
                return redirect("addAdminForm")

        @app.route("/addAdminDELETE", methods=["POST"])
        def addAdminDELETE():
            if request.method == "POST":
                logic = AddAdminLogic()
                id = request.form["id"]
                rows = logic.deleteUser(id)
                return redirect("addAdminCRUD")