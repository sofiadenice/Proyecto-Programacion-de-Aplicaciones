
class ValidarDatos:
    def __init__(self, dataList):
        self.dataList = dataList
        self.result = True

    def verificador(self):
        for data in self.dataList:
            if len(data) < 3:
                self.result = False
            if len(data) > 45:
                self.result = False
        return self.result
