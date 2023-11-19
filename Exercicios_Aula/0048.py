'''
Crie um programa que pede ao usuário para digitar dois números e, em seguida,
    divide o primeiro número pelo segundo número.
    No entanto, o programa deve ser capaz de lidar com a possibilidade de o usuário digitar um valor inválido, como uma string ou o número zero.

ZeroDivisionError ; ValueError
'''

class Calculo():
    def calculo(self):
        try:
            print(self.n1 / self.n2)

        except ZeroDivisionError:
            print("Erro: Divisão por zero!")

        except:
            print("Erro não categorizado!")

    def requestData(self):
        try:
            #Recebe numerador
            self.n1 = int(input("Digite um número: "))

            #Recebe denominador
            self.n2 = int(input("Digite mais um número: "))

        except ValueError:
            print("Apenas números!!")


if __name__ == "__main__":
    while True:
        i = Calculo()
        i.requestData()
        i.calculo()

        print("\n\n\n")
