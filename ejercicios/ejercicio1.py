
class RegistroAlumno:
    
    def __init__(self, cadena_corrupta):
        self.cadena_corrupta = cadena_corrupta
    
    lista=[]
    @staticmethod
    def buscar_cadena_corrupta(cadena_corrupta):
        for cadena_corrupta in enumerate(RegistroAlumno.lista):
            if cadena_corrupta==cadena_corrupta:
                return cadena_corrupta
    
    @staticmethod 
    def agregar_cadena_corrupta(cadena_corrupta):
        RegistroAlumno.lista.append(cadena_corrupta)
        return cadena_corrupta
    
    @staticmethod 
    def proper_cadena(cadena_corrupta):
        properly=cadena_corrupta[::-1]
        registro=properly.split(",")
        nota=registro[0]
        nombreyapellido=registro[1]
        return f'La nota de {nombreyapellido} es un {nota}'
    
    @staticmethod
    def eliminar_cadena_corrupta(cadena_corrupta):
        for i,cadena_corrupta in enumerate (RegistroAlumno.lista):
            if cadena_corrupta==cadena_corrupta:
                del RegistroAlumno.lista[i]
                return cadena_corrupta
            

if __name__ == "__main__":
    nombre1=RegistroAlumno("zeréP nauJ,01")
    print(RegistroAlumno.proper_cadena(nombre1.cadena_corrupta))

