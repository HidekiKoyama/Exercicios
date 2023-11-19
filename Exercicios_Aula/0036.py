'''
Escreva um programa que leia o
    peso de
        7 pessoas, e no final, mostre qual foi o
            maior e o menor peso lidos

'''

maior_peso = 0
menor_peso = 0
for i in range(1, 8):
    peso = int(input(f"Digite o peso da pessoa {i}: "))

    if peso > maior_peso:
        maior_peso = peso

    if peso < menor_peso or menor_peso == 0:
        menor_peso = peso


print(f"O menor peso dentre as 7 pesoas é: {menor_peso}")
print(f"O maior peso dentre as 7 pesoas é: {maior_peso}")