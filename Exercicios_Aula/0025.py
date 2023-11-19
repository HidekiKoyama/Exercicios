'''
Crie um programa para jogar JOKEMPO, usando a função random.randint

'''
import random
class Aleatorio():
    def GeraNum(self):
        return int(random.randint(0, 2))

class Jokempo():
    def Start(self):
        player = int(input("Escolha entre pedra papel e tesoura sendo:"
                            "\n 0 = pedra \n 1 = papel \n 2 = tesoura\n"))
        return player


if __name__ == "__main__":
    while True:
        p = Jokempo()
        a = Aleatorio()

        jogadaA = a.GeraNum()
        jogadaP = 3

        while jogadaP not in range(0,2):
            try:
                jogadaP = p.Start()
            except:
                print('Por favor!!'
                      '\nDigite um número válido!')

        if jogadaA == jogadaP:
            print("Empate!")

        elif jogadaP == 0 and jogadaA == 2:
            print("Você ganhou!")

        elif jogadaP == 1 and jogadaA == 0:
            print("Você ganhou!")

        elif jogadaP == 2 and jogadaA == 1:
            print("Você ganhou!")

        else:
            print('Você perdeu!')


        input("_________________________________________________________________\n"
              "Dê enter para continuar jogando...\n"
              "_________________________________________________________________\n")
