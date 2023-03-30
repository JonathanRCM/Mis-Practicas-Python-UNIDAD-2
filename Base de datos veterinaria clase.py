import tkinter as tk
import sqlite3

# BASE DE DATOS DE UNA VETERINARIA DONDE TE PIDE EL NOMBRE DE LA MASCOTA, EL DUEÑO Y LA RAZA Y TE LO GUARDA DENTRO DEL BUCLE

# Crear la ventana principal
root = tk.Tk()
root.title("Veterinaria")

# Creamos una etiqueta para el nombre de la mascota
# Asi con cada uno de los datos que puse, en ese caso son 3
lbl_nombre = tk.Label(root, text="Nombre de la mascota")
lbl_nombre.pack()

ent_nombre = tk.Entry(root)
ent_nombre.pack()

# Crear una etiqueta para el nombre del dueño
lbl_dueño = tk.Label(root, text="Nombre del dueño")
lbl_dueño.pack()

ent_dueño = tk.Entry(root)
ent_dueño.pack()

# Crear una etiqueta para la especie de la mascota
lbl_especie = tk.Label(root, text="Especie de la mascota")
lbl_especie.pack()


ent_especie = tk.Entry(root)
ent_especie.pack()

# Crear un botón para guardar los datos en la base de datos
def guardar_datos():
    
    conn = sqlite3.connect('veterinaria.db')
    c = conn.cursor()
    c.execute("INSERT INTO mascotas (nombre, dueño, especie) VALUES (?, ?, ?)",
              (ent_nombre.get(), ent_dueño.get(), ent_especie.get()))
    
    conn.commit()
    conn.close()

btn_guardar = tk.Button(root, text="Guardar datos", command=guardar_datos)
btn_guardar.pack()

# Boton para ver las mascotas ingresadas
def ver_mascotas():
    
    conn = sqlite3.connect('veterinaria.db')
    c = conn.cursor()
    c.execute("SELECT * FROM mascotas")
    
    for mascota in c.fetchall():
        print(mascota)
    
    conn.close()

btn_ver_mascotas = tk.Button(root, text="Ver mascotas", command=ver_mascotas)
btn_ver_mascotas.pack()

conn = sqlite3.connect('veterinaria.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS mascotas
             (nombre TEXT, dueño TEXT, especie TEXT)''')
conn.commit()
conn.close()
root.mainloop()
