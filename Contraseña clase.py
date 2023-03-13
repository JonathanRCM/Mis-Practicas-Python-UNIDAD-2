import tkinter as tk

def iniciar_sesion():
    usuario = nombre_usuario.get()
    contrasena = contrasena_usuario.get()
    if usuario == "Jonathan Cruz" and contrasena == "04002218":
        resultado.config(text="Inicio de sesión exitoso")
    else:
        resultado.config(text="Los siguietes datos son incorrectos")

ventana = tk.Tk()
ventana.title("Inicio de sesión")
ventana.configure(padx=200)

# Crear campos de entrada para el nombre de usuario y la contraseña
nombre_usuario = tk.Entry(ventana)
nombre_usuario.pack(pady=20)
contrasena_usuario = tk.Entry(ventana, show="*")
contrasena_usuario.pack()

# Crear botones para iniciar sesión y salir
iniciar_sesion = tk.Button(ventana, text="Iniciar sesión", command=iniciar_sesion)
iniciar_sesion.pack(padx=20, pady=20)
salir = tk.Button(ventana, text="Salir", command=ventana.quit)
salir.pack()

# Crear un widget de etiqueta para mostrar el resultado del inicio de sesión
resultado = tk.Label(ventana, text="")
resultado.pack(pady=20)

ventana.mainloop()