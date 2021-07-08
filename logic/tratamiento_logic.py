from core.pyba_logic import PybaLogic


class TratamientoLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def selectAllTratamiento(self):
        database = self.createDatabaseObj()
        sql = "SELECT * FROM clidente.tratamiento"
        result = database.executeQuery(sql)
        return result

    def insertTratamiento(self, nombre, descripcion, imagen):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `tratamiento` "
            + "(`id`, `nombre`, `descripcion`, `imagen`) "
            + f"VALUES (0,'{nombre}','{descripcion}','{imagen}';"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateTratamiento(self, id, nombre, descripcion, imagen):
        database = self.createDatabaseObj()
        sql = ("UPDATE `clidente`.`cita` SET "
            + f"`id` = {id}, "
            + f"`nombre` = '{nombre}', "
            + f"`descripcion` = '{descripcion}', "
            + f"`imagen` = '{imagen}', "
            + f"WHERE `id` = {id};")

    def deleteTratamineto(self, id):
        database = self.createDatabaseObj()
        sql = (f"DELETE FROM `clidente`.`tratamiento` WHERE id={id};")
        rows = database.executeNonQueryRows(sql)
        return rows

