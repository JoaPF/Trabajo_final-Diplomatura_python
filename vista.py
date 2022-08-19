from tkinter import RAISED, W, Frame, Label, Entry, Button, ttk, IntVar, StringVar, END
import tkinter.font
from modelo import Metodos, Decos_log

logs = Decos_log


class Ventana(Frame):
    comandos = Metodos()

    def __init__(self, master=None):
        super().__init__(master, width=760, height=390)
        self.master = master
        self.pack()
        self.crear_ventana()

    @logs.sesion
    def crear_ventana(self):
        self.var_id = IntVar()
        self.var_nombre = StringVar()
        self.var_apellido = StringVar()
        self.var_num = IntVar()
        self.var_infoad = StringVar()

        # ------------------------------Label para el título------------------------------
        self.label_titulo = Label(self, text="Lista de contactos")
        tt = tkinter.font.Font(size=25)
        self.label_titulo["font"] = tt
        self.label_titulo.place(x=0, y=0, width=280, height=48)

        # ------------------------------Labels para señalar entrys------------------------------
        tamano_labels = tkinter.font.Font(size=10)

        self.label_nombre = tkinter.Label(self, text="Nombre del contacto:")
        self.label_nombre["font"] = tamano_labels
        self.label_nombre.place(x=7, y=48, width=125, height=30)

        self.label_apellido = tkinter.Label(self)
        self.label_apellido["font"] = tamano_labels
        self.label_apellido["text"] = "Apellido:"
        self.label_apellido.place(x=7, y=110, width=55, height=30)

        self.label_numero = tkinter.Label(self)
        self.label_numero["font"] = tamano_labels
        self.label_numero["text"] = "Nº de telefono:"
        self.label_numero.place(x=7, y=170, width=90, height=30)

        self.label_infoad = tkinter.Label(self)
        self.label_infoad["font"] = tamano_labels
        self.label_infoad["text"] = "Información adicional:"
        self.label_infoad.place(x=7, y=230, width=125, height=30)

        # ------------------------------Entrys------------------------------
        tamano_entrys = tkinter.font.Font(size=10)

        self.entrynombre = Entry(self, textvariable=self.var_nombre)
        self.entrynombre["borderwidth"] = "1px"
        self.entrynombre["font"] = tamano_entrys
        self.entrynombre["justify"] = "left"
        self.entrynombre.place(x=150, y=48, width=107, height=30)

        self.entryapellido = Entry(self, textvariable=self.var_apellido)
        self.entryapellido["borderwidth"] = "1px"
        self.entryapellido["font"] = tamano_entrys
        self.entryapellido["justify"] = "left"
        self.entryapellido.place(x=150, y=110, width=107, height=30)

        self.entrynum = Entry(self, textvariable=self.var_num)
        self.entrynum["borderwidth"] = "1px"
        self.entrynum["font"] = tamano_entrys
        self.entrynum["justify"] = "left"
        self.entrynum.place(x=150, y=170, width=107, height=30)

        self.entryinfo = Entry(self, textvariable=self.var_infoad)
        self.entryinfo["borderwidth"] = "1px"
        self.entryinfo["font"] = tamano_entrys
        self.entryinfo["justify"] = "left"
        self.entryinfo.place(x=150, y=230, width=107, height=30)

        # ------------------------------Botones------------------------------
        self.tamano_botones = tkinter.font.Font(size=10)
        self.bg_botones = "#efefef"
        self.fg_botones = "#000000"

        self.botoncargar = Button(self)
        self.botoncargar.config(bg=self.bg_botones,
                                fg=self.fg_botones,
                                font=self.tamano_botones)
        self.botoncargar["text"] = "Cargar"
        self.botoncargar.place(x=0, y=270, width=70, height=30)
        self.botoncargar["cursor"] = "top_side"
        self.botoncargar["command"] = lambda: self.comandos.cargar(self.treew,
                                                                   self.var_nombre.get(),
                                                                   self.var_apellido.get(),
                                                                   self.var_num.get(),
                                                                   self.var_infoad.get())

        self.botonborrar = Button(self)
        self.botonborrar.config(bg=self.bg_botones,
                                fg=self.fg_botones,
                                font=self.tamano_botones)
        self.botonborrar["text"] = "Borrar"
        self.botonborrar.place(x=0, y=310, width=70, height=30)
        self.botonborrar["cursor"] = "X_cursor"
        self.botonborrar["command"] = lambda: self.comandos.borrar(self.treew)

        self.botonmostrar = Button(self)
        self.botonmostrar.config(
            bg=self.bg_botones, fg=self.fg_botones, font=self.tamano_botones)
        self.botonmostrar["text"] = "Mostrar contactos"
        self.botonmostrar.place(x=90, y=270, width=167, height=30)
        self.botonmostrar["cursor"] = "bottom_side"
        self.botonmostrar["command"] = lambda: (print("Mostrando lista de contactos..."),
                                                self.comandos.actualizar_treeview(self.treew))

        self.botonmod = Button(self)
        self.botonmod.config(bg=self.bg_botones,
                             fg=self.fg_botones, font=self.tamano_botones)
        self.botonmod["text"] = "Modificar contacto"
        self.botonmod.place(x=90, y=310, width=167, height=30)
        self.botonmod["command"] = lambda: self.comandos.modificar(self.var_nombre.get(),
                                                                   self.var_apellido.get(),
                                                                   self.var_num.get(),
                                                                   self.var_infoad.get(),
                                                                   self.treew)
        self.botonmod["cursor"] = "pencil"

        self.botonsalir = Button(self)
        self.botonsalir.config(bg=self.bg_botones,
                               font=self.tamano_botones)
        self.botonsalir["text"] = "Salir"
        self.botonsalir.place(x=0, y=350, width=70, height=30)
        self.botonsalir["cursor"] = "X_cursor"
        self.botonsalir["fg"] = "red"
        self.botonsalir["command"] = self.comandos.salir

        self.botoninfo = Button(self)
        self.botoninfo.config(bg=self.bg_botones,
                              font=self.tamano_botones)
        self.botoninfo["text"] = "Acerca de"
        self.botoninfo.place(x=90, y=350, width=167, height=30)
        self.botoninfo["command"] = self.comandos.mostrar_info
        self.botoninfo["cursor"] = "plus"

        # ------------------------------Treeview------------------------------
        self.treew = ttk.Treeview(self)
        self.treew.place(x=265, y=48, width=493, height=340)
        self.treew["columns"] = ("Nombre", "Apellido", "Numero", "Infoad")
        self.treew.column("#0", width=40, anchor=W)
        self.treew.column("Nombre", width=80, anchor=W)
        self.treew.column("Apellido", width=80, anchor=W)
        self.treew.column("Numero", width=100, anchor=W)
        self.treew.column("Infoad", width=150, anchor=W)

        self.treew.heading("#0", text="ID", anchor=W)
        self.treew.heading("Nombre", text="Nombre")
        self.treew.heading("Apellido", text="Apellido")
        self.treew.heading("Numero", text="Teléfono")
        self.treew.heading("Infoad", text="Información adicional")
