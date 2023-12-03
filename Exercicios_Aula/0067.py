'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 

    O programa vai perguntar quantos jogos serão gerados e 
    vai sortear 6 números entre 1 a 60 para cada jogo, 
    
    cadastrando tudo em uma lista composta
 
'''

import random as rm

lista_principal = []
jogos_qtd = int(input("Digite quantos jogos deseja criar: "))

for jogo in range(0, jogos_qtd):
    
    palpite = []
    
    while len(palpite) < 6:
        numero_aleatorio = rm.randint(1,60)
        
        if numero_aleatorio in palpite:
            pass
        else:
            palpite.append(numero_aleatorio)
            
    lista_principal.append(palpite)
    

for jogo in lista_principal:
    print(jogo)