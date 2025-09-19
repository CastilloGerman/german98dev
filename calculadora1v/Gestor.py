import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

#conexion bd
conn = sqlite3.connect(r"C:\Users\German\Documents\Proyectos\GestorTareas\tareas.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS tareas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    estado TEXT DEFAULT 'Pendiente'
)
""")
conn.commit()

#Funciones
def agregar_tarea():
    titulo = entry_tarea.get()
    if titulo.strip() == "":
        messagebox.showwarning("Aviso", "La tarea no puede estar vacía.")
        return
    cursor.execute("INSERT INTO tareas (titulo) VALUES (?)", (titulo,))
    conn.commit()
    entry_tarea.delete(0, tk.END)
    mostrar_tareas()

def mostrar_tareas(filtro="Todas"):
    for row in tree.get_children():
        tree.delete(row)

    if filtro == "Pendientes":
        cursor.execute("SELECT id, titulo, estado FROM tareas WHERE estado='Pendiente'")
    elif filtro == "Completadas":
        cursor.execute("SELECT id, titulo, estado FROM tareas WHERE estado='Completada'")
    else:
        cursor.execute("SELECT id, titulo, estado FROM tareas")

    for tarea in cursor.fetchall():
        tree.insert("", "end", values=tarea)

def completar_tarea():
    seleccion = tree.selection()
    if not seleccion:
        messagebox.showwarning("Aviso", "Selecciona una tarea.")
        return
    item = tree.item(seleccion[0])
    id_tarea = item["values"][0]
    cursor.execute("UPDATE tareas SET estado='Completada' WHERE id=?", (id_tarea,))
    conn.commit()
    mostrar_tareas(combo_filtro.get())

def eliminar_tarea():
    seleccion = tree.selection()
    if not seleccion:
        messagebox.showwarning("Aviso", "Selecciona una tarea.")
        return
    item = tree.item(seleccion[0])
    id_tarea = item["values"][0]
    cursor.execute("DELETE FROM tareas WHERE id=?", (id_tarea,))
    conn.commit()
    mostrar_tareas(combo_filtro.get())

def limpiar_completadas():
    cursor.execute("DELETE FROM tareas WHERE estado='Completada'")
    conn.commit()
    mostrar_tareas(combo_filtro.get())

# ui
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("650x500")
root.resizable(False, False)

# Frame superior para entrada
frame_top = ttk.Frame(root, padding=10)
frame_top.pack(fill="x")

entry_tarea = ttk.Entry(frame_top, width=40)
entry_tarea.pack(side="left", padx=5)

btn_agregar = ttk.Button(frame_top, text="Agregar", command=agregar_tarea)
btn_agregar.pack(side="left")

# Frame del filtro
frame_filter = ttk.Frame(root, padding=10)
frame_filter.pack(fill="x")

ttk.Label(frame_filter, text="Filtrar:").pack(side="left")
combo_filtro = ttk.Combobox(frame_filter, values=["Todas", "Pendientes", "Completadas"], state="readonly")
combo_filtro.set("Todas")
combo_filtro.pack(side="left", padx=5)
combo_filtro.bind("<<ComboboxSelected>>", lambda e: mostrar_tareas(combo_filtro.get()))

# Tabla de tareas
columns = ("ID", "Título", "Estado")
tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")
tree.pack(padx=10, pady=10, fill="both")

# Botones de acciones
frame_buttons = ttk.Frame(root, padding=10)
frame_buttons.pack(fill="x")

btn_completar = ttk.Button(frame_buttons, text="Marcar completada", command=completar_tarea)
btn_completar.pack(side="left", padx=5)

btn_eliminar = ttk.Button(frame_buttons, text="Eliminar", command=eliminar_tarea)
btn_eliminar.pack(side="left", padx=5)

btn_limpiar = ttk.Button(frame_buttons, text="Limpiar completadas", command=limpiar_completadas)
btn_limpiar.pack(side="left", padx=5)

# Mostrar tareas al inicio
mostrar_tareas()

root.mainloop()

# Cerrar conexión al salir
conn.close()
