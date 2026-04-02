import tkinter as tk
from tkinter import messagebox, font

class AppTodo:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio
        self.root.title("Task Master v2.0")
        self.root.geometry("450x600")
        self.root.configure(bg="#f0f2f5")  # Fondo gris claro moderno

        # Definición de Estilos y Colores
        self.color_primario = "#4a90e2"    # Azul vibrante
        self.color_fondo = "#f0f2f5"
        self.color_texto = "#333333"
        self.color_completado = "#888888"
        self.fuente_titulo = font.Font(family="Segoe UI", size=16, weight="bold")
        self.fuente_normal = font.Font(family="Segoe UI", size=10)

        # --- Contenedor Principal ---
        self.main_frame = tk.Frame(root, bg=self.color_fondo, padx=20, pady=20)
        self.main_frame.pack(expand=True, fill="both")

        # Título
        self.lbl_titulo = tk.Label(
            self.main_frame, text="Mis Pendientes", 
            font=self.fuente_titulo, bg=self.color_fondo, fg=self.color_primario
        )
        self.lbl_titulo.pack(pady=(0, 20))

        # --- Área de Entrada ---
        self.entry_frame = tk.Frame(self.main_frame, bg=self.color_fondo)
        self.entry_frame.pack(fill="x", pady=5)

        self.entrada_tarea = tk.Entry(
            self.entry_frame, font=self.fuente_normal, 
            relief="flat", highlightthickness=1, highlightbackground="#cccccc"
        )
        self.entrada_tarea.pack(side=tk.LEFT, fill="x", expand=True, ipady=5, padx=(0, 10))
        self.entrada_tarea.focus_set()

        self.btn_añadir = tk.Button(
            self.entry_frame, text="+", font=("Arial", 12, "bold"),
            bg=self.color_primario, fg="white", relief="flat",
            width=4, command=self.añadir, cursor="hand2"
        )
        self.btn_añadir.pack(side=tk.RIGHT)

        # --- Lista de Tareas ---
        self.lista_box = tk.Listbox(
            self.main_frame, font=self.fuente_normal,
            relief="flat", borderwidth=0, highlightthickness=0,
            selectbackground=self.color_primario, selectforeground="white",
            activestyle="none"
        )
        self.lista_box.pack(fill="both", expand=True, pady=20)

        # --- Panel de Acciones ---
        self.action_frame = tk.Frame(self.main_frame, bg=self.color_fondo)
        self.action_frame.pack(fill="x")

        self.btn_completar = tk.Button(
            self.action_frame, text="✓ Completar (C)", 
            bg="#2ecc71", fg="white", relief="flat", font=self.fuente_normal,
            padx=10, pady=5, command=self.completar, cursor="hand2"
        )
        self.btn_completar.pack(side=tk.LEFT, expand=True, fill="x", padx=5)

        self.btn_eliminar = tk.Button(
            self.action_frame, text="✕ Eliminar (Del)", 
            bg="#e74c3c", fg="white", relief="flat", font=self.fuente_normal,
            padx=10, pady=5, command=self.eliminar, cursor="hand2"
        )
        self.btn_eliminar.pack(side=tk.LEFT, expand=True, fill="x", padx=5)

        # --- Atajos de Teclado ---
        self.bind_events()

    def bind_events(self):
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
            messagebox.showwarning("Aviso", "Escribe algo primero.")

    def completar(self):
        seleccion = self.lista_box.curselection()
        if seleccion:
            self.servicio.marcar_completada(seleccion[0])
            self.actualizar_lista()

    def eliminar(self):
        seleccion = self.lista_box.curselection()
        if seleccion:
            self.servicio.eliminar_tarea(seleccion[0])
            self.actualizar_lista()

    def actualizar_lista(self):
        self.lista_box.delete(0, tk.END)
        for tarea in self.servicio.obtener_todas():
            check = " ● " if not tarea.completada else " ✓ "
            self.lista_box.insert(tk.END, f"{check} {tarea.descripcion}")
            
            # Estilo para tareas completadas
            if tarea.completada:
                index = self.lista_box.size() - 1
                self.lista_box.itemconfig(index, {'fg': self.color_completado})
                