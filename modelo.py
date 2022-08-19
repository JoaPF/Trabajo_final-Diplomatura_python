import datetime
import sqlite3
from tkinter import messagebox

# -----------------
version = "v1.3.2"
# -----------------

class Decos_log:
    # Dentro de esta clase se encuentran todos los decoradores, que solo se usan para crear y editar un registro de log
    def sesion(vent):
        def envoltorio(*args):
            vent(*args)
            log = open("Log.txt", "a")
            frase = "Se ha iniciado sesion en el dia:" + "\n    "
            log.write(frase + str(datetime.datetime.now()) + "\n")
            log.close()
        return envoltorio

    def salida(vent):
        def envoltorio(*args):
            log = open("Log.txt", "a")
            frase = "Se ha cerrado sesion en el dia:" + "\n    "
            log.write(frase + str(datetime.datetime.now()) + "\n")
            log.close()
            vent(*args)
        return envoltorio

    def log_alta(alta):
        def envoltorio(*args):
            alta(*args)
            log = open("Log.txt", "a")
            frase = "Se ha agregado un contacto a la base de datos en el dia:" + "\n    "
            log.write(frase + str(datetime.datetime.now()) + "\n")
            log.close()
            print("Se ha agregado un contacto a la base de datos")
        return envoltorio

    def log_baja(baja):
        def envoltorio(*args):
            baja(*args)
            log = open("Log.txt", "a")
            frase = "Se ha eliminado un contacto de la base de datos en el dia:" + "\n    "
            log.write(frase + str(datetime.datetime.now()) + "\n")
            log.close()
        return envoltorio

    def log_modificacion(mod):
        def envoltorio(*args):
            mod(*args)
            log = open("Log.txt", "a")
            frase = "Se ha modificado un contacto de la base de datos en el dia:" + "\n    "
            log.write(frase + str(datetime.datetime.now()) + "\n")
            log.close()
        return envoltorio


class Conexion():
    # En esta clase se encuentra todo lo necesario para conectarse (o crear) la base de datos
    def conectar_base(self):
        con = sqlite3.connect("Listabd.db")
        return con

    def crear_tabla(self):
        con = self.conectar_base()
        cursor = con.cursor()
        sql = "CREATE TABLE IF NOT EXISTS contactos(id INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE text, APELLIDO text, TELEFONO integer, INFOAD text)"
        cursor.execute(sql)
        con.commit()

    def intentar_conexion(self):
        try:
            self.conectar_base()
            self.crear_tabla()
            print("Conectado a la base de datos")
        except:
            messagebox.showerror(title="ERROR",
                                 message="No fue posible conectarse a la base de datos")
            print("Error al conectarse a la base de datos")


conbd = Conexion()
logs = Decos_log


class Metodos():
    def mostrar_info(self):
        messagebox.showinfo(title="Acerca de",
                            message=version + "\nJoaquín Pérez Figueira\njoaquinperezfigueira@gmail.com")

    @logs.salida
    def salir(self):
        print("Adiós"), quit()

    def actualizar_treeview(self, treew):
        records = treew.get_children()
        for element in records:
            treew.delete(element)
        con = conbd.conectar_base()
        cursor = con.cursor()
        sql = "SELECT * FROM contactos ORDER BY id ASC"
        valores = cursor.execute(sql)
        resultado = valores.fetchall()
        for a in resultado:
            treew.insert("", 0, text=a[0], values=(a[1], a[2], a[3], a[4]))

    @logs.log_alta
    def cargar(self, treew, nombre, apellido, numero, infoad):
        try:
            con = conbd.conectar_base()
            cursor = con.cursor()
            data = (nombre, apellido, numero, infoad)
            sql = "INSERT INTO contactos(nombre, apellido, telefono, infoad) VALUES(?, ?, ?, ?)"
            cursor.execute(sql, data)
            con.commit()
            self.actualizar_treeview(treew)
            print("Datos cargados:", data)
            messagebox.showinfo(title="Contacto cargado",
                                message=f"El contacto fue cargado exitosamente")
        except:
            messagebox.showerror(title="ERROR",
                                 message="Se ha producido un error")

    @logs.log_baja
    def borrar(self, treew):
        if messagebox.askyesno("Borrar contacto", "¿Borrar contacto?"):
            valor = treew.selection()
            item = treew.item(valor)
            mi_id = item['text']
            con = conbd.conectar_base()
            cursor = con.cursor()
            mi_id = int(mi_id)
            data = (mi_id, )
            sql = "DELETE FROM contactos WHERE id = ?;"
            try:
                cursor.execute(sql, data)
                con.commit()
                treew.delete(valor)
                print("Id del contaco borrado:", mi_id)
                messagebox.showinfo(title="Contacto borrado",
                                    message=f"El contacto fue borrado exitosamente")
            except:
                messagebox.showerror(title="ERROR",
                                     message="Se ha producido un error")
        else:
            messagebox.showinfo(title="Contacto borrado",
                                message="El contacto no fue borrado")

    @logs.log_modificacion
    def modificar(self, nombre, apellido, numero, infoad, treew):
        if messagebox.askyesno("Editar contacto", "¿Editar contacto?"):
            valor = treew.selection()
            item = treew.item(valor)
            mi_id = item['text']
            con = conbd.conectar_base()
            cursor = con.cursor()
            mi_id = int(mi_id)
            data = (nombre, apellido, numero, infoad, mi_id)
            sql = "UPDATE contactos SET nombre=?, apellido=?, telefono=?, infoad=? WHERE ID=?;"
            try:
                cursor.execute(sql, data)
                con.commit()
                self.actualizar_treeview(treew)
                print("Id del contacto modificado:", mi_id)
                messagebox.showinfo("Editar contacto",
                                    "Contacto modificado exitosamente")
            except:
                messagebox.showerror(title="ERROR",
                                     message="Se ha producido un error")
        else:
            messagebox.showinfo("Editar contacto",
                                "Contacto no modificado")
