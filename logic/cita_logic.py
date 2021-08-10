from core.pyba_logic import PybaLogic


class CitaLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def selectAllCita(self):
        database = self.createDatabaseObj()
        sql = "SELECT * FROM cita"
        result = database.executeQuery(sql)
        return result

    def getCitaById(self, id):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM cita WHERE id={id};"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result[0]
        else:
            return []
    
    def getCitaByUser(self, user):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM cita WHERE user='{user}';"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result
        else:
            return []






    def insertCita(self, userName, userEmail, nombre, apellido, telefono, motivo, fecha, hora):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `cita` "
            + "(`id`, `user`, `nombre`, `apellido`, `correo`, `telefono`, `motivo`, `fecha`, `hora`) "
            + f"VALUES (0,'{userName}','{nombre}','{apellido}','{userEmail}','{telefono}','{motivo}','{fecha}','{hora}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateCita(self, id, userName, userEmail, nombre, apellido, telefono, motivo, fecha, hora):
        database = self.createDatabaseObj()
        sql = ("UPDATE `cita` SET "
            + f"`id` = {id}, "
            + f"`user` = '{userName}', "
            + f"`nombre` = '{nombre}', "
            + f"`apellido` = '{apellido}', "
            + f"`correo` = '{userEmail}', "
            + f"`telefono` = '{telefono}', "
            + f"`motivo` = '{motivo}', "
            + f"`fecha` = '{fecha}', "
            + f"`hora` = '{hora}',"
            + f"WHERE `id` = {id};")
        rows = database.executeNonQueryRows(sql)
        return rows

    def update(self, id, motivo, fecha, hora, estado):
        database = self.createDatabaseObj()
        sql = ("UPDATE `cita` SET "
            + f"`id` = {id}, "
            + f"`motivo` = '{motivo}', "
            + f"`fecha` = '{fecha}', "
            + f"`hora` = '{hora}', "
            + f"`estado` = '{estado}'"
            + f" WHERE `id` = {id};")
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteCita(self, id):
        database = self.createDatabaseObj()
        sql = (f"DELETE FROM `cita` WHERE id={id};")
        rows = database.executeNonQueryRows(sql)
        return rows

    
