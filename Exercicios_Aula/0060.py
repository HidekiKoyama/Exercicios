'''
Escreva um programa que crie uma lista com os números de 1 a 10 
    e, em seguida, exiba apenas os números pares da lista.
'''

class Numero():
    def __init__(self) -> None:
        self.ls = []
        
    def addInList(self):
        for _ in range(1, 11):
            self.ls.append(_)
                
    def showPar(self):
        for _ in self.ls:
            if _ % 2 == 0:
                print(_)
                
    def __del__(self) -> None:
        print("Seu objeto foi destruido com sucesso!")
                
                
if __name__ == "__main__":
    n = Numero()
    n.addInList()
    print("Números Pares: ")
    n.showPar()
    del n