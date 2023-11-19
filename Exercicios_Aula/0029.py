'''
Escreva um programa que imprima a tabuada de um número fornecido pelo usuário.

'''

x = int(input("Digite qual tabuada deseja visualizar: "))

for i in range (1, 11):
    print(f"{i} x {x} = {i*x}")
