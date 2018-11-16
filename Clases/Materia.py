class Materia:
    def __init__(self, codigo, nombre, calificacion1er, calificacion2do, calificacion3er):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__calificacion1er = calificacion1er
        self.__calificacion2do = calificacion2do
        self.__calificacion3er = calificacion3er

    def get_nombre(self):
        return self.__nombre

    def get_calificacion1er(self):
        return self.__calificacion1er

    def get_calificacion2do(self):
        return self.__calificacion2do

    def get_calificacion3er(self):
        return self.__calificacion3er

    def set_calificacion1er(self, calificacion):
        self.__calificacion1er = calificacion

    def set_calificacion2do(self, calificacion):
        self.__calificacion2do = calificacion

    def set_calificacion3er(self, calificacion):
        self.__calificacion3er = calificacion

    def calif_to_string(self):
        c1 = str(self.__calificacion1er)
        c2 = str(self.__calificacion2do)
        c3 = str(self.__calificacion3er)
        cadena = c1+';'+c2+';'+c3
        return cadena
