from flask import Flask
from routes.main_routes import MainRoutes
from routes.register_routes import RegisterRoutes
from routes.logprocess_routes import LogProcessRoutes
from routes.dashboard_routes import DashboardRoutes
from routes.adminRoutes import AdminRoutes
from routes.clientRoutes import ClientRoutes
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "Bal1s2e3c4r5e6t7k8e9y0+"
app.permanent_session_lifetime = timedelta(minutes=5)


mainTemplateFolder = "/notLogged/"
adminTemplateFolder = "/admin/"
clientTemplateFolder = "/client/"
dashboardTemplateFolder = "/logged/"



MainRoutes.configure_routes(app, templateFolder=mainTemplateFolder)
RegisterRoutes.configure_routes(app)
LogProcessRoutes.configure_routes(app)
DashboardRoutes.configure_routes(app, templateFolder=dashboardTemplateFolder)
AdminRoutes.configure_routes(app, templateFolder=adminTemplateFolder)
#ClientRoutes.configure_routes(app, templateFolder=clientTemplateFolder)

if __name__ == "__main__":
    app.run(debug=True)
