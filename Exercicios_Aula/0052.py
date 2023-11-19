'''
Crie uma tupla com 5 nomes de países e exiba os países em ordem alfabética.
'''

class Calculo():

    def requestData(self, *n):
        try:
            order = sorted(n)
            print(order)
        except ValueError:
            print("Apenas números!!")


if __name__ == "__main__":
    i = Calculo()
    i.requestData('Inglaterra','Suiça', 'Paises baixos', 'Brasil', 'Egito', 'Alemanha')

