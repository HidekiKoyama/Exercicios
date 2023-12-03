"""
Crie um programa onde o usuário possa digitar sete letras, e cadastre em uma única lista, 
    que mantenha separado as consoantes das vogais
"""

lista = [[], []]
for i in range(0,7):
    w = input("Digite uma letra: ")
    lista[0].append(w) if w.lower() in 'aeiou' else lista[1].append(w)

print(lista)