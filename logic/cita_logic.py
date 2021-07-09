from core.pyba_logic import PybaLogic


class CitaLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def selectAllCita(self):
        database = self.createDatabaseObj()
        sql = "SELECT * FROM clidente.cita"
        result = database.executeQuery(sql)
        return result

    def insertCita(self, userName, userEmail, nombre, apellido, telefono, motivo, fecha, hora):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `clidente`.`cita` "
            + "(`id`, `user`, `nombre`, `apellido`, `correo`, `telefono`, `motivo`, `fecha`, `hora`) "
            + f"VALUES (0,'{userName}','{nombre}','{apellido}','{userEmail}','{telefono}','{motivo}','{fecha}','{hora}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateCita(self, id, userName, userEmail, nombre, apellido, telefono, motivo, fecha, hora):
        database = self.createDatabaseObj()
        sql = ("UPDATE `clidente`.`cita` SET "
            + f"`id` = {id}, "
            + f"`user` = '{userName}', "
            + f"`nombre` = '{nombre}', "
            + f"`apellido` = '{apellido}', "
            + f"`correo` = '{userEmail}', "
            + f"`telefono` = '{telefono}', "
            + f"`motivo` = '{motivo}', "
            + f"`fecha` = '{fecha}', "
            + f"`hora` = '{hora}', "
            + f"WHERE `id` = {id};")

    def deleteCita(self, id):
        database = self.createDatabaseObj()
        sql = (f"DELETE FROM `clidente`.`cita` WHERE id={id};")
        rows = database.executeNonQueryRows(sql)
        return rows
