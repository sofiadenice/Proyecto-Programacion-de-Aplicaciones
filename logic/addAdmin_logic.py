from core.pyba_logic import PybaLogic


class AddAdminLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def selectAllAddAdmin(self):
        database = self.createDatabaseObj()
        sql = "SELECT * FROM clidente.user WHERE role = 'admin';"
        result = database.executeQuery(sql)
        return result

    def selectAllAddCliente(self):
        database = self.createDatabaseObj()
        sql = "SELECT * FROM clidente.user WHERE role = 'cliente';"
        result = database.executeQuery(sql)
        return result

    def getAdminById(self, id):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM clidente.user WHERE id={id};"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result[0]
        else:
            return []

    def insertAdminUser(self, userName, userEmail, password, salt):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO clidente.user "
            + "( id, user_name, user_email, password, salt, role) "
            + f"VALUES(0,'{userName}','{userEmail}','{password}','{salt}', 'admin');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def updateUser(self, id, userEmail, password, salt):
        database = self.createDatabaseObj()
        sql =  ("UPDATE `clidente`.`user` SET "
            + f"`id` = {id}, "
            + f" user_email = '{userEmail}', "
            + f" password = '{password}', "
            + f" salt = '{salt}' "
            + f" WHERE `id` = {id} ;")
        
        rows = database.executeNonQueryRows(sql)
        return rows



    def deleteUser(self, id):
        database = self.createDatabaseObj()
        sql = (f"DELETE FROM `clidente`.`user` WHERE id={id};")
        rows = database.executeNonQueryRows(sql)
        return rows