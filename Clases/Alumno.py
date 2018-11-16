from Clases.Materia import Materia


class Alumno:
    # Las variables declaradas en el constructor deben seguir este formato
    # __nro_registro :: int
    # __nombre :: string
    # __apellido :: string
    # __dni :: int
    # __direccion :: string
    # __telefono :: int
    # __email :: string
    # __nacimiento :: (int, int, int)
    # __curso :: int
    # __alta_colegio :: (int, int, int)
    # __baja_colegio :: (int, int, int)
    # __user :: string
    # __password :: string
    # __concepto :: string
    # __inasistencia :: int
    # __materias :: [Materia]
    # __maximo :: 15
    def __init__(self, nro_registrop=0, userp='', passwordp='', nombrep='', apellidop='a', dnip=0, direccionp='',
                 telefonop=0, emailp='', nacimientop=(0,0,0), cursop='', altap=(0,0,0), bajap=(0,0,0), conceptop='',
                 inasistenciap=0,maximop=15):
        self.__nro_registro = nro_registrop
        self.__usuario = userp
        self.__clave = passwordp
        self.__nombre = nombrep
        self.__apellido = apellidop
        self.__dni = dnip
        self.__direccion = direccionp
        self.__telefono = telefonop
        self.__email = emailp
        self.__nacimiento = nacimientop
        self.__curso = cursop
        self.__alta_colegio = altap
        self.__baja_colegio = bajap
        self.__concepto = conceptop
        self.__inasistencia = inasistenciap
        self.__materias = [Materia(0, 'Matematica', -1, -1, -1), Materia(1, 'Lengua', -1, -1, -1),
                           Materia(2, 'Fisica', -1, -1, -1), Materia(3, 'Quimica', -1, -1, -1),
                           Materia(4, 'Biologia', -1, -1, -1), Materia(5, 'Etica', -1, -1, -1),
                           Materia(6, 'Historia', -1, -1, -1), Materia(7, 'Geografia', -1, -1, -1),
                           Materia(8, 'Computacion', -1, -1, -1)]
        self.__maximo = maximop

    def get_numero_registro(self):
        return self.__nro_registro

    def get_usuario(self):
        return self.__usuario

    def get_clave(self):
        return self.__clave

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_dni(self):
        return self.__dni

    def get_direccion(self):
        return self.__direccion

    def get_telefono(self):
        return self.__telefono

    def get_email(self):
        return self.__email

    def get_nacimiento(self):
        return self.__nacimiento

    def get_curso(self):
        return self.__curso

    def get_alta(self):
        return self.__alta_colegio

    def get_baja(self):
        return self.__baja_colegio

    def get_concepto(self):
        return self.__concepto

    def get_inasistencia(self):
        return self.__inasistencia

    def get_materias(self):
        return self.__materias

    def get_maximo(self):
        return self.__maximo

    def set_baja(self,baja):
        self.__baja_colegio = baja

    def set_materias(self, materias):
        self.__materias=materias

    def mod_alumno(self, userp, passwordp, nombrep, apellidop, dnip, direccionp, telefonop, emailp,
                   nacimientop, cursop, altap, bajap, conceptop, inasistenciap, materiasp, maximop):
        self.__usuario = userp
        self.__clave = passwordp
        self.__nombre = nombrep
        self.__apellido = apellidop
        self.__dni = dnip
        self.__direccion = direccionp
        self.__telefono = telefonop
        self.__email = emailp
        self.__nacimiento = nacimientop
        self.__curso = cursop
        self.__alta_colegio = altap
        self.__baja_colegio = bajap
        self.__concepto = conceptop
        self.__inasistencia = inasistenciap
        self.__materias = materiasp
        self.__maximo = maximop

    def control_password(self, password):
        return self.__clave == password

    def maximo_inasistencia(self):
        return self.__inasistencia > self.__maximo

    def readmision(self):
        if self.__inasistencia < self.__maximo:
            return 0
        if self.__concepto == 'NA':
            return 1
        self.__maximo = 30
        return 2

