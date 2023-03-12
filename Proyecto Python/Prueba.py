import tkinter as tk
from tkinter import messagebox

# Definir la función para mostrar el menú


# Definir la función para agregar un elemento
def agregar_elemento():
    elemento = entrada.get()
    if elemento:
        lista.insert(tk.END, elemento)
        messagebox.showinfo("Agregar elemento", "El elemento ha sido agregado exitosamente.")
    else:
        messagebox.showerror("Agregar elemento", "Debe ingresar un elemento.")

# Definir la función para mostrar todos los elementos
def mostrar_elementos():
    elementos = lista.get(0, tk.END)
    if elementos:
        messagebox.showinfo("Mostrar elementos", "\n".join(elementos))
    else:
        messagebox.showwarning("Mostrar elementos", "No hay elementos en la lista.")

# Definir la función para buscar un elemento
def buscar_elemento():
    elemento = entrada.get()
    if elemento:
        elementos = lista.get(0, tk.END)
        if elemento in elementos:
            messagebox.showinfo("Buscar elemento", "El elemento se encuentra en la lista.")
        else:
            messagebox.showwarning("Buscar elemento", "El elemento no se encuentra en la lista.")
    else:
        messagebox.showerror("Buscar elemento", "Debe ingresar un elemento.")

# Definir la función para actualizar un elemento
def actualizar_elemento():
    elemento_viejo = entrada.get()
    if elemento_viejo:
        elementos = lista.get(0, tk.END)
        if elemento_viejo in elementos:
            indice = elementos.index(elemento_viejo)
            elemento_nuevo = entrada_nueva.get()
            lista.delete(indice)
            lista.insert(indice, elemento_nuevo)
            entrada_nueva.delete(0, tk.END)
            messagebox.showinfo("Actualizar elemento", "El elemento ha sido actualizado exitosamente.")
        else:
            messagebox.showwarning("Actualizar elemento", "El elemento no se encuentra en la lista.")
    else:
        messagebox.showerror("Actualizar elemento", "Debe ingresar un elemento.")

# Definir la función para eliminar un elemento
def eliminar_elemento():
    elemento = entrada.get()
    if elemento:
        elementos = lista.get(0, tk.END)
        if elemento in elementos:
            indice = elementos.index(elemento)
            lista.delete(indice)
            messagebox.showinfo("Eliminar elemento", "El elemento ha sido eliminado exitosamente.")
        else:
            messagebox.showwarning("Eliminar elemento", "El elemento no se encuentra en la lista.")
    else:
        messagebox.showerror("Eliminar elemento", "Debe ingresar un elemento.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("CRUD en Python y Tkinter")

# Crear los widgets de la ventana
etiqueta = tk.Label(ventana, text="Ingrese un elemento:")
etiqueta.pack(pady=10)

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)
boton_agregar.pack(pady=5)

boton_mostrar = tk.Button(ventana, text="Mostrar", command=mostrar_elementos)
boton_mostrar.pack(pady=5)

etiqueta_nueva = tk.Label(ventana, text="Ingrese el nuevo elemento:")
etiqueta_nueva.pack(pady=10)

entrada_nueva = tk.Entry(ventana)
entrada_nueva.pack(pady=5)

boton_actualizar = tk.Button(ventana, text="Actualizar", command=actualizar_elemento)
boton_actualizar.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar_elemento)
boton_eliminar.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=5)

# Crear la lista para almacenar los elementos
lista = tk.Listbox(ventana)
lista.pack(padx=10, pady=10)

# Mostrar el menú


# Iniciar el bucle principal de la ventana
ventana.mainloop()