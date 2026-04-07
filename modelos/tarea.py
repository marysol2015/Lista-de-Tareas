class Tarea:
    def __init__(self, descripcion):
        self._descripcion = descripcion  # Atributo protegido con guion bajo
        self._completada = False

    @property
    def descripcion(self):
        return self._descripcion

    @property
    def completada(self):
        return self._completada

    @completada.setter
    def completada(self, estado):
        if isinstance(estado, bool):
            self._completada = estado

    def __str__(self):
        estado = "[Completada]" if self._completada else "[Pendiente]"
        return f"{estado} {self._descripcion}"
    
    