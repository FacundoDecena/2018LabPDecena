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
    def __init__(self, nro_registrop=0, userp='', passwordp='', nombrep='', apellidop='a', dnip=0, direccionp='', telefonop=4, emailp='', nacimientop=(0,0,0), cursop='', altap=(0,0,0), bajap=(0,0,0), conceptop=''):
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
        self.__inasistencia = 0
        self.__materias = [Materia(0, 'Matematica', -1, -1, -1), Materia(1, 'Lengua', -1, -1, -1),
                           Materia(2, 'Fisica', -1, -1, -1), Materia(3, 'Quimica', -1, -1, -1),
                           Materia(4, 'Biologia', -1, -1, -1), Materia(5, 'Etica', -1, -1, -1),
                           Materia(5, 'Historia', -1, -1, -1), Materia(5, 'Geografia', -1, -1, -1),
                           Materia(5, 'Computacion', -1, -1, -1)]
        self.__maximo = 15

    # Getters

    def get_nro_registro(self):
        return self.__nro_registro

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

    def get_user(self):
        return self.__usuario

    def get_clave(self):
        return self.__clave

    def get_concepto(self):
        return self.__concepto

    def get_inasistencia(self):
        return self.__inasistencia

    def get_materias(self):
        return self.__materias

    def get_maximo(self):
        return self.__maximo

    # Setters

    def set_nro_registro(self, nro_registrop):
        self.__nro_registro = nro_registrop

    def set_nombre(self, nombrep):
        self.__nombre = nombrep

    def set_apellido(self, apellidop):
        self.__apellido = apellidop

    def set_dni(self, dnip):
        self.__dni = dnip

    def set_direccion(self, direccionp):
        self.__direccion = direccionp

    def set_telefono(self, telefonop):
        self.__telefono = telefonop

    def set_email(self, emailp):
        self.__email = emailp

    def set_nacimiento(self, nacimientop):
        self.__nacimiento = nacimientop

    def set_curso(self, cursop):
        self.__curso = cursop

    def set_alta(self, altap):
        self.__alta_colegio = altap

    def set_baja(self, bajap):
        self.__baja_colegio = bajap

    def set_user(self, userp):
        self.__usuario = userp

    def set_clave(self, passwordp):
        self.__clave = passwordp

    def set_concepto(self, conceptop):
        self.__concepto = conceptop

    def set_inasistencia(self, inasistenciap):
        self.__inasistencia = inasistenciap

    def set_materias(self, materiasp:[Materia]):
        self.__materias = materiasp

    def set_maximo(self, maximop):
        self.__maximo = maximop

    # Others Methods

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

