import tkinter as tk
# Importaciones desde los paquetes del sistema
from servicios.tarea_servicio import TareaServicio
from ui.app_tkinter import AppTodo

def main():
    # 1. Inicializar la lógica de negocio (Servicios)
    # Esto mantiene la separación de responsabilidades
    servicio = TareaServicio() 
    
    # 2. Configurar la raíz de la interfaz gráfica
    root = tk.Tk() 
    
    # 3. Inyectar el servicio en la UI
    # La clase AppTodo ya contiene los eventos .bind() necesarios
    app = AppTodo(root, servicio) 
    
    # 4. Iniciar el ciclo principal de la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()
    
