'''
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
Saída esperada:
A dobro de 9 é : 18
A triplo de 9 é : 27
A raiz quadrada de 9 é : 3
'''

x = int(input(f'Digite seu numero: '))
x2 = x * 2
x3 = x * 3
xr = x ** 0.5

print(f' O dobro de {x} é: {x2}' +
      f'\n O Triplo de {x} é: {x3}'+
      f'\n A raiz quadrada de {x} é: {xr}')