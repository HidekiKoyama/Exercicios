'''
Escreva um programa que execute o cálculo da Função horária da posição no MRUV,
e retorne de acordo com o tempo informado pelo usuário

Saída esperada:

A posição do objeto no tempo x é de y (m)
S=So+Vot+at2/2
'''

# Captura informacoes do calculo

posicao_inicial = float(input('Digite sua posicao inicial: '))
velocidade = float(input('Informe a velocidade : '))
aceleracao = float(input('Digite sua aceleracao inicial: '))
tempo = float(input('Informe o tempo: '))

posicao = posicao_inicial + velocidade * tempo + (aceleracao * tempo ** 2) / 2

print(f'a posicao do objeto no tempo {tempo} e sua posicao é: {posicao}')