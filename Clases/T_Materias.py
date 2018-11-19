from Clases.Materia import Materia

class T_Materias:
    def __init__(self):
        self.__lista = {}

    def cargar_materia(self, reg:int, materia:Materia):
        self.__lista[reg] = materia

    def get_materia_reg(self, reg:int):
        return self.__lista[reg]
