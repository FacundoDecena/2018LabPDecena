from Clases.Alumno import Alumno


class BD_Escuela:

    def __init__(self):
        self.cant_usuarios = 1
        self.acceso = {'P-Admin': 'Ad1'}
        self.nbre_tablas = {'T_Alumnos':0, 'T_Materias': 1}
        self.tablas = ['T_Alumnos', 'T_Materias']

    def cargar_usuarios(self):
        mapa = {}
        with open('Usuarios.txt', 'r') as f:
            for linea in f:
                usuario = linea.split(':')
                user = usuario[0]
                clave = usuario[1]
                clave = clave[0:-1]
                mapa[user] = clave
        f.close()
        return mapa

    def registrar_usuario(self, user, pass_, mapa):
        map_ = mapa
        usuario = user
        clave = pass_
        map_[usuario] = clave
        self.grabar_usuarios(map_)
        return map_

    def grabar_usuarios(self, mapa):
        with open ('Usuarios.txt', 'w') as f:
            for clave in mapa.keys():
                f.write(clave+':'+mapa[clave]+'\n')

    def eliminar_usuario(self, usr, mapa):
        shallow_copy = dict(mapa)
        del shallow_copy[usr]
        self.grabar_usuarios(shallow_copy)
        return shallow_copy
