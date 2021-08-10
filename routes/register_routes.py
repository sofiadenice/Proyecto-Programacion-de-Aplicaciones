from flask import render_template, request, redirect, flash
from tools.recaptcha_helper import RecaptchaHelper
from logic.user_logic import UserLogic
from logic.dbInsertLogic import ValidarDatos
import bcrypt


class RegisterRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/register", methods=["GET", "POST"])
        def register():
            if request.method == "GET":
                return render_template("register.html")
            elif request.method == "POST":
                recHelper = RecaptchaHelper(request)
                if recHelper.validateRecaptcha():

                    # verificar que el usuario sea unico
                    logic = UserLogic()
                    username = request.form["user"]
                    result = logic.getRowByUser(username)
                    if len(result) == 0:

                        # verificar que el password sea igual al confirm password
                        password = request.form["password"]
                        confirmPassword = request.form["confpassword"]
                        useremail = request.form["email"]
                        if password == confirmPassword:

                            lista = [username, password, confirmPassword, useremail]
                            validar = ValidarDatos(lista)
                            result = validar.verificador()

                            if result:
                                # generar el salt , hacer el hash de la passw y insertar en bd
                                salt = bcrypt.gensalt(rounds=14)
                                strSalt = salt.decode("utf-8")
                                encPassword = password.encode("utf-8")
                                hashPassword = bcrypt.hashpw(encPassword, salt)
                                strPassword = hashPassword.decode("utf-8")
                                rows = logic.insertUser(
                                    username, useremail, strPassword, strSalt
                                )
                                return redirect("login")
                                # return "register validRecaptcha uniqueUser Passw==ConfPassw post"
                            else: 
                                flash("Los datos deben tener una longitud entre 3 y 45 caracteres")
                                return redirect("register")

                        else:
                            flash("No coinciden las contraseñas")
                            return redirect("register")
                    else:
                        flash("Ingresa otro usuario")
                        return redirect("register")
                else:
                    flash("Debe validar el Recaptcha")
                    return redirect("register")
