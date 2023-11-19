'''
Escreva um programa que peça ao
    usuário 5 notas, de 0 a 10 e imprima se a média, é
    insuficiente    (menor que 6),
    suficiente    (entre 6 e 7),
    bom (entre 7 e 9)
    ou excelente (9 ou maior).
'''

notas = []
x = 0
while x < 5:
    n = int(input("Digite a nota: "))
    notas.append(n)
    x = x + 1

media = sum(notas) / len(notas)

if media < 6:
    print("insuficiente")
elif media in range(6, 7):
    print("suficiente")
elif media in range(7, 9):
    print("bom")
elif media in range(9, 10):
    print("Excelente")
else:
    print("Notas digitadas invalidas")