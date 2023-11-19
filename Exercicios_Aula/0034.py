'''
Escreva um programa que
    leia 10 números,
        se for ímpar deve ser descartado,
            se não, deve ser agregado a uma
                soma
'''

soma_par = 0

for i in range(1, 11):
    n = int(input("Digite um numero: "))
    if n % 2 == 0:
        soma_par += n
        print(f"Ocorrencia: {i}")

print(soma_par)