'''
    Escreva um programa que verifique se uma frase é um palíndromo.


a = input("Escreva sua palavra para eu verificar se é um palíndromo: ")

if a == (a[::-1]):
    print(f"\nÉ um palíndromo, sua palavra foi {a} e ela ao contrário é {a[::-1]}")

else:
    print(f"\nNão é um palíndromo!! Sua palavra foi {a} e ela ao contrário é {a[::-1]}")

'''

a = input("Escreva sua palavra para eu verificar se é um palíndromo: ")
valida = 0

for i in range(0, len(a)):
    if a[i] == a[-i -1]:
        valida += 1

if valida == len(a):
    print("é palindromo")
else:
    print("Não é palindromo")