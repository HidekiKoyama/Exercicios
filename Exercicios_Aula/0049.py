'''
Crie um programa que tenha a função área(),
    que receba as dimensões de um muro retangular e mostra a área do terreno

'''

class Calculo():
    def area(self):
        try:
            print(self.n1 * self.n2)

        except ZeroDivisionError:
            print("Erro: Divisão por zero!")

        except:
            print("Erro não categorizado!")

    def requestData(self):
        try:
            #Recebe comprimento
            self.n1 = int(input("Digite o comprimento do terro: "))

            #Recebe largura
            self.n2 = int(input("Digite a lagura do terro: "))

        except ValueError:
            print("Apenas números!!")


if __name__ == "__main__":
    while True:
        i = Calculo()
        i.requestData()
        i.area()

        print("\n\n\n")
