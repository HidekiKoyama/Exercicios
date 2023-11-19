'''
    Escreva um programa que imprima todos os números pares entre dois números fornecidos pelo usuário.
'''

num1 = int(input("Digite o primeiro numero de sua seuqencia: "))
num2 = int(input("Digite o ultimo numero de sua seuqencia: "))

for i in range(num1, num2):
    if i % 2 == 0:
        print(i)
