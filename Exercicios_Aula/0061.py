"""
Escreva um programa que crie uma lista vazia e permita que o usuário 
    insira números nessa lista até que ele digite um número negativo. 
    Em seguida, exiba a lista na tela.
"""

class Numero():
    def __init__(self) -> None:
        self.ls = []
        
    def addInList(self, val):
        if val > -1:
            self.ls.append(val)
            return True
        else:
            return False

    def __del__(self):
        print(self.ls)
        print("Seu objeto numero foi destruido!")


if __name__ == "__main__":
    n = Numero()
    cont = True
    
    while cont:
        try:
            cont = n.addInList(int(input("Digite algum número: ")))
        except ValueError:
            print("Somente núemros, por favor!")
        
        except:
            print("Algum erro imprevisto ocorreu!")
            
    del n