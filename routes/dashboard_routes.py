from flask import render_template, redirect, request
import requests


class DashboardRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/dashboard")
        def dashboard():
            return render_template("dashboard.html")

        
        @app.route("/inicio")
        def inicio():
            return render_template("inicio.html")


        @app.route("/productos")
        def productos():
            return render_template("productos.html")


        @app.route("/cita")
        def cita():
            return render_template("cita.html")


        @app.route("/contacto")
        def contacto():
            return render_template("contacto.html")


        @app.route("/registro")
        def registro():
            return render_template("registro.html")


        @app.route("/about")
        def about():
            return render_template("about.html")



        @app.route("/add_cli")
        def addcli():
            return render_template("addcli.html")


        @app.route("/add_adm")
        def addadm():
            return render_template("addadm.html")



        @app.route("/dashboard/city/<int:id>")
        def city(id):
            url = f"http://localhost:23512/city/{id}"
            response = requests.get(url)
            if response.status_code == 200:
                dataJson = response.json()
                return render_template("city.html", id=id, city=dataJson)
            else:
                return redirect("dashboard")

        @app.route("/dashboard/country/<int:id>")
        def country(id):
            url = f"http://localhost:23512/city/{id}"
            response = requests.post(url)
            if response.status_code == 200:
                dataJson = response.json()
                return render_template("country.html", cityList=dataJson)
            else:
                return redirect("dashboard")

        @app.route("/dashboard/city/create", methods=["GET", "POST"])
        def cityCreate():
            if request.method == "GET":
                return render_template("cityCreate.html")
            elif request.method == "POST":
                url = f"http://localhost:23512/city/0"
                data = {
                    "Name": request.form["name"],
                    "CountryCode": request.form["countrycode"],
                    "District": request.form["district"],
                    "Population": int(request.form["population"]),
                }
                response = requests.put(url, data=data)
                if response.status_code == 200:
                    dataJson = response.json()
                    # return f"rowsAffected by create: {dataJson['rowsAffected']}"
                    return render_template(
                        "nonQuery.html",
                        message=dataJson,
                        type="create",
                    )
                else:
                    return redirect("dashboard")

        @app.route("/dashboard/city/modify", methods=["GET", "POST"])
        def cityModify():
            if request.method == "GET":
                return render_template("cityModify.html")
            elif request.method == "POST":
                cityId = int(request.form["cityid"])
                url = f"http://localhost:23512/city/{cityId}"
                data = {
                    "Name": request.form["name"],
                    "CountryCode": request.form["countrycode"],
                    "District": request.form["district"],
                    "Population": int(request.form["population"]),
                }
                response = requests.patch(url, data=data)
                if response.status_code == 200:
                    dataJson = response.json()
                    # return f"rowsAffected by modify: {dataJson['rowsAffected']}"
                    return render_template(
                        "nonQuery.html",
                        message=dataJson,
                        type="modify",
                    )
                else:
                    return redirect("dashboard")

        @app.route("/dashboard/city/delete", methods=["GET", "POST"])
        def cityDelete():
            if request.method == "GET":
                return render_template("cityDelete.html")
            elif request.method == "POST":
                cityId = int(request.form["cityid"])
                url = f"http://localhost:23512/city/{cityId}"
                response = requests.delete(url)
                if response.status_code == 200:
                    dataJson = response.json()
                    # return f"rowsAffected by delete: {dataJson['rowsAffected']}"
                    return render_template(
                        "nonQuery.html",
                        message=dataJson,
                        type="delete",
                    )
                else:
                    return redirect("dashboard")
