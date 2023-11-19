"""
Crie um programa que leia vários números inteiros.

    O programa só vai parar quando o usuário digitar 0000.
        No final mostre
            quantos números foram digitados e qual
                a soma entre eles (desconsiderando o flag)
"""

nSys = 1000
nVall = []
nMais = True
cConta = 0

while nSys != 0000:
    num = int(input("Digite um número: "))
    nVall.append(num)

    if num != 0000:
        cConta += 1
    else:
        break
print(f"A soma dos números é {sum(nVall)}"
      f"\nA quantidade de números digitados foi {cConta}")
