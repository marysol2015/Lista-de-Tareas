import tkinter as tk
from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppTodo

if __name__ == "__main__":
    # Inicializar servicios
    servicio = TareaServicio()
    
    # Configurar ventana principal
    root = tk.Tk()
    
    # Inyectar servicio en la UI
    app = AppTodo(root, servicio)
    
    # Iniciar aplicación
    root.mainloop()
    