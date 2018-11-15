from tkinter import *
# import tkinter.ttk as tkk
from Clases.BD_Escuela import BD_Escuela
from Clases.T_Alumnos import T_Alumnos

FUENTE = 'Tahoma'
TAMANOF = '14'

talumno = T_Alumnos()
bd = BD_Escuela()


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
        # Main loop
        self.frame.mainloop()

    def comprobar_clave(self):
        self.label_pass_incorrecta.grid_remove()
        self.label_usr_incorrecto.grid_remove()
        usuarios = bd.cargar_usuarios()
        usr = ''
        if self.om_selected.get() == 'Programador':
            usr = 'P-' + self.usuario.get()
        if self.om_selected.get() == 'Docente':
            usr = 'D-' + self.usuario.get()
        if self.om_selected.get() == 'Alumno':
            usr = 'A-' + self.usuario.get()
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
        self.button_reg_us = Button(self.frame,
                                    text='Registrar un Usuario',
                                    command=lambda: swap_view(self, 'registrar_usuario'))
        self.button_reg_us.grid(pady=0,
                                ipadx=75,
                                row=1,
                                column=0,
                                columnspan=1,
                                sticky=E + W)
        self.button_elim_us = Button(self.frame,
                                     text="Eliminar Usuario",
                                     command=lambda: swap_view(self, 'eliminar_usuario'))
        self.button_elim_us.grid(pady=0,
                                 ipadx=75,
                                 row=2,
                                 column=0,
                                 columnspan=1,
                                 sticky=E + W)
        self.button_carga_bd = Button(self.frame,
                                      text="Inicializar sesión de trabajo")
        self.button_carga_bd.grid(pady=0,
                                  ipadx=75,
                                  row=3,
                                  column=0,
                                  columnspan=1,
                                  sticky=E + W)
        self.button_abmc_alu = Button(self.frame,
                                      text="ABMC Alumno")
        self.button_abmc_alu.grid(pady=0,
                                  ipadx=75,
                                  row=4,
                                  column=0,
                                  columnspan=1,
                                  sticky=E + W)
        self.button_abmc_mat = Button(self.frame,
                                      text="ABMC Materias")
        self.button_abmc_mat.grid(pady=0,
                                  ipadx=75,
                                  row=5,
                                  column=0,
                                  columnspan=1,
                                  sticky=E + W)
        self.button_back_up = Button(self.frame,
                                     text="BackUp")
        self.button_back_up.grid(pady=50,
                                 ipadx=75,
                                 row=0,
                                 column=0,
                                 columnspan=2,
                                 sticky=N + E + W)
        self.button_list_t_alu = Button(self.frame,
                                        text="Tabla Alumnos")
        self.button_list_t_alu.grid(pady=0,
                                    ipadx=0,
                                    row=1,
                                    column=1,
                                    columnspan=1,
                                    sticky=E + W)
        self.button_list_t_mat = Button(self.frame,
                                        text="Tabla Materias")
        self.button_list_t_mat.grid(pady=0,
                                    ipadx=75,
                                    row=2,
                                    column=1,
                                    columnspan=1,
                                    sticky=E + W)
        self.button_list_leg_a = Button(self.frame,
                                        text="Legajo")
        self.button_list_leg_a.grid(pady=0,
                                    ipadx=75,
                                    row=3,
                                    column=1,
                                    columnspan=1,
                                    sticky=E + W)
        self.button_list_inas = Button(self.frame,
                                       text="Solicitudes de readmision")
        self.button_list_inas.grid(pady=0,
                                   ipadx=75,
                                   row=4,
                                   column=1,
                                   columnspan=1,
                                   sticky=E + W)
        self.button_lis_reg_curso = Button(self.frame,
                                           text="Listado Alumnos")
        self.button_lis_reg_curso.grid(pady=0,
                                       ipadx=75,
                                       row=5,
                                       column=1,
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

        self.label_usr_incorrecto = Label(self.frame, text='El usuario ya existe')
        self.label_usr_incorrecto.grid(row=2,
                                       column=4,
                                       sticky=E)
        self.label_usr_incorrecto.config(fg='red')
        self.label_usr_incorrecto.grid_remove()
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
                       columnspan=3,
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
        if usr == '' or clv == '':
            user = None
        if user is None:
            bd.registrar_usuario(usr, clv, usuarios)
        else:
            self.label_usr_incorrecto.grid()

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
            bd.eliminar_usuario(usr, usuarios)
            self.label_Estado.config(text='Si')
        else:
            self.label_usr_incorrecto.grid()

    def terminate(self):
        self.frame.pack_forget()
        self.frame.destroy()


root = Tk()
# Set login
Login(root)
# Start
root.mainloop()
