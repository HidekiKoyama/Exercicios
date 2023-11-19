'''
Escreva um programa que peça ao usuário um
    número e imprima se está
        entre 0 e 10,
        entre 10 e 20 ou
        maior que 20.

'''

x = int(input("Digite um numero qualquer: "))

if x in range(0, 10):
    print("Seu numero esta entre 0 a 10")

elif x in range(10, 20):
    print("Seu numero esta entre 10 a 20")

else:
    print("Seu numero é maior que 20")

