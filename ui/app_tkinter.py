import tkinter as tk
from tkinter import messagebox

class AppTodo:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio
        self.root.title("Gestor de Tareas Pro")
        self.root.geometry("400x450")

        # --- Componentes UI ---
        self.label = tk.Label(root, text="Nueva Tarea:", font=("Arial", 10, "bold"))
        self.label.pack(pady=5)

        self.entrada_tarea = tk.Entry(root, width=40)
        self.entrada_tarea.pack(pady=5)
        self.entrada_tarea.focus_set()

        # Botones
        self.btn_añadir = tk.Button(root, text="Añadir (Enter)", command=self.añadir)
        self.btn_añadir.pack(pady=5)

        self.lista_box = tk.Listbox(root, width=50, height=15)
        self.lista_box.pack(pady=10, padx=10)

        self.btn_completar = tk.Button(root, text="Completar (C)", command=self.completar)
        self.btn_completar.pack(side=tk.LEFT, padx=30)

        self.btn_eliminar = tk.Button(root, text="Eliminar (Del)", command=self.eliminar)
        self.btn_eliminar.pack(side=tk.RIGHT, padx=30)

        # --- Atajos de Teclado (Event Binding) ---
        self.root.bind('<Return>', lambda e: self.añadir())
        self.root.bind('<Delete>', lambda e: self.eliminar())
        self.root.bind('d', lambda e: self.eliminar())
        self.root.bind('c', lambda e: self.completar())
        self.root.bind('C', lambda e: self.completar())
        self.root.bind('<Escape>', lambda e: self.root.destroy())

    def añadir(self):
        texto = self.entrada_tarea.get()
        if self.servicio.añadir_tarea(texto):
            self.entrada_tarea.delete(0, tk.END)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Aviso", "La tarea no puede estar vacía.")

    def completar(self):
        seleccion = self.lista_box.curselection()
        if seleccion:
            self.servicio.marcar_completada(seleccion[0])
            self.actualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Selecciona una tarea para completar.")

    def eliminar(self):
        seleccion = self.lista_box.curselection()
        if seleccion:
            self.servicio.eliminar_tarea(seleccion[0])
            self.actualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Selecciona una tarea para eliminar.")

    def actualizar_lista(self):
        self.lista_box.delete(0, tk.END)
        for tarea in self.servicio.obtener_todas():
            item = str(tarea)
            self.lista_box.insert(tk.END, item)
            # Feedback visual: Color gris para completadas
            if tarea.completada:
                self.lista_box.itemconfig(tk.END, {'fg': 'gray'})