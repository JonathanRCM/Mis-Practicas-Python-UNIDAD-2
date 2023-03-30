import tkinter as tk
import sqlite3

# Crear la ventana principal
root = tk.Tk()
root.title("Veterinaria")

# Crear una etiqueta para el nombre de la mascota
lbl_nombre = tk.Label(root, text="Nombre de la mascota")
lbl_nombre.pack()

# Crear un campo de entrada para el nombre de la mascota
ent_nombre = tk.Entry(root)
ent_nombre.pack()

# Crear una etiqueta para el nombre del dueño
lbl_dueño = tk.Label(root, text="Nombre del dueño")
lbl_dueño.pack()

# Crear un campo de entrada para el nombre del dueño
ent_dueño = tk.Entry(root)
ent_dueño.pack()

# Crear una etiqueta para la especie de la mascota
lbl_especie = tk.Label(root, text="Especie de la mascota")
lbl_especie.pack()

# Crear un campo de entrada para la especie de la mascota
ent_especie = tk.Entry(root)
ent_especie.pack()

# Crear un botón para guardar los datos en la base de datos
def guardar_datos():
    # Conectar a la base de datos
    conn = sqlite3.connect('veterinaria.db')
    # Crear un cursor
    c = conn.cursor()
    # Insertar los datos en la base de datos
    c.execute("INSERT INTO mascotas (nombre, dueño, especie) VALUES (?, ?, ?)",
              (ent_nombre.get(), ent_dueño.get(), ent_especie.get()))
    # Guardar los cambios en la base de datos
    conn.commit()
    # Cerrar la conexión con la base de datos
    conn.close()

btn_guardar = tk.Button(root, text="Guardar datos", command=guardar_datos)
btn_guardar.pack()

# Crear un botón para ver la lista de mascotas registradas
def ver_mascotas():
    # Conectar a la base de datos
    conn = sqlite3.connect('veterinaria.db')
    # Crear un cursor
    c = conn.cursor()
    # Seleccionar todos los datos de la tabla mascotas
    c.execute("SELECT * FROM mascotas")
    # Recorrer los datos y mostrarlos en la consola
    for mascota in c.fetchall():
        print(mascota)
    # Cerrar la conexión con la base de datos
    conn.close()

btn_ver_mascotas = tk.Button(root, text="Ver mascotas", command=ver_mascotas)
btn_ver_mascotas.pack()

# Crear la tabla mascotas en la base de datos si no existe
conn = sqlite3.connect('veterinaria.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS mascotas
             (nombre TEXT, dueño TEXT, especie TEXT)''')
conn.commit()
conn.close()

# Iniciar el bucle principal de la ventana
root.mainloop()
