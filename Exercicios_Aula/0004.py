# Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.
import math

r = float(input('Digite o raio de sua esfera: '))
y = (4/3) * math.pi * (r**3)
x = 4 * math.pi * (r**2)

print(f'O volume de sua esfera e: {y:.2f}'+
      f' e a Area de sua esfera é:  {x:.2f}')