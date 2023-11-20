'''
Escreva um programa que crie duas listas com 5 números cada uma 
e exiba a soma dos elementos correspondentes das duas listas. 
    Por exemplo, se as listas forem [1, 2, 3, 4, 5] e [5, 4, 3, 2, 1], 
        o programa deve exibir [6, 6, 6, 6, 6].
'''

class Lista():
    def __init__(self) -> None:
        self.__a = [1,2,3,4,5]
        self.__b = [5,4,3,2,1]
        self.__ab = []

    def sumLs(self) -> None:
        for _ in self.__a:
            self.__ab.append(self.__a[_-1]+self.__b[_-1])
            
    def getLs(self) -> list:
        return self.__ab
        
    def __del__(self) -> None:
        print("Seu objeto Lista foi destruido!")

if __name__ == "__main__":
    l = Lista()
    l.sumLs()
    l.getLs()
    print(l.getLs())
    del l
