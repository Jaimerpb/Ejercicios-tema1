class Descomposicion:
    def __init__(self,num):
        self.num=num 

    @staticmethod
    def descomponer(self):
        num_str=str(self.num)
        longitud=len(num_str)
        resultado=[]
        for i,digito in enumerate(num_str)
            unidades=int(digito)*10**(longitud-i-1)
            resultado.append(unidades)

        return resultado
    
if __name__=='__main__':
    import sys 
    if len(sys.argv)!=2:
        print("Uso: python descomposicion.py <numero>")
    else:
        try:
            numero=int(sys.argv[1])
            descomposicion = Descomposicion(numero)
            descompuesto = descomposicion.descomponer()
            for n in descompuesto:
                print(f"{n:04d}")
        except ValueError:
            print("Error: el argumento debe ser un número entero positivo.")
            