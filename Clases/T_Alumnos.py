from Clases.Alumno import Alumno
import time
#from Clases.BD_Escuela import BD_Escuela


class T_Alumnos:
    def __init__(self):
        self.__lista = {}

    def cargar_alumno(self, alumno:Alumno):
        llave = alumno.get_numero_registro()
        self.__lista[llave] = alumno

    def eliminar_alumno(self, alumno):
        hoy = time.strftime("%d/%m/%y")
        l_aux = hoy.split("/")
        baja = (l_aux[0], l_aux[1], l_aux[2])
        actu_alumno = alumno.set_baja(baja)

    def buscar_alumno(self,registro):
        try:
            return self.__lista[registro]
        except KeyError:
            return None

    def get_lista(self):
        return self.__lista

    def __iter__(self):
        return iter(self.__lista)

    def nuevo_nro_registro(self):
        return len(self.__lista)+1