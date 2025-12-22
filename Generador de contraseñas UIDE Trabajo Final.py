import string
import secrets
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox


# Función para generar la contraseña 
def generar_contraseña():
    longitud = entrada_longitud.get()

    # Validar que la longitud sea numérica
    if not longitud.isdigit():
        messagebox.showerror("Error", "Ingrese carácter válido")
        return

    longitud = int(longitud)

    if longitud <= 0:
        messagebox.showerror("Error", "La longitud debe ser mayor a 0")
        return

    caracter = ""

    if var_mayus.get():
        caracter += string.ascii_uppercase
    if var_minus.get():
        caracter += string.ascii_lowercase
    if var_numeros.get():
        caracter += string.digits
    if var_especiales.get():
        caracter += string.punctuation

    if caracter == "":
        messagebox.showerror("Error", "Seleccione al menos un tipo de carácter")
        return

    # Generar contraseña segura
    contraseña = "".join(secrets.choice(caracter) for _ in range(longitud))

    salida_contrasena.delete(0, END)
    salida_contrasena.insert(0, contraseña)


#  Ventana principal.
root = ttk.Window(themename="darkly")
root.title("Generador de Contraseña UIDE")
root.geometry("425x370")
root.resizable(False, False)

# Título de la ventana principal.
ttk.Label(
    root,
    text="Generador de Contraseñas UIDE",
    font=("Arial", 14, "bold")
).pack(pady=10)

#  Longitud (cuadro de texto donde se ingresara la longitud "tamaño" de la contraseña desea)
ttk.Label(root, text="Longitud de la contraseña:").pack()
entrada_longitud = ttk.Entry(root, width=10)
entrada_longitud.pack(pady=5)

#  Cuadros se seleccion para los caracteres a usar para la creacion de la contraseña. 
var_mayus = ttk.BooleanVar()
var_minus = ttk.BooleanVar()
var_numeros = ttk.BooleanVar()
var_especiales = ttk.BooleanVar()

ttk.Checkbutton(root, text="Mayúsculas", variable=var_mayus).pack(anchor="w", padx=60)
ttk.Checkbutton(root, text="Minúsculas", variable=var_minus).pack(anchor="w", padx=60)
ttk.Checkbutton(root, text="Números", variable=var_numeros).pack(anchor="w", padx=60)
ttk.Checkbutton(root, text="Caracteres especiales", variable=var_especiales).pack(anchor="w", padx=60)

#  Botón para generar la contraseña.
ttk.Button(
    root,
    text="Generar contraseña",
    bootstyle=SUCCESS,
    command=generar_contraseña
).pack(pady=15)

#  Salida (contraseña generada)
ttk.Label(root, text="Contraseña generada:").pack()
salida_contrasena = ttk.Entry(root, width=40, font=("Helvetica", 11))
salida_contrasena.pack(pady=5)

#  Ejecutar (iniciar)
root.mainloop()
