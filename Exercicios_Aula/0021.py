'''
Escreva um programa que peça ao usuário um
    número de 1 a 7 e imprima o dia da semana correspondente
    (1 é segunda-feira, 2 é terça-feira, etc.).
'''

x = int(input("Digite o numero do dia da semana correspondente: "))

nome = ['Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Domingo']

print(f"O dia da semna digitado é: {nome[x-1]}")