from Clases.Materia import Materia

class T_Materias:
    def __init__(self):
        self.__lista = {}

    def cargar_materia(self, reg:int, materias:Materia):
        self.__lista[reg] = materias

    def get_materia_reg(self, reg:int):
        return self.__lista[reg]
    def vaciar(self):
        self.__lista.clear()
        return self.__lista