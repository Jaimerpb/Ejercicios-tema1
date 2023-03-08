class Separador:
    def __init__(self,lista):
        self.lista=lista
        self.pares=[]
        self.impares=[]

    def separar(self):
        for num in self.lista:
            if num%2==0:
                self.pares.append(num)
            else:
                self.impares.append(num)
        
        self.pares.sort()
        self.impares.sort()
        return self.pares.sort(),self.impares.sort()
    
if __name__=='__main__':
    lista=[1,2,3,4,5,6,7,8,9,10]
    separador=Separador(lista)
    print(separador.separar())