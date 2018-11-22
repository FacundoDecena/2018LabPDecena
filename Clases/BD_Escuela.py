from Clases.Alumno import Alumno
from Clases.Materia import Materia
from Clases.T_Alumnos import T_Alumnos
from Clases.T_Materias import T_Materias


class BD_Escuela:

    def __init__(self):
        self.__cant_usuarios = 1
        self.__acceso = {'P-Admin': 'ad1'}
        self.__nbre_tablas = {'T_Alumnos':0, 'T_Materias': 1}
        self.__t_alumnos = T_Alumnos()
        self.__t_materias = T_Materias()
        self.__tablas = [self.__t_alumnos, self.__t_materias]

    '''def cargar_usuarios(self):
        self.__cant_usuarios = 0
        with open('Usuarios.txt', 'r') as f:
            for linea in f:
                usuario = linea.split(':')
                user = usuario[0]
                clave = usuario[1]
                clave = clave[0:-1]
                self.__acceso[user] = clave
                self.__cant_usuarios = self.__cant_usuarios + 1
        f.close()
        return self.__acceso'''

    def cargar_usuarios(self):
        return self.__acceso

    def registrar_usuario(self, user, pass_):
        usuario = user
        clave = pass_
        try:
            u = self.__acceso[usuario]
            self.__acceso[usuario] = clave
        except KeyError:
            self.__acceso[usuario] = clave
            self.__cant_usuarios = self.__cant_usuarios+1
        return self.__acceso

    '''def grabar_usuarios(self):
        with open('Usuarios.txt', 'w') as f:
            for clave in self.__acceso.keys():
                f.write(clave +':' + self.__acceso[clave] + '\n')
        f.close()'''

    def eliminar_usuario(self, usr):
        try:
            del self.__acceso[usr]
            return self.__acceso
        except:
            raise KeyError

    def cargar_alumnos(self, arch):
        self.__t_alumnos.vaciar()
        self.__t_materias.vaciar()
        self.__acceso.clear()
        self.__acceso = {'P-Admin': 'ad1'} # No nos podemos olvidar de nuestro superusuario
        self.__cant_usuarios = 1

        with open(arch, 'r') as f:
            try:
                c_u = int(f.readline())
                for i in range(c_u):
                    linea = f.readline()
                    usuario = linea.split(':')
                    user = usuario[0]
                    clave = usuario[1]
                    clave = clave[0:-1]
                    self.__acceso[user] = clave
                self.__cant_usuarios = len(self.__acceso)
                c_a = int(f.readline())
                for i in range(c_a):
                    linea = f.readline()
                    datos_alumno = linea.split(';')
                    nro_registro1 = datos_alumno[0]
                    nro_registro = int(nro_registro1)
                    usuario = datos_alumno[1]
                    clave = datos_alumno[2]
                    nombre = datos_alumno[3]
                    apellido = datos_alumno[4]
                    dni1 = datos_alumno[5]
                    dni = int(dni1)
                    direccion = datos_alumno[6]
                    telefono = datos_alumno[7]
                    email = datos_alumno[8]
                    nacimientos = datos_alumno[9]
                    curso = int(datos_alumno[10])
                    alta_colegios = datos_alumno[11]
                    baja_colegios = datos_alumno[12]
                    concepto = datos_alumno[13]
                    inasistencia1 = datos_alumno[14]
                    inasistencia = int(inasistencia1)
                    maximo = datos_alumno[15]
                    nacimiento = eval(nacimientos)
                    alta_colegio = eval(alta_colegios)
                    baja_colegio = eval(baja_colegios)
                    alumno = Alumno(nro_registro,usuario,clave,nombre,apellido,dni,direccion,telefono,email,nacimiento,curso,alta_colegio,baja_colegio,concepto,inasistencia,maximo)
                    # self.__acceso[usuario] = clave
                    # self.__cant_usuarios = self.__cant_usuarios + 1
                    nota11 = int(datos_alumno[16])
                    nota12 = int(datos_alumno[17])
                    nota13 = int(datos_alumno[18])
                    nota21 = int(datos_alumno[19])
                    nota22 = int(datos_alumno[20])
                    nota23 = int(datos_alumno[21])
                    nota31 = int(datos_alumno[22])
                    nota32 = int(datos_alumno[23])
                    nota33 = int(datos_alumno[24])
                    nota41 = int(datos_alumno[25])
                    nota42 = int(datos_alumno[26])
                    nota43 = int(datos_alumno[27])
                    nota51 = int(datos_alumno[28])
                    nota52 = int(datos_alumno[29])
                    nota53 = int(datos_alumno[30])
                    nota61 = int(datos_alumno[31])
                    nota62 = int(datos_alumno[32])
                    nota63 = int(datos_alumno[33])
                    nota71 = int(datos_alumno[34])
                    nota72 = int(datos_alumno[35])
                    nota73 = int(datos_alumno[36])
                    nota81 = int(datos_alumno[37])
                    nota82 = int(datos_alumno[38])
                    nota83 = int(datos_alumno[39])
                    nota91 = int(datos_alumno[40])
                    nota92 = int(datos_alumno[41])
                    nota93 = int(datos_alumno[42])
                    materias = [Materia(0, 'Matematica', nota11, nota12, nota13), Materia(1, 'Lengua', nota21, nota22, nota23),
                                Materia(2, 'Fisica', nota31, nota32, nota33), Materia(3, 'Quimica', nota41, nota42, nota43),
                                Materia(4, 'Biologia', nota51, nota52, nota53), Materia(5, 'Etica', nota61, nota62, nota63),
                                Materia(6, 'Historia', nota71, nota72, nota73), Materia(7, 'Geografia', nota81, nota82, nota83),
                                Materia(8, 'Computacion', nota91, nota92, nota93)]
                    alumno.set_materias(materias)
                    self.__t_materias.cargar_materia(nro_registro,materias)
                    self.__t_alumnos.cargar_alumno(alumno)
            except ValueError:
                pass # Dado que el archivo esta vacio no hay nada que leer
        f.close()
        return self.__t_alumnos

    def grabar_alumnos(self, arch, talumnos:T_Alumnos):
        alumnos_aux = talumnos.get_lista()
        alumnos = list(alumnos_aux.items())
        with open (arch, 'w') as f:
            l = self.__cant_usuarios
            f.write(str(l)+'\n')
            for clave in self.__acceso.keys():
                f.write(clave + ':' + self.__acceso[clave] + '\n')
            l = len(alumnos_aux)
            f.write(str(l) + '\n')
            for alumno in alumnos:
                f.write(str(alumno[1])+'\n')
        f.close()
