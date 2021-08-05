from core.pyba_logic import PybaLogic


class TratamientoLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def selectAllTratamiento(self):
        database = self.createDatabaseObj()
        sql = "SELECT * FROM clidente.tratamiento;"
        result = database.executeQuery(sql)
        return result
    
    def getTratamientoById(self, id):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM clidente.tratamiento WHERE id={id};"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result[0]
        else:
            return []

    def insertTratamiento(self, nombre, descripcion, imagen):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO clidente.tratamiento "
            + "(`id`, `nombre`, `descripcion`, `imagen`) "
            + f"VALUES (0,'{nombre}','{descripcion}','{imagen}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateTratamiento(self, id, nombre, descripcion, imagen):
        database = self.createDatabaseObj()
        sql = ("UPDATE clidente.tratamiento SET "
            + f"`id` = {id}, "
            + f"`nombre` = '{nombre}', "
            + f"`descripcion` = '{descripcion}', "
            + f"`imagen` = '{imagen}' "
            + f"WHERE `id` = {id};")
        rows = database.executeNonQueryRows(sql)
        return rows

    def deleteTratamiento(self, id):
        database = self.createDatabaseObj()
        sql = (f"DELETE FROM `clidente`.`tratamiento` WHERE id={id};")
        rows = database.executeNonQueryRows(sql)
        return rows

