from flask import render_template, request, redirect, session, flash
from logic.user_logic import UserLogic
from logic.cita_logic import CitaLogic
from tools.recaptcha_helper import RecaptchaHelper
import bcrypt


class LogProcessRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/login", methods=["GET", "POST"])
        def login():
            if request.method == "GET":
                return render_template("login.html")
            elif request.method == "POST":
                recHelper = RecaptchaHelper(request)
                if recHelper.validateRecaptcha():                
                
                
                
                    logic = UserLogic()
                    username = request.form["user"]
                    password = request.form["password"]
                    userDict = logic.getRowByUser(username)

                    # validar si userDict no es vacio
                    if len(userDict) != 0:
                        # user existe
                        salt = userDict["salt"].encode("utf-8")
                        strPassword = password.encode("utf-8")
                        hashPassword = bcrypt.hashpw(strPassword, salt)
                        dbPassword = userDict["password"].encode("utf-8")
                        if hashPassword == dbPassword:
                            # se valido la password, se puede crear sesion y pasar al dashboard
                            session["login_user"] = username
                            session["loggedIn"] = True
                            session["id"] = userDict["id"]
                            session["role"] = userDict["role"]
                            session["email"] = userDict["user_email"]
                            return redirect("inicio")
                        else:
                            flash("Su contraseña es incorrecta")
                            return redirect("login")
                    else:
                        # user no existe
                        flash("Su usuario es incorrecto")
                        return redirect("login")
                else:
                    flash("Debe validar el Recaptcha")
                    return redirect("login")

        @app.route("/logout")
        def logout():
            session["loggedIn"] = False
            return redirect("main")


