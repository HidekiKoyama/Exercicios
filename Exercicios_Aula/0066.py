'''
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 

No final mostre a matriz na tela, com a formatação correta
'''
listaPrincipal = []
for ele in range(0,3):
    lista = []
    for i in range(0,3):
        while True:
            try:
                num = int(input("Digite um numero: "))
                lista.append(num)
                break
            except ValueError:
                print("só aceitamos numeros!")
    listaPrincipal.append(lista)
    
for i in listaPrincipal:
    print(i)