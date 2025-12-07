import tkinter as tk
import random
import string
import ttkbootstrap as ttk 

# Generador de contraseña
def generadorcontraseña(longitud=16):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(caracteres) for _ in range(longitud))

# Función para generar contraseña desde la interfaz
def generador_de_contraseña():
    try:
        longitud = int(longitud_de_entrada.get())
        contraseña = generadorcontraseña(longitud)
        contraseña_generada.config(text=contraseña)
    except ValueError:
        contraseña_generada.config(text="Ingrese un número válido")

# Ventana principal
root = ttk.Window(themename='darkly')
root.title("Generador de Contraseña UIDE")
root.geometry("400x250")

# Etiqueta
longitud_de_ventana = ttk.Label(root, text="Longitud de la contraseña:")
longitud_de_ventana.pack(pady=10)

# Entrada de longitud
longitud_de_entrada = ttk.Entry(root)
longitud_de_entrada.pack()

# Botón
Boton_generar = ttk.Button(root, text="Generar contraseña", command=generador_de_contraseña)
Boton_generar.pack(pady=10)

# Etiqueta para mostrar contraseña
contraseña_generada = ttk.Label(root, text="", font=("Helvetica", 12), wraplength=380)
contraseña_generada.pack(pady=10)

# Ejecutar ventana
root.mainloop()
