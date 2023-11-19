'''

Faça um programa que leia um número e retorne o fatorial !

4! = 4 x 3 x 2 x 1

'''

x = int(input("Digite um número para descobrir seu fatorial: "))
calculo = 1

while x != 0:
    calculo *= x
    x -= 1

print(f"Seu fatorial é: {calculo}")