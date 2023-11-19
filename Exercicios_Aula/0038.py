'''
Crie uma calculadora que após ler 3 valores, mostre e opere de acordo com as opções:

1.	Somar
2.	Multiplicar
3.	Maior
4.	Novos números
5.	Sair do programa
'''

escolha = 0
valores = []
for i in range(0, 3):
    valores.append(int(input("Digite um numero: ")))

while escolha != 5:

    print(valores)
    escolha = int(input("O que deseja realizar?"
                    "\n 1.	Somar"
                    "\n 2.	Multiplicar"
                    "\n 3.	Maior"
                    "\n 4.	Novos números"
                    "\n 5.	Sair do programa\n"))

    if escolha == 1:
        print(f"Sua soma é {sum(valores)}")

    elif escolha == 2:
        mult = 1
        for i in valores:
            mult = mult * i

        print (f"Sua multiplicacao é {mult}")

    elif escolha == 3:

        print(f"O maior número é {max(valores)}")

    elif escolha == 4:
        valores.clear()
        for i in range(0, 3):
            valores.append(int(input("Digite um numero: ")))
    else:
        break