from functools import reduce
from Clases.Alumno import Alumno
import time


class T_Alumnos:
    def __init__(self):
        self.__lista = {}

    def cargar_alumno(self, alumno: Alumno):
        llave = alumno.get_numero_registro()
        self.__lista[llave] = alumno

    def eliminar_alumno(self, alumno):
        hoy = time.strftime("%d/%m/%y")
        l_aux = hoy.split("/")
        baja = (int(l_aux[0]), int(l_aux[1]), int(l_aux[2]))
        actu_alumno = alumno.set_baja(baja)

    def buscar_alumno(self, registro):
        try:
            return self.__lista[registro]
        except KeyError:
            return None

    def buscar_por_dni(self, dni: int):
        alumnos = self.__lista.values()
        for alumno in alumnos:
            dni_a = alumno.get_dni()
            if dni_a == dni:
                return alumno
        return None

    def buscar_por_readmision(self):
        alumnos_todos = self.__lista.values()
        alumnos_faltas = list(filter(lambda x: x.get_inasistencia() > 15, alumnos_todos))
        return alumnos_faltas

    def buscar_por_curso(self, curso: int):
        alumnos_todos = list(self.__lista.values())
        # alumnos_curso = list(filter(lambda x: x.get_curso() == curso, alumnos_todos))
        alumnos_curso = reduce(lambda ac, a: ac + [a] if a.get_curso() == curso else ac, alumnos_todos, [])

        d_alumnos_curso = map(lambda alumno: [alumno.get_nombre(), alumno.get_apellido(), alumno.get_dni(),
                                                 alumno.get_numero_registro()], alumnos_curso)

        return reduce(lambda x, y: self.ordenar(x, y), d_alumnos_curso, [])

    def ordenar(self, x, y):
        if len(x) > 0:
            for i, val in enumerate(x):
                if y[0] < val[0]:
                    x.insert(i, y)
                    break
            else:
                x.append(y)
        else:
            x.append(y)
        return x

    def get_lista(self):
        return self.__lista

    def __iter__(self):
        return iter(self.__lista)

    def nuevo_nro_registro(self):
        return len(self.__lista) + 1

    def vaciar(self):
        self.__lista.clear()
        return self.__lista
