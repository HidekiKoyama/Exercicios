'''
Crie um programa que leia vários números inteiros pelo teclado.

No final da execução,
    mostre a média entre todos os valores e
    qual foi o maior
    e o menor valores lidos.

O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
'''

escolha = 0

cNum = True

while escolha != "N":
    valores = []
    while cNum:
        valores.append(int(input("Digite um numero: ")))

        if "S" == str(input("Digite [S] se deseja continuar digitando números, ou [N] para sair: ")).upper():
            pass
        else:
            break

    print(f"\nA Soma dos valores digitados é {sum(valores)}"
          f"\nA Media dos valores digitados é {sum(valores)/len(valores)}"
          f"\nO Maior dos valores digitados é {max(valores)}"
          f"\nO Menor dos valores digitados é {min(valores)}")

    escolha = input("Deseja continuar? [S/N]")