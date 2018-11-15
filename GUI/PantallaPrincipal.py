import tkinter as tk
# import tkinter.ttk as tkk
from Clases.BD_Escuela import BD_Escuela
FUENTE = 'Tahoma'
TAMANOF = '14'

class Login:
    # Constantes


    def __init__(self):
        # crear ventana
        self.login = tk.Tk()
        # Variables para usar en widgets
        self.usuario = tk.StringVar()
        self.clave = tk.StringVar()
        self.om_selected = tk.StringVar()
        self.om_selected.set('Programador')
        # Apariencia ventana
        self.login.title('Iniciar Sesion')
        w = 640  # ancho
        h = 480  # alto
        # alto y ancho de la pantalla
        ws = self.login.winfo_screenwidth()  # ancho de la pantalla
        hs = self.login.winfo_screenheight()  # alto de la pantalla
        # calculo el lugar para que la ventana este centrada
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.login.geometry('%dx%d+%d+%d' % (w, h, x, y))
        # Creo la matriz
        self.login.columnconfigure(0, weight=0)
        self.login.columnconfigure(1, weight=1)
        self.login.columnconfigure(2, weight=1)
        self.login.columnconfigure(3, weight=1)
        self.login.columnconfigure(4, weight=0)
        self.login.rowconfigure(0, weight=1)
        self.login.rowconfigure(1, weight=1)
        self.login.rowconfigure(2, weight=1)
        self.login.rowconfigure(3, weight=1)
        self.login.rowconfigure(4, weight=1)
        self.login.rowconfigure(5, weight=1)
        self.login.rowconfigure(6, weight=1)
        self.login.rowconfigure(7, weight=1)
        self.login.rowconfigure(8, weight=1)
        # Agregar widgets
        # Labels
        self.label_usuario = tk.Label(self.login,
                                      text="Usuario:")
        self.label_usuario.grid(row=2,
                                column=1,
                                sticky=tk.E)
        self.label_clave = tk.Label(self.login,
                                    text="Contraseña:")
        self.label_clave.grid(row=3,
                              column=1,
                              sticky=tk.E + tk.N)
        self.label_usr_incorrecto = tk.Label(self.login, text='El usuario no existe')
        self.label_usr_incorrecto.grid(row=2,
                                       column=3,
                                       sticky=tk.E)
        self.label_usr_incorrecto.config(fg='red')
        self.label_usr_incorrecto.grid_remove()
        self.label_pass_incorrecta = tk.Label(self.login, text='La clave es incorrecta')
        self.label_pass_incorrecta.grid(row=3,
                                        column=3,
                                        sticky=tk.E)
        self.label_pass_incorrecta.config(fg='red')
        self.label_pass_incorrecta.grid_remove()
        # Campos de texto
        self.entry_usuario = tk.Entry(self.login,
                                      textvariable=self.usuario)
        self.entry_usuario.grid(pady=0,
                                row=2,
                                column=2,
                                sticky=tk.E + tk.W)
        self.entry_clave = tk.Entry(self.login,
                                    show='•',
                                    font=(FUENTE, TAMANOF),
                                    textvariable=self.clave)
        self.entry_clave.grid(row=3,
                              column=2,
                              sticky=tk.E + tk.W + tk.N)
        # Option Menu
        self.opt1 = tk.OptionMenu(self.login, self.om_selected, 'Programador', 'Docente', 'Alumno')
        self.opt1.grid(pady=0,
                       ipadx=75,
                       row=4,
                       column=1,
                       columnspan=3,
                       sticky=tk.N)
        # Botones
        self.button_acceder = tk.Button(self.login,
                                        text="Acceder",
                                        command=self.comprobar_clave)
        self.button_acceder.grid(pady=0,
                                 ipadx=75,
                                 row=6,
                                 column=1,
                                 columnspan=3,
                                 sticky=tk.N)
        # Main loop
        self.login.mainloop()

    def comprobar_clave(self):
        self.label_pass_incorrecta.grid_remove()
        self.label_usr_incorrecto.grid_remove()
        bd = BD_Escuela()
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
                self.login.destroy()
                app = SeaofBTCapp()
                app.mainloop()
            else:
                self.label_pass_incorrecta.grid()
        except KeyError:
            self.label_usr_incorrecto.grid()


# ******************************************************************************************************************** #
class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MenuPrincipalP, Reg_Us):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MenuPrincipalP)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# ******************************************************************************************************************** #
class MenuPrincipalP(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Variables para usar en widgets
        # Apariencia ventana
        self._name.title('Menu Principal')
        '''w = 640  # ancho
        h = 640  # alto
        # alto y ancho de la pantalla
        ws = self.winfo_screenwidth()  # width of the screen
        hs = self.winfo_screenheight()  # height of the screen
        # calculo el lugar para que la ventana este centrada
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2) - 30  # Subo un poco la pantalla
        self.size('%dx%d+%d+%d' % (w, h, x, y))'''
        # Creo la matriz
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        # Botones
        self.button_reg_us = tk.Button(self,
                                       text="Registrar Usuario",
                                       command=lambda: controller.show_frame(Reg_Us))
        self.button_reg_us.grid(pady=0,
                                ipadx=75,
                                row=1,
                                column=0,
                                columnspan=1,
                                sticky=tk.E + tk.W)
        self.button_elim_us = tk.Button(self,
                                        text="Eliminar Usuario",
                                        command=self.reg_us())
        self.button_elim_us.grid(pady=0,
                                 ipadx=75,
                                 row=2,
                                 column=0,
                                 columnspan=1,
                                 sticky=tk.E + tk.W)
        self.button_carga_bd = tk.Button(self,
                                         text="Inicializar sesión de trabajo",
                                         command=self.reg_us())
        self.button_carga_bd.grid(pady=0,
                                  ipadx=75,
                                  row=3,
                                  column=0,
                                  columnspan=1,
                                  sticky=tk.E + tk.W)
        self.button_abmc_alu = tk.Button(self,
                                         text="ABMC Alumno",
                                         command=self.reg_us())
        self.button_abmc_alu.grid(pady=0,
                                  ipadx=75,
                                  row=4,
                                  column=0,
                                  columnspan=1,
                                  sticky=tk.E + tk.W)
        self.button_abmc_mat = tk.Button(self,
                                         text="ABMC Materias",
                                         command=self.reg_us())
        self.button_abmc_mat.grid(pady=0,
                                  ipadx=75,
                                  row=5,
                                  column=0,
                                  columnspan=1,
                                  sticky=tk.E + tk.W)
        self.button_back_up = tk.Button(self,
                                        text="BackUp",
                                        command=self.reg_us())
        self.button_back_up.grid(pady=50,
                                 ipadx=75,
                                 row=0,
                                 column=0,
                                 columnspan=2,
                                 sticky=tk.N + tk.E + tk.W)
        self.button_list_t_alu = tk.Button(self,
                                           text="Tabla Alumnos",
                                           command=self.reg_us())
        self.button_list_t_alu.grid(pady=0,
                                    ipadx=0,
                                    row=1,
                                    column=1,
                                    columnspan=1,
                                    sticky=tk.E + tk.W)
        self.button_list_t_mat = tk.Button(self,
                                           text="Tabla Materias",
                                           command=self.reg_us())
        self.button_list_t_mat.grid(pady=0,
                                    ipadx=75,
                                    row=2,
                                    column=1,
                                    columnspan=1,
                                    sticky=tk.E + tk.W)
        self.button_list_leg_a = tk.Button(self,
                                           text="Legajo",
                                           command=self.reg_us())
        self.button_list_leg_a.grid(pady=0,
                                    ipadx=75,
                                    row=3,
                                    column=1,
                                    columnspan=1,
                                    sticky=tk.E + tk.W)
        self.button_list_inas = tk.Button(self,
                                          text="Solicitudes de readmision",
                                          command=self.reg_us())
        self.button_list_inas.grid(pady=0,
                                   ipadx=75,
                                   row=4,
                                   column=1,
                                   columnspan=1,
                                   sticky=tk.E + tk.W)
        self.button_lis_reg_curso = tk.Button(self,
                                              text="Listado Alumnos",
                                              command=self.reg_us())
        self.button_lis_reg_curso.grid(pady=0,
                                       ipadx=75,
                                       row=5,
                                       column=1,
                                       columnspan=1,
                                       sticky=tk.E + tk.W)

    def reg_us(self):
        # bd = BD_Escuela()
        ru = Reg_Us(self)

    def elim_us(self):
        bd = BD_Escuela()

    def carga_bd(self):
        bd = BD_Escuela()

    def abmc_alu(self):
        bd = BD_Escuela()

    def abmc_mat(self):
        bd = BD_Escuela()

    def back_up(self):
        bd = BD_Escuela()

    def list_t_alu(self):
        bd = BD_Escuela()

    def list_t_mat(self):
        bd = BD_Escuela()

    def list_leg_a(self):
        bd = BD_Escuela()

    def list_inas(self):
        bd = BD_Escuela()

    def lis_reg_curso(self):
        bd = BD_Escuela()


# ******************************************************************************************************************** #
class Reg_Us(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # Variables para usar en widgets
        # Apariencia ventana
        self.tk.title('Registrar Usuario')
        '''w = 640  # ancho
        h = 480  # alto
        # alto y ancho de la pantalla
        ws = self.winfo_screenwidth()  # width of the screen
        hs = self.winfo_screenheight()  # height of the screen
        # calculo el lugar para que la ventana este centrada
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2) - 30  # Subo un poco la pantalla
        self.tk.geometry('%dx%d+%d+%d' % (w, h, x, y))'''
        # Creo la matriz
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=0)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)
        # Agregar widgets
        self.usuario = tk.StringVar()
        self.clave = tk.StringVar()
        self.om_selected = tk.StringVar()
        self.om_selected.set('Programador')
        # Labels
        self.label_usuario = tk.Label(self,
                                      text="Usuario:")
        self.label_usuario.grid(row=2,
                                column=1,
                                sticky=tk.E)
        self.label_clave = tk.Label(self,
                                    text="Contraseña:")
        self.label_clave.grid(row=3,
                              column=1,
                              sticky=tk.E + tk.N)
        self.label_usr_incorrecto = tk.Label(self, text='El usuario no existe')
        self.label_usr_incorrecto.grid(row=2,
                                       column=3,
                                       sticky=tk.E)
        self.label_usr_incorrecto.config(fg='red')
        self.label_usr_incorrecto.grid_remove()
        self.label_pass_incorrecta = tk.Label(self, text='La clave es incorrecta')
        self.label_pass_incorrecta.grid(row=3,
                                        column=3,
                                        sticky=tk.E)
        self.label_pass_incorrecta.config(fg='red')
        self.label_pass_incorrecta.grid_remove()
        # Campos de texto
        self.entry_usuario = tk.Entry(self,
                                      textvariable=self.usuario)
        self.entry_usuario.grid(pady=0,
                                row=2,
                                column=2,
                                sticky=tk.E + tk.W)
        self.entry_clave = tk.Entry(self,
                                    show='•',
                                    font=(FUENTE, TAMANOF),
                                    textvariable=self.clave)
        self.entry_clave.grid(row=3,
                              column=2,
                              sticky=tk.E + tk.W + tk.N)
        # Option Menu
        self.opt1 = tk.OptionMenu(self, self.om_selected, 'Programador', 'Docente', 'Alumno')
        self.opt1.grid(pady=0,
                       ipadx=75,
                       row=4,
                       column=1,
                       columnspan=3,
                       sticky=tk.N)
        # Botones
        self.button_acceder = tk.Button(self,
                                        text="Registrar")
        # command=self.comprobar_clave)
        self.button_acceder.grid(pady=0,
                                 ipadx=75,
                                 row=6,
                                 column=1,
                                 columnspan=3,
                                 sticky=tk.N)
        # Main loop


plogin = Login()
