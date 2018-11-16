from Clases.Alumno import Alumno
#from Clases.BD_Escuela import BD_Escuela


class T_Alumnos:
    def __init__(self):
        self.__lista = {}

    #def cargar_bd(self):
        #bd = BD_Escuela()

    def cargar_alumno(self, alumno:Alumno):
        llave = alumno.get_numero_registro()
        self.__lista[llave] = alumno

    def eliminar_alumno(self, alumno):
        baja = (16,11,2018) #Si tuviese mas tiempo lo seteo con el dia de hoy
        actu_alumno = alumno.set_baja(baja)
        llave = alumno.get_numero_registro()
        self.__lista[llave] = actu_alumno

    def buscar_alumno(self,registro):
        try:
            return self.__lista[registro]
        except KeyError:
            return None

    def __iter__(self):
        return iter(self.__lista)

    def nuevo_nro_registro(self):
        return len(self.__lista)+1