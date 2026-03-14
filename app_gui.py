import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# -------- FUNCIONES --------

def agregar_dato(event=None):
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()

    if nombre == "" or edad == "":
        messagebox.showwarning("Advertencia", "Debe completar todos los campos")
        return

    tabla.insert("", "end", values=(nombre, edad))

    entrada_nombre.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)
    entrada_nombre.focus()


def limpiar_tabla():
    confirmacion = messagebox.askyesno("Confirmar", "¿Está seguro de borrar todos los datos?")

    if confirmacion:
        for item in tabla.get_children():
            tabla.delete(item)


# -------- VENTANA PRINCIPAL --------

ventana = tk.Tk()
ventana.title("Registro de Datos")
ventana.geometry("500x400")
ventana.resizable(False, False)

# -------- TITULO --------

titulo = tk.Label(ventana, text="Aplicación de Registro de Datos", font=("Arial", 16))
titulo.pack(pady=10)

# -------- FRAME DE ENTRADA --------

frame_entrada = tk.Frame(ventana)
frame_entrada.pack(pady=10)

# Nombre
label_nombre = tk.Label(frame_entrada, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=5, pady=5)

entrada_nombre = tk.Entry(frame_entrada)
entrada_nombre.grid(row=0, column=1, padx=5, pady=5)

# Edad
label_edad = tk.Label(frame_entrada, text="Edad:")
label_edad.grid(row=1, column=0, padx=5, pady=5)

entrada_edad = tk.Entry(frame_entrada)
entrada_edad.grid(row=1, column=1, padx=5, pady=5)

# -------- BOTONES --------

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

boton_agregar = tk.Button(frame_botones, text="Agregar", command=agregar_dato)
boton_agregar.grid(row=0, column=0, padx=10)

boton_limpiar = tk.Button(frame_botones, text="Limpiar", command=limpiar_tabla)
boton_limpiar.grid(row=0, column=1, padx=10)

# -------- TABLA --------

frame_tabla = tk.Frame(ventana)
frame_tabla.pack(pady=10)

tabla = ttk.Treeview(frame_tabla, columns=("Nombre", "Edad"), show="headings")

tabla.heading("Nombre", text="Nombre")
tabla.heading("Edad", text="Edad")

tabla.column("Nombre", width=200)
tabla.column("Edad", width=100)

tabla.pack()

# -------- MEJORA: ENTER PARA AGREGAR --------

entrada_nombre.bind("<Return>", agregar_dato)
entrada_edad.bind("<Return>", agregar_dato)

# -------- EJECUTAR --------

ventana.mainloop()
