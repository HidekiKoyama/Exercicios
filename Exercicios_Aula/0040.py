"""

Escreva um programa que leia um
    número n inteiro qualquer e mostra na tela os n primeiros elementos de uma Sequência de Fibonacci

"""

n = int(input("Digite um numero de vezes que deseja vizualizar a Sequência de Fibonacci: "))
i = 0
sum, v1, v2 = 0, 0, 1

while i != n:
    if i == 1:
        print(f"Fibonacci Seq {i} - {sum}")
        sum = 1
        i += 1
    else:
        print(f"Fibonacci Seq {i} - {sum}")
        sum = v1 + v2
        v1 = v2
        v2 = sum
        i += 1