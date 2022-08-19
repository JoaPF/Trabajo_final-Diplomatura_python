from tkinter import Tk
from vista import Ventana
from modelo import Conexion
"""
Joaquín Pérez Figueira
joaquinperezfigueira@gmail.com
"""
conbd = Conexion()

if __name__ == "__main__":
    conbd.intentar_conexion()

    root = Tk()
    app = Ventana(master=root)
    app.mainloop()
