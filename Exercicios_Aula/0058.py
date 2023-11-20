'''
Crie um programa onde serão informados diversos valores em uma lista. 
    Caso o número já exista ele não será adicionado. 
    No final, serão exibidos todos os valores únicos em ordem crescente
'''


class Lista():
    def __init__(self) -> None:
        self.lista = []

    def addInList(self, val):
        if val not in self.lista:
            self.lista.append(val)

        else:
            print("Valor já registrado!")

    def showList(self):
        return sorted(self.lista)

    def __del__(self):
        print("Seu objeto Lista foi destruído!!")


if __name__ == "__main__":
    l = Lista()
    print("Digite quantos números desejar!\n" +
          "Para sair, digite sair, ou qualquer tecla e cofirme")

    loo = True
    while loo:
        try:
            l.addInList(int(input("Digite seu número: ")))
        except ValueError:
            print(l.showList())
            loo = False

    