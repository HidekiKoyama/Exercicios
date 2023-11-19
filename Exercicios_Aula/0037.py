'''

Escreva um programa que peça ao usuário para
adivinhar um número entre
    1 e 10 e continue pedindo até que o usuário acerte o número.

E no final, retorne também a quantidade de tentativas necessárias.
'''

import random as rm
aleatorio = rm.randint(1,10)
nUsuario = 0
contador = 0

while aleatorio != nUsuario:
    aleatorio = rm.randint(1,10)
    nUsuario = int(input("\nTente adivinhar o número que eu pensei: "
                          "\n Entre 1 e 10: "))
    contador += 1
    if aleatorio != nUsuario:
            print(f"\nNão foi desse vez."
                  f"\nEu escolhi {aleatorio} e você {nUsuario}")

print("\n\n*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/"
      "\nParabens você acertou!!"
      f"\nEu escolhi {aleatorio} e você {nUsuario}"
      f" e precisou de {contador} tentativas")