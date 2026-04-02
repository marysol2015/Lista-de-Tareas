from modelos.tarea import Tarea

class TareaServicio:
    def __init__(self):
        self.tareas = []

    def añadir_tarea(self, descripcion):
        if descripcion.strip():
            nueva_tarea = Tarea(descripcion)
            self.tareas.append(nueva_tarea)
            return True
        return False

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completada = True
            return True
        return False

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
            return True
        return False

    def obtener_todas(self):
        return self.tareas
    
    