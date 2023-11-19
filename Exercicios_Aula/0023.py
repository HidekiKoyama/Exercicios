'''
Escreva um programa que peça ao usuário uma palavra e imprima se começa com vogal ou consoante.
'''

vogais = ['a', 'e', 'i', 'o', 'u']

x = input("Digite uma palavra: ").lower()

if x[0] in vogais:
    print("A primeira letra é uma vogal")
else:
    print("Sua palavra começa uma consoante")