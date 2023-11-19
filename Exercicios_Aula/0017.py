'''
Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.

'''

x = input("Digite qualquer letra: ").lower()

if x in ['a', 'e', 'i', 'o', 'u']:
    print("Você digitou uma vogal")

else:
    print("Você digitou uma consoante!")