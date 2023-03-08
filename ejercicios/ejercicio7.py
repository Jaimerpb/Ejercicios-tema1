class Agregar:
    def __init__(self,lista,el):
        self.lista=lista
        self.el=el
    @staticmethod 
    def agregar(self):
        if self.el in self.lista:
            raise ValueError("Error: Imposible añadir elementos duplicados => [elemento].")
        else:
            self.lista.append(self.el)
        return self.lista
if __name__=="__main__":
    elementos=[1,5,-2]
    agregador=Agregar(elementos,10)
    try:
        agregador.agregar()
        agregador=Agregar(elementos,-2)
        agregador = Agregar(elementos, "Hola")
        agregador.agregar()
    except ValueError as error:
        print(error)
    print(elementos)
