from tkinter import *
from tkinter.filedialog import *
from GUI.TableScroll import Table
from Clases.BD_Escuela import BD_Escuela
from Clases.T_Alumnos import T_Alumnos
from Clases.Alumno import Alumno
from Clases.Materia import Materia

FUENTE = 'Tahoma'
TAMANOF = '14'

global arch
arch = ''
global talumno
talumno = T_Alumnos()
bd = BD_Escuela()
global es_prog


def swap_view(old_view, new_view):
    old_view.terminate()
    if new_view == 'MP':
        MenuPrincipalP(root)
    elif new_view == 'login':
        Login(root)
    elif new_view == 'registrar_usuario':
        RegUs(root)
    elif new_view == 'eliminar_usuario':
        ElimUs(root)
    elif new_view == 'Alta':
        Alta(root)
    elif new_view == 'Baja':
        Baja(root)
    elif new_view == 'Consulta':
        Consulta(root)
    elif new_view == 'Modificacion':
        Modificacion(root)
    elif new_view == 'buscar arch':
        BuscarArchivo(root)
    elif new_view == 'back_up':
        BackUp(root)
    elif new_view == 'tabla_a':
        TablaA(root)
    elif new_view == 'tabla_m':
        TablaM(root)
    elif new_view == 'legajo':
        Legajo(root)
    elif new_view == 'readmision':
        Readmision(root)
    elif new_view == 'curso':
        Curso(root)

def center(n):
    # Center window
    n.eval('tk::PlaceWindow %s center' % n.winfo_pathname(n.winfo_id()))


class Login:
    # Constantes
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Login')
        # Variables para usar en widgets
        self.usuario = StringVar()
        self.clave = StringVar()
        self.om_selected = StringVar()
        self.om_selected.set('Programador')
        # Creo la matriz
        self.frame.columnconfigure(0, weight=0)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=0)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.frame.rowconfigure(4, weight=1)
        self.frame.rowconfigure(5, weight=1)
        self.frame.rowconfigure(6, weight=1)
        self.frame.rowconfigure(7, weight=1)
        self.frame.rowconfigure(8, weight=1)
        # Agregar widgets
        # Labels
        self.label_usuario = Label(self.frame,
                                   text="Usuario:")
        self.label_usuario.grid(row=2,
                                column=1,
                                sticky=E)
        self.label_clave = Label(self.frame,
                                 text="Contraseña:")
        self.label_clave.grid(row=3,
                              column=1,
                              sticky=E + N)
        self.label_usr_incorrecto = Label(self.frame, text='El usuario no existe')
        self.label_usr_incorrecto.grid(row=2,
                                       column=3,
                                       sticky=E)
        self.label_usr_incorrecto.config(fg='red')
        self.label_usr_incorrecto.grid_remove()
        self.label_pass_incorrecta = Label(self.frame, text='La clave es incorrecta')
        self.label_pass_incorrecta.grid(row=3,
                                        column=3,
                                        sticky=E)
        self.label_pass_incorrecta.config(fg='red')
        self.label_pass_incorrecta.grid_remove()
        # Campos de texto
        self.entry_usuario = Entry(self.frame,
                                   textvariable=self.usuario)
        self.entry_usuario.grid(pady=0,
                                row=2,
                                column=2,
                                sticky=E + W)
        self.entry_clave = Entry(self.frame,
                                 show='•',
                                 font=(FUENTE, TAMANOF),
                                 textvariable=self.clave)
        self.entry_clave.grid(row=3,
                              column=2,
                              sticky=E + W + N)
        # Option Menu
        self.opt1 = OptionMenu(self.frame, self.om_selected, 'Programador', 'Docente', 'Alumno')
        self.opt1.grid(pady=0,
                       ipadx=75,
                       row=4,
                       column=1,
                       columnspan=3,
                       sticky=N)
        # Botones
        self.button_acceder = Button(self.frame,
                                     text="Acceder",
                                     command=self.comprobar_clave)
        self.button_acceder.grid(pady=0,
                                 ipadx=75,
                                 row=6,
                                 column=1,
                                 columnspan=3,
                                 sticky=N)
        center(master)
        # Main loop
        self.frame.mainloop()

    def comprobar_clave(self):
        self.label_pass_incorrecta.grid_remove()
        self.label_usr_incorrecto.grid_remove()
        usuarios = bd.cargar_usuarios()
        usr = ''
        if self.om_selected.get() == 'Programador':
            usr = 'P-' + self.usuario.get()
            global es_prog
            es_prog = True
        if self.om_selected.get() == 'Docente':
            usr = 'D-' + self.usuario.get()
            es_prog = False
        if self.om_selected.get() == 'Alumno':
            usr = 'A-' + self.usuario.get()
            es_prog = False
        clv = self.clave.get()
        try:
            if usuarios[usr] == clv:
                self.login()
            else:
                self.label_pass_incorrecta.grid()
        except KeyError:
            self.label_usr_incorrecto.grid()

    def login(self):
        swap_view(self, 'MP')

    def terminate(self):
        self.frame.pack_forget()
        self.frame.destroy()


# ******************************************************************************************************************** #
class MenuPrincipalP(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Menu Principal')
        # Creo la matriz
        self.frame.columnconfigure(0, weight=0)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.frame.rowconfigure(4, weight=1)
        self.frame.rowconfigure(5, weight=1)
        self.frame.rowconfigure(6, weight=1)
        # Botones
        global es_prog
        self.button_reg_us = Button(self.frame,
                                    text='Registrar un Usuario',
                                    command=lambda: swap_view(self, 'registrar_usuario'))
        self.button_reg_us.grid(pady=0,
                                ipadx=75,
                                row=1,
                                column=0,
                                columnspan=1,
                                sticky=E + W)
        if not es_prog:
            self.button_reg_us.config(state='disabled')
        self.button_elim_us = Button(self.frame,
                                     text="Eliminar Usuario",
                                     command=lambda: swap_view(self, 'eliminar_usuario'))
        self.button_elim_us.grid(pady=0,
                                 ipadx=75,
                                 row=2,
                                 column=0,
                                 columnspan=1,
                                 sticky=E + W)
        if es_prog == False:
            self.button_elim_us.config(state='disabled')
        self.button_carga_bd = Button(self.frame,
                                      text="Inicializar sesión de trabajo",
                                      command=lambda: swap_view(self, 'buscar arch'))
        self.button_carga_bd.grid(pady=0,
                                  ipadx=75,
                                  row=3,
                                  column=0,
                                  columnspan=1,
                                  sticky=E + W)
        if es_prog == False:
            self.button_carga_bd.config(state='disabled')
        self.button_back_up = Button(self.frame,
                                     text="BackUp",
                                     command=lambda: swap_view(self, 'back_up'))
        self.button_back_up.grid(pady=0,
                                 ipadx=75,
                                 row=4,
                                 column=0,
                                 columnspan=1,
                                 sticky=E + W)
        if es_prog == False:
            self.button_back_up.config(state='disabled')
        self.button_cerrar_sesion = Button(self.frame,
                                           text="Cerrar Sesion",
                                           command=lambda: swap_view(self, 'login'))
        self.button_cerrar_sesion.grid(pady=0,
                                       ipadx=75,
                                       row=5,
                                       column=0,
                                       columnspan=1,
                                       sticky=E + W)
        self.button_alta_alu = Button(self.frame,
                                      text="Alta",
                                      command=lambda: swap_view(self, 'Alta'))
        self.button_alta_alu.grid(pady=0,
                                  ipadx=75,
                                  row=1,
                                  column=1,
                                  columnspan=1,
                                  sticky=E + W)
        if es_prog == False:
            self.button_alta_alu.config(state='disabled')
        self.button_baja_alu = Button(self.frame,
                                      text="Baja",
                                      command=lambda: swap_view(self, 'Baja'))
        self.button_baja_alu.grid(pady=0,
                                  ipadx=75,
                                  row=2,
                                  column=1,
                                  columnspan=1,
                                  sticky=E + W)
        if es_prog == False:
            self.button_baja_alu.config(state='disabled')
        self.button_con_alu = Button(self.frame,
                                     text="Consulta",
                                     command=lambda: swap_view(self, 'Consulta'))
        self.button_con_alu.grid(pady=0,
                                 ipadx=75,
                                 row=3,
                                 column=1,
                                 columnspan=1,
                                 sticky=E + W)
        if es_prog == False:
            self.button_con_alu.config(state='disabled')
        self.button_mod_alu = Button(self.frame,
                                     text="Modificacion",
                                     command=lambda: swap_view(self, 'Modificacion'))
        self.button_mod_alu.grid(pady=0,
                                 ipadx=75,
                                 row=4,
                                 column=1,
                                 columnspan=1,
                                 sticky=E + W)
        if es_prog == False:
            self.button_mod_alu.config(state='disabled')
        self.button_list_t_alu = Button(self.frame,
                                        text="Tabla Alumnos",
                                        command=lambda: swap_view(self, 'tabla_a'))
        self.button_list_t_alu.grid(pady=0,
                                    ipadx=0,
                                    row=1,
                                    column=2,
                                    columnspan=1,
                                    sticky=E + W)
        self.button_list_t_mat = Button(self.frame,
                                        text="Tabla Materias",
                                        command=lambda: swap_view(self, 'tabla_m'))
        self.button_list_t_mat.grid(pady=0,
                                    ipadx=75,
                                    row=2,
                                    column=2,
                                    columnspan=1,
                                    sticky=E + W)
        self.button_list_leg_a = Button(self.frame,
                                        text="Legajo",
                                        command=lambda: swap_view(self, 'legajo'))
        self.button_list_leg_a.grid(pady=0,
                                    ipadx=75,
                                    row=3,
                                    column=2,
                                    columnspan=1,
                                    sticky=E + W)
        self.button_list_inas = Button(self.frame,
                                       text="Solicitudes de readmision",
                                       command=lambda: swap_view(self, 'readmision'))
        self.button_list_inas.grid(pady=0,
                                   ipadx=75,
                                   row=4,
                                   column=2,
                                   columnspan=1,
                                   sticky=E + W)
        self.button_lis_reg_curso = Button(self.frame,
                                           text="Listado Alumnos",
                                           command=lambda: swap_view(self, 'curso'))
        self.button_lis_reg_curso.grid(pady=0,
                                       ipadx=75,
                                       row=5,
                                       column=2,
                                       columnspan=1,
                                       sticky=E + W)

        # Center
        center(master)

    def terminate(self):
        self.frame.pack_forget()
        self.frame.destroy()


# ******************************************************************************************************************** #
class RegUs(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Registrar Usuario')
        # Creo la matriz
        self.frame.columnconfigure(0, weight=0)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=0)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.frame.rowconfigure(4, weight=1)
        self.frame.rowconfigure(5, weight=1)
        self.frame.rowconfigure(6, weight=1)
        self.frame.rowconfigure(7, weight=1)
        self.frame.rowconfigure(8, weight=1)
        # Agregar widgets
        self.usuario = StringVar()
        self.clave = StringVar()
        self.om_selected = StringVar()
        self.om_selected.set('Programador')
        # Labels
        self.label_usuario = Label(self.frame,
                                   text="Usuario:")
        self.label_usuario.grid(row=2,
                                column=1,
                                sticky=E)

        self.label_usr_incorrecto = Label(self.frame, text='', fg='red')
        self.label_usr_incorrecto.grid(row=2,
                                       column=4,
                                       sticky=E)
        self.label_clave = Label(self.frame,
                                 text="Contraseña:")
        self.label_clave.grid(row=3,
                              column=1,
                              sticky=E + N)
        # Campos de texto
        self.entry_usuario = Entry(self.frame,
                                   textvariable=self.usuario)
        self.entry_usuario.grid(pady=0,
                                row=2,
                                column=3,
                                sticky=E + W)
        self.entry_clave = Entry(self.frame,
                                 show='•',
                                 font=(FUENTE, TAMANOF),
                                 textvariable=self.clave)
        self.entry_clave.grid(row=3,
                              column=3,
                              sticky=E + W + N)
        # Option Menu
        self.opt1 = OptionMenu(self.frame, self.om_selected, 'Programador', 'Docente', 'Alumno')
        self.opt1.grid(pady=0,
                       ipadx=75,
                       row=4,
                       column=1,
                       columnspan=4,
                       sticky=N)
        # Botones
        self.button_registrar = Button(self.frame,
                                       text="Registrar",
                                       command=self.registrar)
        self.button_registrar.grid(pady=0,
                                   ipadx=75,
                                   row=6,
                                   column=1,
                                   columnspan=2,
                                   sticky=N)
        self.button_volver = Button(self.frame,
                                    text='Volver',
                                    command=lambda: swap_view(self, 'MP'))

        self.button_volver.grid(pady=0,
                                ipadx=75,
                                row=6,
                                column=3,
                                columnspan=2,
                                sticky=N)
        center(master)

    def registrar(self):
        usuarios = bd.cargar_usuarios()
        usr = ''
        if self.om_selected.get() == 'Programador':
            usr = 'P-' + self.usuario.get()
        if self.om_selected.get() == 'Docente':
            usr = 'D-' + self.usuario.get()
        if self.om_selected.get() == 'Alumno':
            usr = 'A-' + self.usuario.get()
        clv = self.clave.get()
        user = usuarios.get(usr)
        if self.usuario.get() == '' or clv == '':
            user = 'nonone'
        if user is None:
            bd.registrar_usuario(usr, clv)
        else:
            if user == 'nonone':
                self.label_usr_incorrecto.config(text='Nombre de usuario inválido')
            else:
                self.label_usr_incorrecto.config(text='El usuario ya existe')

    def terminate(self):
        self.frame.pack_forget()
        self.frame.destroy()


# ******************************************************************************************************************** #
class ElimUs(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Eliminar Usuario')
        # Creo la matriz
        self.frame.columnconfigure(0, weight=0)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=0)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.frame.rowconfigure(4, weight=1)
        self.frame.rowconfigure(5, weight=1)
        self.frame.rowconfigure(6, weight=1)
        self.frame.rowconfigure(7, weight=1)
        self.frame.rowconfigure(8, weight=1)
        # Agregar widgets
        self.usuario = StringVar()
        self.om_selected = StringVar()
        self.om_selected.set('Programador')
        # Labels
        self.label_usuario = Label(self.frame,
                                   text="Usuario:")
        self.label_usuario.grid(row=2,
                                column=1,
                                sticky=E)

        self.label_usr_incorrecto = Label(self.frame, text='El usuario no existe')
        self.label_usr_incorrecto.grid(row=2,
                                       column=4,
                                       sticky=E)
        self.label_usr_incorrecto.config(fg='red')
        self.label_usr_incorrecto.grid_remove()
        self.label_estado = Label(self.frame,
                                  text="Eliminado:")
        self.label_estado.grid(row=3,
                               column=1,
                               sticky=E + N)
        # Campos de texto
        self.entry_usuario = Entry(self.frame,
                                   textvariable=self.usuario)
        self.entry_usuario.grid(pady=0,
                                row=2,
                                column=3,
                                sticky=E + W)
        self.label_Estado = Label(self.frame,
                                  text="No:")
        self.label_Estado.grid(row=3,
                               column=3,
                               sticky=E + W + N)
        # Option Menu
        self.opt1 = OptionMenu(self.frame, self.om_selected, 'Programador', 'Docente', 'Alumno')
        self.opt1.grid(pady=0,
                       ipadx=75,
                       row=4,
                       column=1,
                       columnspan=3,
                       sticky=N)
        # Botones
        self.button_registrar = Button(self.frame,
                                       text="Eliminar",
                                       command=self.eliminar)
        self.button_registrar.grid(pady=0,
                                   ipadx=75,
                                   row=6,
                                   column=1,
                                   columnspan=2,
                                   sticky=N)
        self.button_volver = Button(self.frame,
                                    text='Volver',
                                    command=lambda: swap_view(self, 'MP'))

        self.button_volver.grid(pady=0,
                                ipadx=75,
                                row=6,
                                column=3,
                                columnspan=2,
                                sticky=N)
        center(master)

    def eliminar(self):
        usuarios = bd.cargar_usuarios()
        usr = ''
        if self.om_selected.get() == 'Programador':
            usr = 'P-' + self.usuario.get()
        if self.om_selected.get() == 'Docente':
            usr = 'D-' + self.usuario.get()
        if self.om_selected.get() == 'Alumno':
            usr = 'A-' + self.usuario.get()
        user = usuarios.get(usr)
        if not (user is None):
            bd.eliminar_usuario(usr)
            self.label_Estado.config(text='Si')
        else:
            self.label_usr_incorrecto.grid()

    def terminate(self):
        self.frame.pack_forget()
        self.frame.destroy()


# ******************************************************************************************************************** #
class BuscarArchivo(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('buscar')
        self.nombre = StringVar()
        self.label_aviso = Label(self.frame,
                                 text='Para crear complete el campo de abajo y oprima Aceptar. Para buscar' +
                                      'presione el botón Buscar')
        self.label_aviso.grid(pady=0, row=0, column=0, columnspan=2, sticky=E + W)
        self.label_nombre = Label(self.frame, text='Nombre del archivo')
        self.label_nombre.grid(pady=0, row=2, column=0, sticky=E + W)
        self.entry_nombre = Entry(self.frame, textvariable=self.nombre)
        self.entry_nombre.grid(pady=0, row=2, column=1, sticky=E + W)
        self.button_aceptar = Button(self.frame, text="Aceptar", command=self.aceptar)
        self.button_aceptar.grid(pady=0, row=3, column=0, sticky=E + W)
        self.button_buscar = Button(self.frame, text="Buscar", command=self.buscar)
        self.button_buscar.grid(pady=0, row=3, column=1, sticky=E + W)
        self.button_volver = Button(self.frame, text="Volver", command=lambda: swap_view(self, 'MP'))
        self.button_volver.grid(pady=0, row=4, column=0, sticky=E + W)

    def aceptar(self):
        global arch
        arch = self.nombre.get() + '.txt'
        f = open(arch, 'w')
        f.close()
        global talumno
        talumno = bd.cargar_alumnos(arch)
        self.label_aviso.config(text=arch + ' Abierto', fg='green')

    def buscar(self):
        options = {'initialdir': os.getcwd()}
        global arch
        arch = askopenfilename(**options)
        if arch == "":
            self.label_aviso.config(text=arch + 'Ningun archivo Abierto', fg='red')
        else:
            global talumno
            self.label_aviso.config(text=arch + ' Abierto', fg='green')
            talumno = bd.cargar_alumnos(arch)

    def terminate(self):
        self.frame.pack_forget()
        self.frame.destroy()


# ******************************************************************************************************************** #
class BackUp(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('buscar')
        self.nombre = StringVar()
        self.label_aviso = Label(self.frame,
                                 text='Para crear complete el campo de abajo y oprima Aceptar. Para buscar' +
                                      'presione el botón Buscar')
        self.label_aviso.grid(pady=0, row=0, column=0, columnspan=2, sticky=E + W)
        self.label_nombre = Label(self.frame, text='Nombre del archivo')
        self.label_nombre.grid(pady=0, row=2, column=0, sticky=E + W)
        self.entry_nombre = Entry(self.frame, textvariable=self.nombre)
        self.entry_nombre.grid(pady=0, row=2, column=1, sticky=E + W)
        self.button_aceptar = Button(self.frame, text="Aceptar", command=self.aceptar)
        self.button_aceptar.grid(pady=0, row=3, column=0, sticky=E + W)
        self.button_buscar = Button(self.frame, text="Buscar", command=self.buscar)
        self.button_buscar.grid(pady=0, row=3, column=1, sticky=E + W)
        self.button_volver = Button(self.frame, text="Volver", command=lambda: swap_view(self, 'MP'))
        self.button_volver.grid(pady=0, row=4, column=0, sticky=E + W)

    def aceptar(self):
        global arch
        global talumno
        arch = self.nombre.get() + '.txt'
        f = open(arch, 'w')
        f.close()
        bd.grabar_alumnos(arch, talumno)
        self.label_aviso.config(text=arch + ' cargado y abierto', fg='green')

    def buscar(self):
        options = {'initialdir': os.getcwd()}
        global arch
        global talumno
        arch = askopenfilename(**options)
        if arch == "":
            self.label_aviso.config(text=arch + ' ningun archivo seleccionado')
        else:
            self.label_aviso.config(text=arch + ' cargado y abierto', fg='green')
            bd.grabar_alumnos(arch, talumno)

    def terminate(self):
        self.frame.pack_forget()
        self.frame.destroy()


# ******************************************************************************************************************** #
class Alta(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        global talumno
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Alta')
        # las 30000 Variables para usar en widgets
        self.nro_registro = IntVar()
        nreg = talumno.nuevo_nro_registro()
        self.nro_registro.set(nreg)
        self.usuario = StringVar()
        self.clave = StringVar()
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.dni = IntVar()
        self.direccion = StringVar()
        self.telefono = IntVar()
        self.email = StringVar()
        self.nacimientos = StringVar()
        self.curso = IntVar()
        self.alta_colegios = StringVar()
        self.baja_colegios = StringVar()
        self.baja_colegios.set('0,0,0')
        self.inasistencia = IntVar()
        self.om_selected = StringVar()
        self.om_selected.set('MA')

        self.nota11 = IntVar()
        self.nota12 = IntVar()
        self.nota13 = IntVar()
        self.nota21 = IntVar()
        self.nota22 = IntVar()
        self.nota23 = IntVar()
        self.nota31 = IntVar()
        self.nota32 = IntVar()
        self.nota33 = IntVar()
        self.nota41 = IntVar()
        self.nota42 = IntVar()
        self.nota43 = IntVar()
        self.nota51 = IntVar()
        self.nota52 = IntVar()
        self.nota53 = IntVar()
        self.nota61 = IntVar()
        self.nota62 = IntVar()
        self.nota63 = IntVar()
        self.nota71 = IntVar()
        self.nota72 = IntVar()
        self.nota73 = IntVar()
        self.nota81 = IntVar()
        self.nota82 = IntVar()
        self.nota83 = IntVar()
        self.nota91 = IntVar()
        self.nota92 = IntVar()
        self.nota93 = IntVar()
        # los 30000 widgets
        self.label_nro_registro = Label(self.frame, text='Numero de Registro')
        self.label_nro_registro.grid(pady=0, row=1, column=0, sticky=E + W)
        self.label_usuario = Label(self.frame, text='Usuario')
        self.label_usuario.grid(pady=0, row=2, column=0, sticky=E + W)
        self.label_clave = Label(self.frame, text='clave')
        self.label_clave.grid(pady=0, row=3, column=0, sticky=E + W)
        self.label_nombre = Label(self.frame, text='nombre')
        self.label_nombre.grid(pady=0, row=4, column=0, sticky=E + W)
        self.label_apellido = Label(self.frame, text='apellido')
        self.label_apellido.grid(pady=0, row=5, column=0, sticky=E + W)
        self.label_dni = Label(self.frame, text='DNI')
        self.label_dni.grid(pady=0, row=6, column=0, sticky=E + W)
        self.label_direccion = Label(self.frame, text='direccion')
        self.label_direccion.grid(pady=0, row=7, column=0, sticky=E + W)
        self.label_telefono = Label(self.frame, text='telefono')
        self.label_telefono.grid(pady=0, row=8, column=0, sticky=E + W)
        self.label_email = Label(self.frame, text='email')
        self.label_email.grid(pady=0, row=9, column=0, sticky=E + W)
        self.label_nacimiento = Label(self.frame, text='nacimiento dd,mm,aaaa')
        self.label_nacimiento.grid(pady=0, row=10, column=0, sticky=E + W)
        self.label_curso = Label(self.frame, text='curso')
        self.label_curso.grid(pady=0, row=11, column=0, sticky=E + W)
        self.label_alta_colegio = Label(self.frame, text='alta colegio dd,mm,aaaa')
        self.label_alta_colegio.grid(pady=0, row=12, column=0, sticky=E + W)
        self.label_baja_colegio = Label(self.frame, text='baja colegio dd,mm,aaaa')
        self.label_baja_colegio.grid(pady=0, row=13, column=0, sticky=E + W)
        self.label_concepto = Label(self.frame, text='concepto')
        self.label_concepto.grid(pady=0, row=14, column=0, sticky=E + W)
        self.label_inasistencia = Label(self.frame, text='inasistencia')
        self.label_inasistencia.grid(pady=0, row=15, column=0, sticky=E + W)
        self.label_nota11 = Label(self.frame, text='Nota Matematica 1')
        self.label_nota11.grid(pady=0, row=16, column=0, sticky=E + W)
        self.label_nota12 = Label(self.frame, text='Nota Matematica 2')
        self.label_nota12.grid(pady=0, row=17, column=0, sticky=E + W)
        self.label_nota13 = Label(self.frame, text='Nota Matematica 3')
        self.label_nota13.grid(pady=0, row=18, column=0, sticky=E + W)
        self.label_nota21 = Label(self.frame, text='Nota Lengua 1')
        self.label_nota21.grid(pady=0, row=19, column=0, sticky=E + W)
        self.label_nota22 = Label(self.frame, text='Nota Lengua 2')
        self.label_nota22.grid(pady=0, row=20, column=0, sticky=E + W)
        self.label_nota23 = Label(self.frame, text='Nota Lengua 3')
        self.label_nota23.grid(pady=0, row=21, column=0, sticky=E + W)

        self.label_nota31 = Label(self.frame, text='Nota Fisica 1')
        self.label_nota31.grid(pady=0, row=1, column=2, sticky=E + W)
        self.label_nota32 = Label(self.frame, text='Nota Fisica 2')
        self.label_nota32.grid(pady=0, row=2, column=2, sticky=E + W)
        self.label_nota33 = Label(self.frame, text='Nota Fisica 3')
        self.label_nota33.grid(pady=0, row=3, column=2, sticky=E + W)
        self.label_nota41 = Label(self.frame, text='Nota Quimica 1')
        self.label_nota41.grid(pady=0, row=4, column=2, sticky=E + W)
        self.label_nota42 = Label(self.frame, text='Nota Quimica 2')
        self.label_nota42.grid(pady=0, row=5, column=2, sticky=E + W)
        self.label_nota43 = Label(self.frame, text='Nota Quimica 3')
        self.label_nota43.grid(pady=0, row=6, column=2, sticky=E + W)
        self.label_nota51 = Label(self.frame, text='Nota Biologia 1')
        self.label_nota51.grid(pady=0, row=7, column=2, sticky=E + W)
        self.label_nota52 = Label(self.frame, text='Nota Biologia 2')
        self.label_nota52.grid(pady=0, row=8, column=2, sticky=E + W)
        self.label_nota53 = Label(self.frame, text='Nota Biologia 3')
        self.label_nota53.grid(pady=0, row=9, column=2, sticky=E + W)
        self.label_nota61 = Label(self.frame, text='Nota Etica 1')
        self.label_nota61.grid(pady=0, row=10, column=2, sticky=E + W)
        self.label_nota62 = Label(self.frame, text='Nota Etica 2')
        self.label_nota62.grid(pady=0, row=11, column=2, sticky=E + W)
        self.label_nota63 = Label(self.frame, text='Nota Etica 3')
        self.label_nota63.grid(pady=0, row=12, column=2, sticky=E + W)
        self.label_nota71 = Label(self.frame, text='Nota Historia 1')
        self.label_nota71.grid(pady=0, row=13, column=2, sticky=E + W)
        self.label_nota72 = Label(self.frame, text='Nota Historia 2')
        self.label_nota72.grid(pady=0, row=14, column=2, sticky=E + W)
        self.label_nota73 = Label(self.frame, text='Nota Historia 3')
        self.label_nota73.grid(pady=0, row=15, column=2, sticky=E + W)
        self.label_nota81 = Label(self.frame, text='Nota Geografia 1')
        self.label_nota81.grid(pady=0, row=16, column=2, sticky=E + W)
        self.label_nota82 = Label(self.frame, text='Nota Geografia 2')
        self.label_nota82.grid(pady=0, row=17, column=2, sticky=E + W)
        self.label_nota83 = Label(self.frame, text='Nota Geografia 3')
        self.label_nota83.grid(pady=0, row=18, column=2, sticky=E + W)
        self.label_nota91 = Label(self.frame, text='Nota Computacion 1')
        self.label_nota91.grid(pady=0, row=19, column=2, sticky=E + W)
        self.label_nota92 = Label(self.frame, text='Nota Computacion 2')
        self.label_nota92.grid(pady=0, row=20, column=2, sticky=E + W)
        self.label_nota93 = Label(self.frame, text='Nota Computacion 3')
        self.label_nota93.grid(pady=0, row=21, column=2, sticky=E + W)
        # Campos de texto
        self.entry_nro_registro = Entry(self.frame, textvariable=self.nro_registro, state='disable')
        self.entry_nro_registro.grid(pady=0, row=1, column=1, sticky=E + W)
        self.entry_usuario = Entry(self.frame, textvariable=self.usuario)
        self.entry_usuario.grid(pady=0, row=2, column=1, sticky=E + W)
        self.entry_clave = Entry(self.frame, textvariable=self.clave)
        self.entry_clave.grid(pady=0, row=3, column=1, sticky=E + W)
        self.entry_nombre = Entry(self.frame, textvariable=self.nombre)
        self.entry_nombre.grid(pady=0, row=4, column=1, sticky=E + W)
        self.entry_apellido = Entry(self.frame, textvariable=self.apellido)
        self.entry_apellido.grid(pady=0, row=5, column=1, sticky=E + W)
        self.entry_dni = Entry(self.frame, textvariable=self.dni)
        self.entry_dni.grid(pady=0, row=6, column=1, sticky=E + W)
        self.entry_direccion = Entry(self.frame, textvariable=self.direccion)
        self.entry_direccion.grid(pady=0, row=7, column=1, sticky=E + W)
        self.entry_telefono = Entry(self.frame, textvariable=self.telefono)
        self.entry_telefono.grid(pady=0, row=8, column=1, sticky=E + W)
        self.entry_email = Entry(self.frame, textvariable=self.email)
        self.entry_email.grid(pady=0, row=9, column=1, sticky=E + W)
        self.entry_nacimiento = Entry(self.frame, textvariable=self.nacimientos)
        self.entry_nacimiento.grid(pady=0, row=10, column=1, sticky=E + W)
        self.entry_curso = Entry(self.frame, textvariable=self.curso)
        self.entry_curso.grid(pady=0, row=11, column=1, sticky=E + W)
        self.entry_alta_colegio = Entry(self.frame, textvariable=self.alta_colegios)
        self.entry_alta_colegio.grid(pady=0, row=12, column=1, sticky=E + W)
        self.entry_baja_colegio = Entry(self.frame, textvariable=self.baja_colegios)
        self.entry_baja_colegio.grid(pady=0, row=13, column=1, sticky=E + W)
        self.opt1 = OptionMenu(self.frame, self.om_selected, 'MA', 'A', 'NA')
        self.opt1.grid(pady=0, row=14, column=1, sticky=E + W)
        self.entry_inasistencia = Entry(self.frame, textvariable=self.inasistencia)
        self.entry_inasistencia.grid(pady=0, row=15, column=1, sticky=E + W)
        self.entry_nota11 = Entry(self.frame, textvariable=self.nota11)
        self.entry_nota11.grid(pady=0, row=16, column=1, sticky=E + W)
        self.entry_nota12 = Entry(self.frame, textvariable=self.nota12)
        self.entry_nota12.grid(pady=0, row=17, column=1, sticky=E + W)
        self.entry_nota13 = Entry(self.frame, textvariable=self.nota13)
        self.entry_nota13.grid(pady=0, row=18, column=1, sticky=E + W)
        self.entry_nota21 = Entry(self.frame, textvariable=self.nota21)
        self.entry_nota21.grid(pady=0, row=19, column=1, sticky=E + W)
        self.entry_nota22 = Entry(self.frame, textvariable=self.nota22)
        self.entry_nota22.grid(pady=0, row=20, column=1, sticky=E + W)
        self.entry_nota23 = Entry(self.frame, textvariable=self.nota23)
        self.entry_nota23.grid(pady=0, row=21, column=1, sticky=E + W)

        self.entry_nota31 = Entry(self.frame, textvariable=self.nota31)
        self.entry_nota31.grid(pady=0, row=1, column=3, sticky=E + W)
        self.entry_nota32 = Entry(self.frame, textvariable=self.nota32)
        self.entry_nota32.grid(pady=0, row=2, column=3, sticky=E + W)
        self.entry_nota33 = Entry(self.frame, textvariable=self.nota33)
        self.entry_nota33.grid(pady=0, row=3, column=3, sticky=E + W)
        self.entry_nota41 = Entry(self.frame, textvariable=self.nota41)
        self.entry_nota41.grid(pady=0, row=4, column=3, sticky=E + W)
        self.entry_nota42 = Entry(self.frame, textvariable=self.nota42)
        self.entry_nota42.grid(pady=0, row=5, column=3, sticky=E + W)
        self.entry_nota43 = Entry(self.frame, textvariable=self.nota43)
        self.entry_nota43.grid(pady=0, row=6, column=3, sticky=E + W)
        self.entry_nota51 = Entry(self.frame, textvariable=self.nota51)
        self.entry_nota51.grid(pady=0, row=7, column=3, sticky=E + W)
        self.entry_nota52 = Entry(self.frame, textvariable=self.nota52)
        self.entry_nota52.grid(pady=0, row=8, column=3, sticky=E + W)
        self.entry_nota53 = Entry(self.frame, textvariable=self.nota53)
        self.entry_nota53.grid(pady=0, row=9, column=3, sticky=E + W)
        self.entry_nota61 = Entry(self.frame, textvariable=self.nota61)
        self.entry_nota61.grid(pady=0, row=10, column=3, sticky=E + W)
        self.entry_nota62 = Entry(self.frame, textvariable=self.nota62)
        self.entry_nota62.grid(pady=0, row=11, column=3, sticky=E + W)
        self.entry_nota63 = Entry(self.frame, textvariable=self.nota63)
        self.entry_nota63.grid(pady=0, row=12, column=3, sticky=E + W)
        self.entry_nota71 = Entry(self.frame, textvariable=self.nota71)
        self.entry_nota71.grid(pady=0, row=13, column=3, sticky=E + W)
        self.entry_nota72 = Entry(self.frame, textvariable=self.nota72)
        self.entry_nota72.grid(pady=0, row=14, column=3, sticky=E + W)
        self.entry_nota73 = Entry(self.frame, textvariable=self.nota73)
        self.entry_nota73.grid(pady=0, row=15, column=3, sticky=E + W)
        self.entry_nota81 = Entry(self.frame, textvariable=self.nota81)
        self.entry_nota81.grid(pady=0, row=16, column=3, sticky=E + W)
        self.entry_nota82 = Entry(self.frame, textvariable=self.nota82)
        self.entry_nota82.grid(pady=0, row=17, column=3, sticky=E + W)
        self.entry_nota83 = Entry(self.frame, textvariable=self.nota83)
        self.entry_nota83.grid(pady=0, row=18, column=3, sticky=E + W)
        self.entry_nota91 = Entry(self.frame, textvariable=self.nota91)
        self.entry_nota91.grid(pady=0, row=19, column=3, sticky=E + W)
        self.entry_nota92 = Entry(self.frame, textvariable=self.nota92)
        self.entry_nota92.grid(pady=0, row=20, column=3, sticky=E + W)
        self.entry_nota93 = Entry(self.frame, textvariable=self.nota93)
        self.entry_nota93.grid(pady=0, row=21, column=3, sticky=E + W)

        self.label_error = Label(self.frame, text=' ')
        self.label_error.grid(pady=0, row=22, column=0, sticky=E + W)
        self.label_error.config(fg='red')

        self.button_alta = Button(self.frame, text="Alta", command=self.alta)
        self.button_alta.grid(pady=0, row=23, column=1, sticky=E + W)

        self.button_volver = Button(self.frame, text='Volver', command=lambda: swap_view(self, 'MP'))
        self.button_volver.grid(pady=0, row=24, column=0, sticky=E + W)

        # Center
        center(master)

    def alta(self):
        global talumno
        self.label_error.config(text=' ')
        try:
            nacimiento = eval('(' + str(self.nacimientos.get()) + ')')
            alta_colegio = eval('(' + str(self.alta_colegios.get()) + ')')
            baja_colegio = eval('(' + str(self.baja_colegios.get()) + ')')
            alumn = talumno.buscar_alumno(self.nro_registro.get())
            if alumn is None:
                usu = 'A-' + self.usuario.get()
                alumno = Alumno(self.nro_registro.get(), usu, self.clave.get(), self.nombre.get(),
                                self.apellido.get(), self.dni.get(), self.direccion.get(), self.telefono.get(),
                                self.email.get(), nacimiento, self.curso.get(), alta_colegio, baja_colegio,
                                self.om_selected.get(), self.inasistencia.get())
                materias = [Materia(0, 'Matematica', self.nota11.get(), self.nota12.get(), self.nota13.get()),
                            Materia(1, 'Lengua', self.nota21.get(), self.nota22.get(), self.nota23.get()),
                            Materia(2, 'Fisica', self.nota31.get(), self.nota32.get(), self.nota33.get()),
                            Materia(3, 'Quimica', self.nota41.get(), self.nota42.get(), self.nota43.get()),
                            Materia(4, 'Biologia', self.nota51.get(), self.nota52.get(), self.nota53.get()),
                            Materia(5, 'Etica', self.nota61.get(), self.nota62.get(), self.nota63.get()),
                            Materia(6, 'Historia', self.nota71.get(), self.nota72.get(), self.nota73.get()),
                            Materia(7, 'Geografia', self.nota81.get(), self.nota82.get(), self.nota83.get()),
                            Materia(8, 'Computacion', self.nota91.get(), self.nota92.get(), self.nota93.get())]
                alumno.set_materias(materias)
                talumno.cargar_alumno(alumno)
                bd.registrar_usuario('A-' + str(self.usuario.get()), self.clave.get())
                global arch
                # bd.grabar_alumnos(talumno, arch)
                self.label_error.config(text='Alumno dado de alta correctamente', fg='green')
            else:
                self.label_error.config(text='El numero de registro ya existe', fg='red')
        except SyntaxError:
            self.label_error.config(text='Hay campos con errores', fg='red')
        except:
            self.label_error.config(text='Hay campos con valores invalidos', fg='red')

    def terminate(self):
        self.frame.pack_forget()
        self.frame.destroy()


# ******************************************************************************************************************** #
class Baja(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        global talumno
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Baja')

        self.nro_registro = IntVar()
        nreg = talumno.nuevo_nro_registro()
        self.nro_registro.set(nreg)

        self.label_nro_registro = Label(self.frame, text='Numero de Registro')
        self.label_nro_registro.grid(pady=0, row=1, column=0, sticky=E + W)

        # Campos de texto
        self.entry_nro_registro = Entry(self.frame, textvariable=self.nro_registro)
        self.entry_nro_registro.grid(pady=0, row=1, column=1, sticky=E + W)

        self.label_error = Label(self.frame, text=' ')
        self.label_error.grid(pady=0, row=2, column=0, sticky=E + W)
        self.label_error.config(fg='red')

        self.button_baja = Button(self.frame, text="Baja", command=self.baja)
        self.button_baja.grid(pady=0, row=3, column=1, columnspan=2, sticky=E + W)

        self.button_volver = Button(self.frame, text='Volver', command=lambda: swap_view(self, 'MP'))
        self.button_volver.grid(pady=0, row=4, column=0, sticky=E + W)

        # Center
        center(master)

    def baja(self):
        global talumno
        self.label_error.config(text=' ')
        try:
            nroreg = int(self.nro_registro.get())
            alumno = talumno.buscar_alumno(nroreg)
            if alumno is None:
                self.label_error.config(text='El numero de registro no existe')
            else:
                usr = alumno.get_usuario()
                bd.eliminar_usuario(usr)
                talumno.eliminar_alumno(alumno)
                self.label_error.config(text='Alumno dado de baja correctamente', fg='green')
        except SyntaxError:
            self.label_error.config(text='Hay campos con errores')
        '''except:
            self.label_error.config(text='Hay campos con valores invalidos')'''

    def terminate(self):
        self.frame.pack_forget()
        self.frame.destroy()


# ******************************************************************************************************************** #
class Consulta(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        global talumno
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Consulta')
        # las 30000 Variables para usar en widgets
        self.nro_registro = IntVar()
        nreg = talumno.nuevo_nro_registro()
        self.nro_registro.set(nreg)
        self.usuario = StringVar()
        self.clave = StringVar()
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.dni = IntVar()
        self.direccion = StringVar()
        self.telefono = IntVar()
        self.email = StringVar()
        self.nacimientos = StringVar()
        self.curso = StringVar()
        self.alta_colegios = StringVar()
        self.baja_colegios = StringVar()
        self.baja_colegios.set('0,0,0')
        self.concepto = StringVar()
        self.inasistencia = IntVar()

        self.nota11 = IntVar()
        self.nota12 = IntVar()
        self.nota13 = IntVar()
        self.nota21 = IntVar()
        self.nota22 = IntVar()
        self.nota23 = IntVar()
        self.nota31 = IntVar()
        self.nota32 = IntVar()
        self.nota33 = IntVar()
        self.nota41 = IntVar()
        self.nota42 = IntVar()
        self.nota43 = IntVar()
        self.nota51 = IntVar()
        self.nota52 = IntVar()
        self.nota53 = IntVar()
        self.nota61 = IntVar()
        self.nota62 = IntVar()
        self.nota63 = IntVar()
        self.nota71 = IntVar()
        self.nota72 = IntVar()
        self.nota73 = IntVar()
        self.nota81 = IntVar()
        self.nota82 = IntVar()
        self.nota83 = IntVar()
        self.nota91 = IntVar()
        self.nota92 = IntVar()
        self.nota93 = IntVar()
        # los 30000 widgets
        self.label_nro_registro = Label(self.frame, text='Numero de Registro')
        self.label_nro_registro.grid(pady=0, row=1, column=0, sticky=E + W)
        self.label_usuario = Label(self.frame, text='Usuario')
        self.label_usuario.grid(pady=0, row=2, column=0, sticky=E + W)
        self.label_clave = Label(self.frame, text='clave')
        self.label_clave.grid(pady=0, row=3, column=0, sticky=E + W)
        self.label_nombre = Label(self.frame, text='nombre')
        self.label_nombre.grid(pady=0, row=4, column=0, sticky=E + W)
        self.label_apellido = Label(self.frame, text='apellido')
        self.label_apellido.grid(pady=0, row=5, column=0, sticky=E + W)
        self.label_dni = Label(self.frame, text='DNI')
        self.label_dni.grid(pady=0, row=6, column=0, sticky=E + W)
        self.label_direccion = Label(self.frame, text='direccion')
        self.label_direccion.grid(pady=0, row=7, column=0, sticky=E + W)
        self.label_telefono = Label(self.frame, text='telefono')
        self.label_telefono.grid(pady=0, row=8, column=0, sticky=E + W)
        self.label_email = Label(self.frame, text='email')
        self.label_email.grid(pady=0, row=9, column=0, sticky=E + W)
        self.label_nacimiento = Label(self.frame, text='nacimiento dd,mm,aaaa')
        self.label_nacimiento.grid(pady=0, row=10, column=0, sticky=E + W)
        self.label_curso = Label(self.frame, text='curso')
        self.label_curso.grid(pady=0, row=11, column=0, sticky=E + W)
        self.label_alta_colegio = Label(self.frame, text='alta colegio dd,mm,aaaa')
        self.label_alta_colegio.grid(pady=0, row=12, column=0, sticky=E + W)
        self.label_baja_colegio = Label(self.frame, text='baja colegio dd,mm,aaaa')
        self.label_baja_colegio.grid(pady=0, row=13, column=0, sticky=E + W)
        self.label_concepto = Label(self.frame, text='concepto')
        self.label_concepto.grid(pady=0, row=14, column=0, sticky=E + W)
        self.label_inasistencia = Label(self.frame, text='inasistencia')
        self.label_inasistencia.grid(pady=0, row=15, column=0, sticky=E + W)
        self.label_nota11 = Label(self.frame, text='Nota Matematica 1')
        self.label_nota11.grid(pady=0, row=16, column=0, sticky=E + W)
        self.label_nota12 = Label(self.frame, text='Nota Matematica 2')
        self.label_nota12.grid(pady=0, row=17, column=0, sticky=E + W)
        self.label_nota13 = Label(self.frame, text='Nota Matematica 3')
        self.label_nota13.grid(pady=0, row=18, column=0, sticky=E + W)
        self.label_nota21 = Label(self.frame, text='Nota Lengua 1')
        self.label_nota21.grid(pady=0, row=19, column=0, sticky=E + W)
        self.label_nota22 = Label(self.frame, text='Nota Lengua 2')
        self.label_nota22.grid(pady=0, row=20, column=0, sticky=E + W)
        self.label_nota23 = Label(self.frame, text='Nota Lengua 3')
        self.label_nota23.grid(pady=0, row=21, column=0, sticky=E + W)

        self.label_nota31 = Label(self.frame, text='Nota Fisica 1')
        self.label_nota31.grid(pady=0, row=1, column=2, sticky=E + W)
        self.label_nota32 = Label(self.frame, text='Nota Fisica 2')
        self.label_nota32.grid(pady=0, row=2, column=2, sticky=E + W)
        self.label_nota33 = Label(self.frame, text='Nota Fisica 3')
        self.label_nota33.grid(pady=0, row=3, column=2, sticky=E + W)
        self.label_nota41 = Label(self.frame, text='Nota Quimica 1')
        self.label_nota41.grid(pady=0, row=4, column=2, sticky=E + W)
        self.label_nota42 = Label(self.frame, text='Nota Quimica 2')
        self.label_nota42.grid(pady=0, row=5, column=2, sticky=E + W)
        self.label_nota43 = Label(self.frame, text='Nota Quimica 3')
        self.label_nota43.grid(pady=0, row=6, column=2, sticky=E + W)
        self.label_nota51 = Label(self.frame, text='Nota Biologia 1')
        self.label_nota51.grid(pady=0, row=7, column=2, sticky=E + W)
        self.label_nota52 = Label(self.frame, text='Nota Biologia 2')
        self.label_nota52.grid(pady=0, row=8, column=2, sticky=E + W)
        self.label_nota53 = Label(self.frame, text='Nota Biologia 3')
        self.label_nota53.grid(pady=0, row=9, column=2, sticky=E + W)
        self.label_nota61 = Label(self.frame, text='Nota Etica 1')
        self.label_nota61.grid(pady=0, row=10, column=2, sticky=E + W)
        self.label_nota62 = Label(self.frame, text='Nota Etica 2')
        self.label_nota62.grid(pady=0, row=11, column=2, sticky=E + W)
        self.label_nota63 = Label(self.frame, text='Nota Etica 3')
        self.label_nota63.grid(pady=0, row=12, column=2, sticky=E + W)
        self.label_nota71 = Label(self.frame, text='Nota Historia 1')
        self.label_nota71.grid(pady=0, row=13, column=2, sticky=E + W)
        self.label_nota72 = Label(self.frame, text='Nota Historia 2')
        self.label_nota72.grid(pady=0, row=14, column=2, sticky=E + W)
        self.label_nota73 = Label(self.frame, text='Nota Historia 3')
        self.label_nota73.grid(pady=0, row=15, column=2, sticky=E + W)
        self.label_nota81 = Label(self.frame, text='Nota Geografia 1')
        self.label_nota81.grid(pady=0, row=16, column=2, sticky=E + W)
        self.label_nota82 = Label(self.frame, text='Nota Geografia 2')
        self.label_nota82.grid(pady=0, row=17, column=2, sticky=E + W)
        self.label_nota83 = Label(self.frame, text='Nota Geografia 3')
        self.label_nota83.grid(pady=0, row=18, column=2, sticky=E + W)
        self.label_nota91 = Label(self.frame, text='Nota Computacion 1')
        self.label_nota91.grid(pady=0, row=19, column=2, sticky=E + W)
        self.label_nota92 = Label(self.frame, text='Nota Computacion 2')
        self.label_nota92.grid(pady=0, row=20, column=2, sticky=E + W)
        self.label_nota93 = Label(self.frame, text='Nota Computacion 3')
        self.label_nota93.grid(pady=0, row=21, column=2, sticky=E + W)
        # Campos de texto
        self.entry_nro_registro = Entry(self.frame, textvariable=self.nro_registro)
        self.entry_nro_registro.grid(pady=0, row=1, column=1, sticky=E + W)
        self.entry_usuario = Entry(self.frame, textvariable=self.usuario, state='disabled')
        self.entry_usuario.grid(pady=0, row=2, column=1, sticky=E + W)
        self.entry_clave = Entry(self.frame, textvariable=self.clave, state='disabled')
        self.entry_clave.grid(pady=0, row=3, column=1, sticky=E + W)
        self.entry_nombre = Entry(self.frame, textvariable=self.nombre, state='disabled')
        self.entry_nombre.grid(pady=0, row=4, column=1, sticky=E + W)
        self.entry_apellido = Entry(self.frame, textvariable=self.apellido, state='disabled')
        self.entry_apellido.grid(pady=0, row=5, column=1, sticky=E + W)
        self.entry_dni = Entry(self.frame, textvariable=self.dni, state='disabled')
        self.entry_dni.grid(pady=0, row=6, column=1, sticky=E + W)
        self.entry_direccion = Entry(self.frame, textvariable=self.direccion, state='disabled')
        self.entry_direccion.grid(pady=0, row=7, column=1, sticky=E + W)
        self.entry_telefono = Entry(self.frame, textvariable=self.telefono, state='disabled')
        self.entry_telefono.grid(pady=0, row=8, column=1, sticky=E + W)
        self.entry_email = Entry(self.frame, textvariable=self.email, state='disabled')
        self.entry_email.grid(pady=0, row=9, column=1, sticky=E + W)
        self.entry_nacimiento = Entry(self.frame, textvariable=self.nacimientos, state='disabled')
        self.entry_nacimiento.grid(pady=0, row=10, column=1, sticky=E + W)
        self.entry_curso = Entry(self.frame, textvariable=self.curso, state='disabled')
        self.entry_curso.grid(pady=0, row=11, column=1, sticky=E + W)
        self.entry_alta_colegio = Entry(self.frame, textvariable=self.alta_colegios, state='disabled')
        self.entry_alta_colegio.grid(pady=0, row=12, column=1, sticky=E + W)
        self.entry_baja_colegio = Entry(self.frame, textvariable=self.baja_colegios, state='disabled')
        self.entry_baja_colegio.grid(pady=0, row=13, column=1, sticky=E + W)
        self.entry_concepto = Entry(self.frame, textvariable=self.concepto, state='disabled')
        self.entry_concepto.grid(pady=0, row=14, column=1, sticky=E + W)
        self.entry_inasistencia = Entry(self.frame, textvariable=self.inasistencia, state='disabled')
        self.entry_inasistencia.grid(pady=0, row=15, column=1, sticky=E + W)
        self.entry_nota11 = Entry(self.frame, textvariable=self.nota11, state='disabled')
        self.entry_nota11.grid(pady=0, row=16, column=1, sticky=E + W)
        self.entry_nota12 = Entry(self.frame, textvariable=self.nota12, state='disabled')
        self.entry_nota12.grid(pady=0, row=17, column=1, sticky=E + W)
        self.entry_nota13 = Entry(self.frame, textvariable=self.nota13, state='disabled')
        self.entry_nota13.grid(pady=0, row=18, column=1, sticky=E + W)
        self.entry_nota21 = Entry(self.frame, textvariable=self.nota21, state='disabled')
        self.entry_nota21.grid(pady=0, row=19, column=1, sticky=E + W)
        self.entry_nota22 = Entry(self.frame, textvariable=self.nota22, state='disabled')
        self.entry_nota22.grid(pady=0, row=20, column=1, sticky=E + W)
        self.entry_nota23 = Entry(self.frame, textvariable=self.nota23, state='disabled')
        self.entry_nota23.grid(pady=0, row=21, column=1, sticky=E + W)

        self.entry_nota31 = Entry(self.frame, textvariable=self.nota31, state='disabled')
        self.entry_nota31.grid(pady=0, row=1, column=3, sticky=E + W)
        self.entry_nota32 = Entry(self.frame, textvariable=self.nota32, state='disabled')
        self.entry_nota32.grid(pady=0, row=2, column=3, sticky=E + W)
        self.entry_nota33 = Entry(self.frame, textvariable=self.nota33, state='disabled')
        self.entry_nota33.grid(pady=0, row=3, column=3, sticky=E + W)
        self.entry_nota41 = Entry(self.frame, textvariable=self.nota41, state='disabled')
        self.entry_nota41.grid(pady=0, row=4, column=3, sticky=E + W)
        self.entry_nota42 = Entry(self.frame, textvariable=self.nota42, state='disabled')
        self.entry_nota42.grid(pady=0, row=5, column=3, sticky=E + W)
        self.entry_nota43 = Entry(self.frame, textvariable=self.nota43, state='disabled')
        self.entry_nota43.grid(pady=0, row=6, column=3, sticky=E + W)
        self.entry_nota51 = Entry(self.frame, textvariable=self.nota51, state='disabled')
        self.entry_nota51.grid(pady=0, row=7, column=3, sticky=E + W)
        self.entry_nota52 = Entry(self.frame, textvariable=self.nota52, state='disabled')
        self.entry_nota52.grid(pady=0, row=8, column=3, sticky=E + W)
        self.entry_nota53 = Entry(self.frame, textvariable=self.nota53, state='disabled')
        self.entry_nota53.grid(pady=0, row=9, column=3, sticky=E + W)
        self.entry_nota61 = Entry(self.frame, textvariable=self.nota61, state='disabled')
        self.entry_nota61.grid(pady=0, row=10, column=3, sticky=E + W)
        self.entry_nota62 = Entry(self.frame, textvariable=self.nota62, state='disabled')
        self.entry_nota62.grid(pady=0, row=11, column=3, sticky=E + W)
        self.entry_nota63 = Entry(self.frame, textvariable=self.nota63, state='disabled')
        self.entry_nota63.grid(pady=0, row=12, column=3, sticky=E + W)
        self.entry_nota71 = Entry(self.frame, textvariable=self.nota71, state='disabled')
        self.entry_nota71.grid(pady=0, row=13, column=3, sticky=E + W)
        self.entry_nota72 = Entry(self.frame, textvariable=self.nota72, state='disabled')
        self.entry_nota72.grid(pady=0, row=14, column=3, sticky=E + W)
        self.entry_nota73 = Entry(self.frame, textvariable=self.nota73, state='disabled')
        self.entry_nota73.grid(pady=0, row=15, column=3, sticky=E + W)
        self.entry_nota81 = Entry(self.frame, textvariable=self.nota81, state='disabled')
        self.entry_nota81.grid(pady=0, row=16, column=3, sticky=E + W)
        self.entry_nota82 = Entry(self.frame, textvariable=self.nota82, state='disabled')
        self.entry_nota82.grid(pady=0, row=17, column=3, sticky=E + W)
        self.entry_nota83 = Entry(self.frame, textvariable=self.nota83, state='disabled')
        self.entry_nota83.grid(pady=0, row=18, column=3, sticky=E + W)
        self.entry_nota91 = Entry(self.frame, textvariable=self.nota91, state='disabled')
        self.entry_nota91.grid(pady=0, row=19, column=3, sticky=E + W)
        self.entry_nota92 = Entry(self.frame, textvariable=self.nota92, state='disabled')
        self.entry_nota92.grid(pady=0, row=20, column=3, sticky=E + W)
        self.entry_nota93 = Entry(self.frame, textvariable=self.nota93, state='disabled')
        self.entry_nota93.grid(pady=0, row=21, column=3, sticky=E + W)

        self.label_error = Label(self.frame, text=' ')
        self.label_error.grid(pady=0, row=22, column=0, sticky=E + W)
        self.label_error.config(fg='red')

        self.button_consultar = Button(self.frame, text="Consultar", command=self.consultar)
        self.button_consultar.grid(pady=0, row=23, column=1, sticky=E + W)

        self.button_volver = Button(self.frame, text='Volver', command=lambda: swap_view(self, 'MP'))
        self.button_volver.grid(pady=0, row=24, column=0, sticky=E + W)

        # Center
        center(master)

    def consultar(self):
        global talumno
        self.label_error.config(text=' ')
        try:
            nroreg = int(self.nro_registro.get())
            alumno = talumno.buscar_alumno(nroreg)
            if alumno is None:
                self.label_error.config(text='El numero de registro no existe')
            else:
                self.usuario.set(alumno.get_usuario())
                self.clave.set(alumno.get_clave())
                self.nombre.set(alumno.get_nombre())
                self.apellido.set(alumno.get_apellido())
                self.dni.set(alumno.get_dni())
                self.direccion.set(alumno.get_direccion())
                self.telefono.set(alumno.get_telefono())
                self.email.set(alumno.get_email())
                nacimiento1 = str(alumno.get_nacimiento())
                self.nacimientos.set(nacimiento1)
                self.curso.set(alumno.get_curso())
                alta1 = str(alumno.get_alta())
                self.alta_colegios.set(alta1)
                baja1 = str(alumno.get_baja())
                self.baja_colegios.set(baja1)
                self.concepto.set(alumno.get_concepto())
                self.inasistencia.set(alumno.get_inasistencia())
                mats = alumno.get_materias()
                self.nota11.set(mats[0].get_calificacion1er())
                self.nota12.set(mats[0].get_calificacion2do())
                self.nota13.set(mats[0].get_calificacion3er())
                self.nota21.set(mats[1].get_calificacion1er())
                self.nota22.set(mats[1].get_calificacion2do())
                self.nota23.set(mats[1].get_calificacion3er())
                self.nota31.set(mats[2].get_calificacion1er())
                self.nota32.set(mats[2].get_calificacion2do())
                self.nota33.set(mats[2].get_calificacion3er())
                self.nota41.set(mats[3].get_calificacion1er())
                self.nota42.set(mats[3].get_calificacion2do())
                self.nota43.set(mats[3].get_calificacion3er())
                self.nota51.set(mats[4].get_calificacion1er())
                self.nota52.set(mats[4].get_calificacion2do())
                self.nota53.set(mats[4].get_calificacion3er())
                self.nota61.set(mats[5].get_calificacion1er())
                self.nota62.set(mats[5].get_calificacion2do())
                self.nota63.set(mats[5].get_calificacion3er())
                self.nota71.set(mats[6].get_calificacion1er())
                self.nota72.set(mats[6].get_calificacion2do())
                self.nota73.set(mats[6].get_calificacion3er())
                self.nota81.set(mats[7].get_calificacion1er())
                self.nota82.set(mats[7].get_calificacion2do())
                self.nota83.set(mats[7].get_calificacion3er())
                self.nota91.set(mats[8].get_calificacion1er())
                self.nota92.set(mats[8].get_calificacion2do())
                self.nota93.set(mats[8].get_calificacion3er())
        except SyntaxError:
            self.label_error.config(text='Hay campos con errores')

    def terminate(self):
        self.frame.pack_forget()
        self.frame.destroy()


# ******************************************************************************************************************** #
class Modificacion(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        global talumno
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Modificar')
        # las 30000 Variables para usar en widgets
        self.nro_registro = IntVar()
        nreg = talumno.nuevo_nro_registro()
        self.nro_registro.set(nreg)
        self.usuario = StringVar()
        self.clave = StringVar()
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.dni = IntVar()
        self.direccion = StringVar()
        self.telefono = IntVar()
        self.email = StringVar()
        self.nacimientos = StringVar()
        self.curso = StringVar()
        self.alta_colegios = StringVar()
        self.baja_colegios = StringVar()
        self.baja_colegios.set('0,0,0')
        self.om_selected = StringVar()
        self.inasistencia = IntVar()

        self.nota11 = IntVar()
        self.nota12 = IntVar()
        self.nota13 = IntVar()
        self.nota21 = IntVar()
        self.nota22 = IntVar()
        self.nota23 = IntVar()
        self.nota31 = IntVar()
        self.nota32 = IntVar()
        self.nota33 = IntVar()
        self.nota41 = IntVar()
        self.nota42 = IntVar()
        self.nota43 = IntVar()
        self.nota51 = IntVar()
        self.nota52 = IntVar()
        self.nota53 = IntVar()
        self.nota61 = IntVar()
        self.nota62 = IntVar()
        self.nota63 = IntVar()
        self.nota71 = IntVar()
        self.nota72 = IntVar()
        self.nota73 = IntVar()
        self.nota81 = IntVar()
        self.nota82 = IntVar()
        self.nota83 = IntVar()
        self.nota91 = IntVar()
        self.nota92 = IntVar()
        self.nota93 = IntVar()
        # los 30000 widgets
        self.label_nro_registro = Label(self.frame, text='Numero de Registro')
        self.label_nro_registro.grid(pady=0, row=1, column=0, sticky=E + W)
        self.label_usuario = Label(self.frame, text='Usuario')
        self.label_usuario.grid(pady=0, row=2, column=0, sticky=E + W)
        self.label_clave = Label(self.frame, text='clave')
        self.label_clave.grid(pady=0, row=3, column=0, sticky=E + W)
        self.label_nombre = Label(self.frame, text='nombre')
        self.label_nombre.grid(pady=0, row=4, column=0, sticky=E + W)
        self.label_apellido = Label(self.frame, text='apellido')
        self.label_apellido.grid(pady=0, row=5, column=0, sticky=E + W)
        self.label_dni = Label(self.frame, text='DNI')
        self.label_dni.grid(pady=0, row=6, column=0, sticky=E + W)
        self.label_direccion = Label(self.frame, text='direccion')
        self.label_direccion.grid(pady=0, row=7, column=0, sticky=E + W)
        self.label_telefono = Label(self.frame, text='telefono')
        self.label_telefono.grid(pady=0, row=8, column=0, sticky=E + W)
        self.label_email = Label(self.frame, text='email')
        self.label_email.grid(pady=0, row=9, column=0, sticky=E + W)
        self.label_nacimiento = Label(self.frame, text='nacimiento dd,mm,aaaa')
        self.label_nacimiento.grid(pady=0, row=10, column=0, sticky=E + W)
        self.label_curso = Label(self.frame, text='curso')
        self.label_curso.grid(pady=0, row=11, column=0, sticky=E + W)
        self.label_alta_colegio = Label(self.frame, text='alta colegio dd,mm,aaaa')
        self.label_alta_colegio.grid(pady=0, row=12, column=0, sticky=E + W)
        self.label_baja_colegio = Label(self.frame, text='baja colegio dd,mm,aaaa')
        self.label_baja_colegio.grid(pady=0, row=13, column=0, sticky=E + W)
        self.label_concepto = Label(self.frame, text='concepto')
        self.label_concepto.grid(pady=0, row=14, column=0, sticky=E + W)
        self.label_inasistencia = Label(self.frame, text='inasistencia')
        self.label_inasistencia.grid(pady=0, row=15, column=0, sticky=E + W)
        self.label_nota11 = Label(self.frame, text='Nota Matematica 1')
        self.label_nota11.grid(pady=0, row=16, column=0, sticky=E + W)
        self.label_nota12 = Label(self.frame, text='Nota Matematica 2')
        self.label_nota12.grid(pady=0, row=17, column=0, sticky=E + W)
        self.label_nota13 = Label(self.frame, text='Nota Matematica 3')
        self.label_nota13.grid(pady=0, row=18, column=0, sticky=E + W)
        self.label_nota21 = Label(self.frame, text='Nota Lengua 1')
        self.label_nota21.grid(pady=0, row=19, column=0, sticky=E + W)
        self.label_nota22 = Label(self.frame, text='Nota Lengua 2')
        self.label_nota22.grid(pady=0, row=20, column=0, sticky=E + W)
        self.label_nota23 = Label(self.frame, text='Nota Lengua 3')
        self.label_nota23.grid(pady=0, row=21, column=0, sticky=E + W)

        self.label_nota31 = Label(self.frame, text='Nota Fisica 1')
        self.label_nota31.grid(pady=0, row=1, column=2, sticky=E + W)
        self.label_nota32 = Label(self.frame, text='Nota Fisica 2')
        self.label_nota32.grid(pady=0, row=2, column=2, sticky=E + W)
        self.label_nota33 = Label(self.frame, text='Nota Fisica 3')
        self.label_nota33.grid(pady=0, row=3, column=2, sticky=E + W)
        self.label_nota41 = Label(self.frame, text='Nota Quimica 1')
        self.label_nota41.grid(pady=0, row=4, column=2, sticky=E + W)
        self.label_nota42 = Label(self.frame, text='Nota Quimica 2')
        self.label_nota42.grid(pady=0, row=5, column=2, sticky=E + W)
        self.label_nota43 = Label(self.frame, text='Nota Quimica 3')
        self.label_nota43.grid(pady=0, row=6, column=2, sticky=E + W)
        self.label_nota51 = Label(self.frame, text='Nota Biologia 1')
        self.label_nota51.grid(pady=0, row=7, column=2, sticky=E + W)
        self.label_nota52 = Label(self.frame, text='Nota Biologia 2')
        self.label_nota52.grid(pady=0, row=8, column=2, sticky=E + W)
        self.label_nota53 = Label(self.frame, text='Nota Biologia 3')
        self.label_nota53.grid(pady=0, row=9, column=2, sticky=E + W)
        self.label_nota61 = Label(self.frame, text='Nota Etica 1')
        self.label_nota61.grid(pady=0, row=10, column=2, sticky=E + W)
        self.label_nota62 = Label(self.frame, text='Nota Etica 2')
        self.label_nota62.grid(pady=0, row=11, column=2, sticky=E + W)
        self.label_nota63 = Label(self.frame, text='Nota Etica 3')
        self.label_nota63.grid(pady=0, row=12, column=2, sticky=E + W)
        self.label_nota71 = Label(self.frame, text='Nota Historia 1')
        self.label_nota71.grid(pady=0, row=13, column=2, sticky=E + W)
        self.label_nota72 = Label(self.frame, text='Nota Historia 2')
        self.label_nota72.grid(pady=0, row=14, column=2, sticky=E + W)
        self.label_nota73 = Label(self.frame, text='Nota Historia 3')
        self.label_nota73.grid(pady=0, row=15, column=2, sticky=E + W)
        self.label_nota81 = Label(self.frame, text='Nota Geografia 1')
        self.label_nota81.grid(pady=0, row=16, column=2, sticky=E + W)
        self.label_nota82 = Label(self.frame, text='Nota Geografia 2')
        self.label_nota82.grid(pady=0, row=17, column=2, sticky=E + W)
        self.label_nota83 = Label(self.frame, text='Nota Geografia 3')
        self.label_nota83.grid(pady=0, row=18, column=2, sticky=E + W)
        self.label_nota91 = Label(self.frame, text='Nota Computacion 1')
        self.label_nota91.grid(pady=0, row=19, column=2, sticky=E + W)
        self.label_nota92 = Label(self.frame, text='Nota Computacion 2')
        self.label_nota92.grid(pady=0, row=20, column=2, sticky=E + W)
        self.label_nota93 = Label(self.frame, text='Nota Computacion 3')
        self.label_nota93.grid(pady=0, row=21, column=2, sticky=E + W)
        # Campos de texto
        self.entry_nro_registro = Entry(self.frame, textvariable=self.nro_registro)
        self.entry_nro_registro.grid(pady=0, row=1, column=1, sticky=E + W)
        self.entry_usuario = Entry(self.frame, textvariable=self.usuario)
        self.entry_usuario.grid(pady=0, row=2, column=1, sticky=E + W)
        self.entry_clave = Entry(self.frame, textvariable=self.clave)
        self.entry_clave.grid(pady=0, row=3, column=1, sticky=E + W)
        self.entry_nombre = Entry(self.frame, textvariable=self.nombre)
        self.entry_nombre.grid(pady=0, row=4, column=1, sticky=E + W)
        self.entry_apellido = Entry(self.frame, textvariable=self.apellido)
        self.entry_apellido.grid(pady=0, row=5, column=1, sticky=E + W)
        self.entry_dni = Entry(self.frame, textvariable=self.dni)
        self.entry_dni.grid(pady=0, row=6, column=1, sticky=E + W)
        self.entry_direccion = Entry(self.frame, textvariable=self.direccion)
        self.entry_direccion.grid(pady=0, row=7, column=1, sticky=E + W)
        self.entry_telefono = Entry(self.frame, textvariable=self.telefono)
        self.entry_telefono.grid(pady=0, row=8, column=1, sticky=E + W)
        self.entry_email = Entry(self.frame, textvariable=self.email)
        self.entry_email.grid(pady=0, row=9, column=1, sticky=E + W)
        self.entry_nacimiento = Entry(self.frame, textvariable=self.nacimientos)
        self.entry_nacimiento.grid(pady=0, row=10, column=1, sticky=E + W)
        self.entry_curso = Entry(self.frame, textvariable=self.curso)
        self.entry_curso.grid(pady=0, row=11, column=1, sticky=E + W)
        self.entry_alta_colegio = Entry(self.frame, textvariable=self.alta_colegios)
        self.entry_alta_colegio.grid(pady=0, row=12, column=1, sticky=E + W)
        self.entry_baja_colegio = Entry(self.frame, textvariable=self.baja_colegios)
        self.entry_baja_colegio.grid(pady=0, row=13, column=1, sticky=E + W)
        self.om_selected.set('MA')
        self.opt1 = OptionMenu(self.frame, self.om_selected, 'MA', 'A', 'NA')
        self.opt1.grid(pady=0, row=14, column=1, sticky=E + W)
        self.entry_inasistencia = Entry(self.frame, textvariable=self.inasistencia)
        self.entry_inasistencia.grid(pady=0, row=15, column=1, sticky=E + W)
        self.entry_nota11 = Entry(self.frame, textvariable=self.nota11)
        self.entry_nota11.grid(pady=0, row=16, column=1, sticky=E + W)
        self.entry_nota12 = Entry(self.frame, textvariable=self.nota12)
        self.entry_nota12.grid(pady=0, row=17, column=1, sticky=E + W)
        self.entry_nota13 = Entry(self.frame, textvariable=self.nota13)
        self.entry_nota13.grid(pady=0, row=18, column=1, sticky=E + W)
        self.entry_nota21 = Entry(self.frame, textvariable=self.nota21)
        self.entry_nota21.grid(pady=0, row=19, column=1, sticky=E + W)
        self.entry_nota22 = Entry(self.frame, textvariable=self.nota22)
        self.entry_nota22.grid(pady=0, row=20, column=1, sticky=E + W)
        self.entry_nota23 = Entry(self.frame, textvariable=self.nota23)
        self.entry_nota23.grid(pady=0, row=21, column=1, sticky=E + W)

        self.entry_nota31 = Entry(self.frame, textvariable=self.nota31)
        self.entry_nota31.grid(pady=0, row=1, column=3, sticky=E + W)
        self.entry_nota32 = Entry(self.frame, textvariable=self.nota32)
        self.entry_nota32.grid(pady=0, row=2, column=3, sticky=E + W)
        self.entry_nota33 = Entry(self.frame, textvariable=self.nota33)
        self.entry_nota33.grid(pady=0, row=3, column=3, sticky=E + W)
        self.entry_nota41 = Entry(self.frame, textvariable=self.nota41)
        self.entry_nota41.grid(pady=0, row=4, column=3, sticky=E + W)
        self.entry_nota42 = Entry(self.frame, textvariable=self.nota42)
        self.entry_nota42.grid(pady=0, row=5, column=3, sticky=E + W)
        self.entry_nota43 = Entry(self.frame, textvariable=self.nota43)
        self.entry_nota43.grid(pady=0, row=6, column=3, sticky=E + W)
        self.entry_nota51 = Entry(self.frame, textvariable=self.nota51)
        self.entry_nota51.grid(pady=0, row=7, column=3, sticky=E + W)
        self.entry_nota52 = Entry(self.frame, textvariable=self.nota52)
        self.entry_nota52.grid(pady=0, row=8, column=3, sticky=E + W)
        self.entry_nota53 = Entry(self.frame, textvariable=self.nota53)
        self.entry_nota53.grid(pady=0, row=9, column=3, sticky=E + W)
        self.entry_nota61 = Entry(self.frame, textvariable=self.nota61)
        self.entry_nota61.grid(pady=0, row=10, column=3, sticky=E + W)
        self.entry_nota62 = Entry(self.frame, textvariable=self.nota62)
        self.entry_nota62.grid(pady=0, row=11, column=3, sticky=E + W)
        self.entry_nota63 = Entry(self.frame, textvariable=self.nota63)
        self.entry_nota63.grid(pady=0, row=12, column=3, sticky=E + W)
        self.entry_nota71 = Entry(self.frame, textvariable=self.nota71)
        self.entry_nota71.grid(pady=0, row=13, column=3, sticky=E + W)
        self.entry_nota72 = Entry(self.frame, textvariable=self.nota72)
        self.entry_nota72.grid(pady=0, row=14, column=3, sticky=E + W)
        self.entry_nota73 = Entry(self.frame, textvariable=self.nota73)
        self.entry_nota73.grid(pady=0, row=15, column=3, sticky=E + W)
        self.entry_nota81 = Entry(self.frame, textvariable=self.nota81)
        self.entry_nota81.grid(pady=0, row=16, column=3, sticky=E + W)
        self.entry_nota82 = Entry(self.frame, textvariable=self.nota82)
        self.entry_nota82.grid(pady=0, row=17, column=3, sticky=E + W)
        self.entry_nota83 = Entry(self.frame, textvariable=self.nota83)
        self.entry_nota83.grid(pady=0, row=18, column=3, sticky=E + W)
        self.entry_nota91 = Entry(self.frame, textvariable=self.nota91)
        self.entry_nota91.grid(pady=0, row=19, column=3, sticky=E + W)
        self.entry_nota92 = Entry(self.frame, textvariable=self.nota92)
        self.entry_nota92.grid(pady=0, row=20, column=3, sticky=E + W)
        self.entry_nota93 = Entry(self.frame, textvariable=self.nota93)
        self.entry_nota93.grid(pady=0, row=21, column=3, sticky=E + W)

        self.label_error = Label(self.frame, text=' ')
        self.label_error.grid(pady=0, row=22, column=0, sticky=E + W)
        self.label_error.config(fg='red')

        self.button_consultar = Button(self.frame, text="Consultar", command=self.consultar)
        self.button_consultar.grid(pady=0, row=23, column=1, sticky=E + W)
        self.button_modificar = Button(self.frame, text="Modificar", command=self.modificar)
        self.button_modificar.grid(pady=0, row=23, column=2, sticky=E + W)

        self.button_volver = Button(self.frame, text='Volver', command=lambda: swap_view(self, 'MP'))
        self.button_volver.grid(pady=0, row=24, column=0, sticky=E + W)

        # Center
        center(master)

    def consultar(self):
        global talumno
        self.label_error.config(text=' ')
        try:
            nroreg = int(self.nro_registro.get())
            alumno = talumno.buscar_alumno(nroreg)
            if alumno is None:
                self.label_error.config(text='El numero de registro no existe')
            else:
                self.usuario.set(alumno.get_usuario())
                self.clave.set(alumno.get_clave())
                self.nombre.set(alumno.get_nombre())
                self.apellido.set(alumno.get_apellido())
                self.dni.set(alumno.get_dni())
                self.direccion.set(alumno.get_direccion())
                self.telefono.set(alumno.get_telefono())
                self.email.set(alumno.get_email())
                nacimiento1 = str(alumno.get_nacimiento())
                self.nacimientos.set(nacimiento1)
                self.curso.set(alumno.get_curso())
                alta1 = str(alumno.get_alta())
                self.alta_colegios.set(alta1)
                baja1 = str(alumno.get_baja())
                self.baja_colegios.set(baja1)
                self.om_selected.set(alumno.get_concepto())
                self.inasistencia.set(alumno.get_inasistencia())
                mats = alumno.get_materias()
                self.nota11.set(mats[0].get_calificacion1er())
                self.nota12.set(mats[0].get_calificacion2do())
                self.nota13.set(mats[0].get_calificacion3er())
                self.nota21.set(mats[1].get_calificacion1er())
                self.nota22.set(mats[1].get_calificacion2do())
                self.nota23.set(mats[1].get_calificacion3er())
                self.nota31.set(mats[2].get_calificacion1er())
                self.nota32.set(mats[2].get_calificacion2do())
                self.nota33.set(mats[2].get_calificacion3er())
                self.nota41.set(mats[3].get_calificacion1er())
                self.nota42.set(mats[3].get_calificacion2do())
                self.nota43.set(mats[3].get_calificacion3er())
                self.nota51.set(mats[4].get_calificacion1er())
                self.nota52.set(mats[4].get_calificacion2do())
                self.nota53.set(mats[4].get_calificacion3er())
                self.nota61.set(mats[5].get_calificacion1er())
                self.nota62.set(mats[5].get_calificacion2do())
                self.nota63.set(mats[5].get_calificacion3er())
                self.nota71.set(mats[6].get_calificacion1er())
                self.nota72.set(mats[6].get_calificacion2do())
                self.nota73.set(mats[6].get_calificacion3er())
                self.nota81.set(mats[7].get_calificacion1er())
                self.nota82.set(mats[7].get_calificacion2do())
                self.nota83.set(mats[7].get_calificacion3er())
                self.nota91.set(mats[8].get_calificacion1er())
                self.nota92.set(mats[8].get_calificacion2do())
                self.nota93.set(mats[8].get_calificacion3er())
        except SyntaxError:
            self.label_error.config(text='Hay campos con errores')

    def modificar(self):
        global talumno
        self.label_error.config(text=' ')
        try:
            nroreg = int(self.nro_registro.get())
            alumno = talumno.buscar_alumno(nroreg)
            if alumno is None:
                self.label_error.config(text='El numero de registro no existe')
            else:
                us = str(self.usuario.get())
                cl = str(self.clave.get())
                no = str(self.nombre.get())
                ap = str(self.apellido.get())
                dn = self.dni.get()
                di = str(self.direccion.get())
                te = self.telefono.get()
                em = str(self.email.get())
                na = eval(str(self.nacimientos.get()))
                cu = str(self.curso.get())
                al = eval(str(self.alta_colegios.get()))
                ba = eval(str(self.baja_colegios.get()))
                co = str(self.om_selected.get())
                ina = self.inasistencia.get()
                mats = alumno.get_materias()
                n11 = self.nota11.get()
                n12 = self.nota12.get()
                n13 = self.nota13.get()
                n21 = self.nota21.get()
                n22 = self.nota22.get()
                n23 = self.nota23.get()
                n31 = self.nota31.get()
                n32 = self.nota32.get()
                n33 = self.nota33.get()
                n41 = self.nota41.get()
                n42 = self.nota42.get()
                n43 = self.nota43.get()
                n51 = self.nota51.get()
                n52 = self.nota52.get()
                n53 = self.nota53.get()
                n61 = self.nota61.get()
                n62 = self.nota62.get()
                n63 = self.nota63.get()
                n71 = self.nota71.get()
                n72 = self.nota72.get()
                n73 = self.nota73.get()
                n81 = self.nota81.get()
                n82 = self.nota82.get()
                n83 = self.nota83.get()
                n91 = self.nota91.get()
                n92 = self.nota92.get()
                n93 = self.nota93.get()
                mats[0].set_calificacion1er(n11)
                mats[0].set_calificacion2do(n12)
                mats[0].set_calificacion3er(n13)
                mats[1].set_calificacion1er(n21)
                mats[1].set_calificacion2do(n22)
                mats[1].set_calificacion3er(n23)
                mats[2].set_calificacion1er(n31)
                mats[2].set_calificacion2do(n32)
                mats[2].set_calificacion3er(n33)
                mats[3].set_calificacion1er(n41)
                mats[3].set_calificacion2do(n42)
                mats[3].set_calificacion3er(n43)
                mats[4].set_calificacion1er(n51)
                mats[4].set_calificacion2do(n52)
                mats[4].set_calificacion3er(n53)
                mats[5].set_calificacion1er(n61)
                mats[5].set_calificacion2do(n62)
                mats[5].set_calificacion3er(n63)
                mats[6].set_calificacion1er(n71)
                mats[6].set_calificacion2do(n72)
                mats[6].set_calificacion3er(n73)
                mats[7].set_calificacion1er(n81)
                mats[7].set_calificacion2do(n82)
                mats[7].set_calificacion3er(n83)
                mats[8].set_calificacion1er(n91)
                mats[8].set_calificacion2do(n92)
                mats[8].set_calificacion3er(n93)
                alumno.mod_alumno(us, cl, no, ap, dn, di, te, em, na, cu, al, ba, co, ina, mats)
                talumno.cargar_alumno(alumno)
        except SyntaxError:
            self.label_error.config(text='Hay campos con errores')
        except:
            self.label_error.config(text='Hay campos con valores invalidos')

    def terminate(self):
        self.frame.pack_forget()
        self.frame.destroy()


# ******************************************************************************************************************** #
class TablaA(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Tabla de Alumnos')

        self.button_volver = Button(self.frame, text='Volver', command=lambda: swap_view(self, 'MP'))
        self.button_volver.grid(row=0, column=1, sticky=E)

        self.table = Table(self.frame,
                           ['Nro de Registro', 'Nombre', 'Apellido', 'DNI', 'Dirección', 'Telefono', 'e-mail',
                            'Nacimiento', 'Curso', 'Fehca Alta', 'Fecha Baja', 'Concepto', 'Inasistencia'],
                           column_minwidths=[None, None, None, None, None, None, None, None, None, None, None,
                                             None, None],
                           height=700)
        self.table.grid(row=0,
                        column=0,
                        padx=10,
                        pady=10,
                        sticky=E+W+N+S)

        global talumno
        alumnos_dic = talumno.get_lista()
        alumnos = alumnos_dic.values()
        for alumno in alumnos:
            re = alumno.get_numero_registro()
            no = alumno.get_nombre()
            ap = alumno.get_apellido()
            dn = alumno.get_dni()
            di = alumno.get_direccion()
            te = alumno.get_telefono()
            em = alumno.get_email()
            na = str(alumno.get_nacimiento())
            cu = alumno.get_curso()
            al = str(alumno.get_alta())
            ba = str(alumno.get_baja())
            co = alumno.get_concepto()
            ina = alumno.get_inasistencia()

            self.table.insert_row([re, no, ap, dn, di, te, em, na, cu, al, ba, co, ina])

        self.frame.update()
        center(master)

        self.frame.mainloop()

    def terminate(self):
        self.frame.pack_forget()
        self.frame.destroy()


# ******************************************************************************************************************** #
class TablaM(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Tabla de Materias')

        self.button_volver = Button(self.frame, text='Volver', command=lambda: swap_view(self, 'MP'))
        self.button_volver.grid(row=0, column=2, sticky=E)

        self.table = Table(self.frame,
                           ['Nro Registro', 'Codigo Materia', 'Nombre', 'Nota 1er Cuatrimeste', 'Nota 2do Cuatrimeste',
                            'Nota 3er Cuatrimeste'],
                           column_minwidths=[None, None, None, None, None, None],
                           height=700)
        self.table.grid(row=0,
                        column=0,
                        padx=10,
                        pady=10,
                        sticky=E+W+N+S)

        global talumno
        alumnos_dic = talumno.get_lista()
        alumnos = alumnos_dic.values()
        for alumno in alumnos:
            re = alumno.get_numero_registro()
            materias = alumno.get_materias()
            mate = materias[0]
            mate1 = mate.get_calificacion1er()
            mate2 = mate.get_calificacion2do()
            mate3 = mate.get_calificacion3er()
            leng = materias[1]
            leng1 = leng.get_calificacion1er()
            leng2 = leng.get_calificacion2do()
            leng3 = leng.get_calificacion3er()
            fisi = materias[2]
            fisi1 = fisi.get_calificacion1er()
            fisi2 = fisi.get_calificacion2do()
            fisi3 = fisi.get_calificacion3er()
            qui = materias[3]
            qui1 = qui.get_calificacion1er()
            qui2 = qui.get_calificacion2do()
            qui3 = qui.get_calificacion3er()
            bio = materias[4]
            bio1 = bio.get_calificacion1er()
            bio2 = bio.get_calificacion2do()
            bio3 = bio.get_calificacion3er()
            eti = materias[5]
            eti1 = eti.get_calificacion1er()
            eti2 = eti.get_calificacion2do()
            eti3 = eti.get_calificacion3er()
            his = materias[6]
            his1 = his.get_calificacion1er()
            his2 = his.get_calificacion2do()
            his3 = his.get_calificacion3er()
            geo = materias[7]
            geo1 = geo.get_calificacion1er()
            geo2 = geo.get_calificacion2do()
            geo3 = geo.get_calificacion3er()
            comp = materias[8]
            comp1 = comp.get_calificacion1er()
            comp2 = comp.get_calificacion2do()
            comp3 = comp.get_calificacion3er()

            self.table.insert_row([re, 0, 'Matematicas', mate1, mate2, mate3])
            self.table.insert_row([re, 1, 'Lengua', leng1, leng2, leng3])
            self.table.insert_row([re, 2, 'Fisica', fisi1, fisi2, fisi3])
            self.table.insert_row([re, 3, 'Quimica', qui1, qui2, qui3])
            self.table.insert_row([re, 4, 'Biologia', bio1, bio2, bio3])
            self.table.insert_row([re, 5, 'Etica', eti1, eti2, eti3])
            self.table.insert_row([re, 6, 'Historia', his1, his2, his3])
            self.table.insert_row([re, 7, 'Geografia', geo1, geo2, geo3])
            self.table.insert_row([re, 8, 'Computacion', comp1, comp2, comp3])

        self.frame.update()
        center(master)

        self.frame.mainloop()

    def terminate(self):
        self.frame.pack_forget()
        self.frame.destroy()


# ******************************************************************************************************************** #
class Legajo(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Legajo')
        self.__dni = IntVar()
        self.__label_dni = Label(self.frame,
                                 text="DNI:")
        self.__label_dni.grid(row=0,
                                column=0,
                                sticky=W)

        self.label_dni_incorrecto = Label(self.frame, text='', fg='red')
        self.label_dni_incorrecto.grid(row=2,
                                       column=0,
                                       columnspan=1,
                                       sticky=W+E)
        self.entry_dni = Entry(self.frame,
                                   textvariable=self.__dni)
        self.entry_dni.grid(pady=0,
                                row=1,
                                column=0,
                                sticky=E + W)
        self.button_buscar = Button(self.frame,
                                    text='Buscar',
                                    command=self.fill_tabla)
        self.button_buscar.grid(row=3,
                                column=0,
                                columnspan=1,
                                sticky=W)
        self.button_volver = Button(self.frame,
                                    text='Volver',
                                    command=lambda: swap_view(self,'MP'))
        self.button_volver.grid(row=3,
                                column=2,
                                columnspan=1,
                                sticky=W)
        self.table_dp = Table(self.frame,
                           ['Nro de Registro', 'Nombre', 'Apellido', 'DNI', 'Dirección', 'Telefono', 'e-mail',
                            'Nacimiento', 'Curso', 'Fehca Alta', 'Fecha Baja', 'Concepto', 'Inasistencia'],
                           column_minwidths=[None, None, None, None, None, None, None, None, None, None, None,
                                             None, None],
                           height=100)
        self.table_dp.grid(row=4,
                        column=0,
                        padx=10,
                        pady=10,
                        columnspan=3,
                        sticky=E + W + N + S)

        self.table_notas = Table(self.frame,
                           ['Codigo Materia', 'Nombre', 'Nota 1er Cuatrimeste', 'Nota 2do Cuatrimeste',
                            'Nota 3er Cuatrimeste'],
                           column_minwidths=[None, None, None, None, None],
                           height=300)
        self.table_notas.grid(row=5,
                        column=0,
                        padx=10,
                        pady=10,
                        columnspan=2,
                        sticky=E + W + N + S)

    def fill_tabla(self):
        global talumno
        dni_a = self.__dni.get()
        alumno = talumno.buscar_por_dni(dni_a)
        if alumno != None:
            re = alumno.get_numero_registro()
            no = alumno.get_nombre()
            ap = alumno.get_apellido()
            dn = alumno.get_dni()
            di = alumno.get_direccion()
            te = alumno.get_telefono()
            em = alumno.get_email()
            na = str(alumno.get_nacimiento())
            cu = alumno.get_curso()
            al = str(alumno.get_alta())
            ba = str(alumno.get_baja())
            co = alumno.get_concepto()
            ina = alumno.get_inasistencia()
            self.table_dp.insert_row([re, no, ap, dn, di, te, em, na, cu, al, ba, co, ina])
            materias = alumno.get_materias()
            mate = materias[0]
            mate1 = mate.get_calificacion1er()
            mate2 = mate.get_calificacion2do()
            mate3 = mate.get_calificacion3er()
            leng = materias[1]
            leng1 = leng.get_calificacion1er()
            leng2 = leng.get_calificacion2do()
            leng3 = leng.get_calificacion3er()
            fisi = materias[2]
            fisi1 = fisi.get_calificacion1er()
            fisi2 = fisi.get_calificacion2do()
            fisi3 = fisi.get_calificacion3er()
            qui = materias[3]
            qui1 = qui.get_calificacion1er()
            qui2 = qui.get_calificacion2do()
            qui3 = qui.get_calificacion3er()
            bio = materias[4]
            bio1 = bio.get_calificacion1er()
            bio2 = bio.get_calificacion2do()
            bio3 = bio.get_calificacion3er()
            eti = materias[5]
            eti1 = eti.get_calificacion1er()
            eti2 = eti.get_calificacion2do()
            eti3 = eti.get_calificacion3er()
            his = materias[6]
            his1 = his.get_calificacion1er()
            his2 = his.get_calificacion2do()
            his3 = his.get_calificacion3er()
            geo = materias[7]
            geo1 = geo.get_calificacion1er()
            geo2 = geo.get_calificacion2do()
            geo3 = geo.get_calificacion3er()
            comp = materias[8]
            comp1 = comp.get_calificacion1er()
            comp2 = comp.get_calificacion2do()
            comp3 = comp.get_calificacion3er()

            self.table_notas.insert_row([0, 'Matematicas', mate1, mate2, mate3])
            self.table_notas.insert_row([1, 'Lengua', leng1, leng2, leng3])
            self.table_notas.insert_row([2, 'Fisica', fisi1, fisi2, fisi3])
            self.table_notas.insert_row([3, 'Quimica', qui1, qui2, qui3])
            self.table_notas.insert_row([4, 'Biologia', bio1, bio2, bio3])
            self.table_notas.insert_row([5, 'Etica', eti1, eti2, eti3])
            self.table_notas.insert_row([6, 'Historia', his1, his2, his3])
            self.table_notas.insert_row([7, 'Geografia', geo1, geo2, geo3])
            self.table_notas.insert_row([8, 'Computacion', comp1, comp2, comp3])
        else:
            self.label_dni_incorrecto.config(text='No hay alumnos con dicho DNI')

    def terminate(self):
        self.frame.pack_forget()
        self.frame.destroy()

class Readmision(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Readmision')

        self.button_volver = Button(self.frame, text='Volver', command=lambda: swap_view(self, 'MP'))
        self.button_volver.grid(row=0, column=1, sticky=E)

        self.table = Table(self.frame,
                           ['Nombre', 'Apellido', 'Curso', 'Concepto', 'Inasistencia'],
                           column_minwidths=[None, None, None, None, None],
                           height=700)
        self.table.grid(row=0,
                        column=0,
                        padx=10,
                        pady=10,
                        sticky=E + W + N + S)

        global talumno
        faltantes = talumno.buscar_por_readmision()
        for alumno in faltantes:
            no = alumno.get_nombre()
            ap = alumno.get_apellido()
            cu = alumno.get_curso()
            co = alumno.get_concepto()
            ina = alumno.get_inasistencia()

            self.table.insert_row([no, ap, cu, co, ina])

        self.frame.update()

    def terminate(self):
        self.frame.pack_forget()
        self.frame.destroy()



class Curso(Frame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.frame = Frame(master)
        self.frame.pack()
        # Set title
        master.title('Alumnos por curso')

        self.button_volver = Button(self.frame, text='Volver', command=lambda: swap_view(self, 'MP'))
        self.button_volver.grid(row=0, column=1, sticky=E)

        print(talumno.buscar_por_curso(5))

    def terminate(self):
        self.frame.pack_forget()
        self.frame.destroy()


root = Tk()
# Set login
Login(root)
# Start
root.mainloop()
