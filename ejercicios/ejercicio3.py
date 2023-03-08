class Listas:
    def __init__(self,lista_1,lista_2):
        self.lista_1=lista_1
        self.lista_2=lista_2
    @staticmethod
    def third_list(self):
        no_repetidos=[]
        for elemento in self.lista_1:
            if elemento in self.lista_2 and elemento not in no_repetidos:
                no_repetidos.append(elemento)

        return no_repetidos


if __name__=="__main__":
    lista_1= ["h",'o','l','a',' ', 'm','u','n','d','o']
    lista_2=["h",'o','l','a',' ', 'l','u','n','a']
    lista=Listas(lista_1,lista_2)
    print(lista.third_list())



   