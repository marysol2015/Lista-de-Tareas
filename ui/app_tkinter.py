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

        # Botones principales
        self.btn_añadir = tk.Button(root, text="Añadir (Enter)", command=self.añadir)
        self.btn_añadir.pack(pady=5)

        self.lista_box = tk.Listbox(root, width=50, height=15)
        self.lista_box.pack(pady=10, padx=10)

        # Botones de acción inferior
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=5)

        self.btn_completar = tk.Button(self.frame_botones, text="Completar (C)", command=self.completar)
        self.btn_completar.pack(side=tk.LEFT, padx=20)

        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar (Del)", command=self.eliminar)
        self.btn_eliminar.pack(side=tk.LEFT, padx=20)

        # --- Manejo de Eventos Avanzados (.bind) ---
        # El Enter siempre añade la tarea
        self.root.bind('<Return>', lambda e: self.añadir())
        self.root.bind('<Escape>', lambda e: self.root.destroy())

        # Atajos condicionales para evitar errores al escribir
        self.root.bind('c', self._atajo_completar)
        self.root.bind('C', self._atajo_completar)
        self.root.bind('d', self._atajo_eliminar)
        self.root.bind('<Delete>', self._atajo_eliminar)

    def _atajo_completar(self, event):
        # Solo ejecuta si el usuario no está escribiendo en la entrada
        if self.root.focus_get() != self.entrada_tarea:
            self.completar()

    def _atajo_eliminar(self, event):
        # Solo ejecuta si el usuario no está escribiendo en la entrada
        if self.root.focus_get() != self.entrada_tarea:
            self.eliminar()

    def añadir(self):
        texto = self.entrada_tarea.get()
        if self.servicio.añadir_tarea(texto):
            self.entrada_tarea.delete(0, tk.END)
            self.actualizar_lista()
            self.entrada_tarea.focus_set() # Mantiene el Workflow continuo
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
        """Ciclo de Actualización Sincronizada: Limpia y Refresca"""
        self.lista_box.delete(0, tk.END)
        for tarea in self.servicio.obtener_todas():
            # El modelo Tarea gestiona su propia representación visual
            item = str(tarea) 
            self.lista_box.insert(tk.END, item)
            
            # Feedback Visual: Estilo 'Hecho'
            if tarea.completada:
                self.lista_box.itemconfig(tk.END, {'fg': 'gray'})
                