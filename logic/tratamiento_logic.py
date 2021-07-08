from core.pyba_logic import PybaLogic


class UserLogic(PybaLogic):
    def __init__(self):
        super().__init__()

    def insertUser(self, userName, userEmail, password, salt):
        database = self.createDatabaseObj()
        sql = (
            "INSERT INTO `user` "
            + "(`id`,`user_name`,`user_email`,`password`,`salt`) "
            + f"VALUES(0,'{userName}','{userEmail}','{password}','{salt}');"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def getUserByEmail(self, userEmail):
        database = self.createDatabaseObj()
        sql = (
            "SELECT user_email, password, salt "
            + f"FROM user where user_email like '{userEmail}';"
        )
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []

    def getRowByUser(self, user):
        database = self.createDatabaseObj()
        sql = f"SELECT * FROM user where user_name like '{user}';"
        result = database.executeQuery(sql)
        if len(result) > 0:
            return result[0]
        else:
            return []
