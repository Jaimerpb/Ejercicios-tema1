
class NumeroMagico():
    def __init__(self):
        self.numero_magico=12345679
    
    def multiplicar(self,numero_usuario):
        numero_usuario *= 9
        self.numero_magico *= numero_usuario
        return self.numero_magico
    

if __name__ == "__main__":
    num_magico=NumeroMagico()
    numero_usuario=int(input("Introduce un número que se entre 1 y 9: "))
    resultado = num_magico.multiplicar(numero_usuario)
    print(resultado)