class tareas:
    def __init__(self, tarea, prioridad):
        self.tarea = tarea
        self.prioridad = prioridad

    def __str__(self):
        return f"{self.tarea}"

    @staticmethod
    def ordenar_tareas(lista_tareas):
        # lista_tareas.sort(key=lambda tarea: tarea.prioridad)
        lista_tareas.sort()
        for tarea in lista_tareas:
            print(tarea[1])
        return lista_tareas
