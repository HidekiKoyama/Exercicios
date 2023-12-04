'''
Escreva um programa que crie um dicionário com os nomes e preços de 5 produtos. 

Em seguida, exiba o produto mais barato e o mais caro.

'''

class Buscador():
    def __init__(self) -> None:
        self.__produtos = {
            'Sabonete': 2.5,
            'Pasta de Dente': 3.0,
            'Shampoo': 8.75,
            'Condicionador': 7.0,
            'Desodorante': 5.25,
            'Açaí': 8.75
            }

    def comparar(self, dado : float, cond : str) -> None:
        self.__dado = dado
        for prod, valor in self.__produtos.items():
            if self.__dado == valor:
                print("O produto mais {} é {}".format(cond,prod))
                
    def getProdutos(self):
        return self.__produtos

class Comparar(Buscador):
    def __init__(self) -> None:
        super().__init__()
        
    def maior(self) -> None:
        super().comparar(max(super().getProdutos().values()), "caro")

    def menor(self) -> None:
        super().comparar(min(super().getProdutos().values()), "barato")
        
if __name__ == "__main__":
    c = Comparar()
    c.maior()
    c.menor()