#Escreva um programa que leia 6 notas diferentes e faça a média do aluno

lista = []
x = 0
#Captura as notas dos alunos
while (x < 6):
    nota = int(input('Digite uma nota e pressione enter: \n'))
    lista.append((nota))
    x = x+1

#realiza o calculo de media dos alunos
media = sum(lista) / len(lista)

#Retorna a media dos alunos

print(f'A media dos alunos é: {media}')