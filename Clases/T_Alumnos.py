from Clases.Alumno import Alumno
from Clases.BD_Escuela import BD_Escuela


class T_Alumnos:
    def __init__(self):
        self.__lista = {}
        self.__lista = self.cargar_bd()

    def cargar_bd(self):
        bd = BD_Escuela()
        self.__lista = bd.cargar_usuarios()
        return self.__lista

    def registrar_usuario(self, usr, pas):
        bd = BD_Escuela()
        self.__lista[usr] = pas
        bd.registrar_usuario(usr, pas, self.__lista)

    def eliminar_usuario(self, usr):
        del self.__lista[usr]
