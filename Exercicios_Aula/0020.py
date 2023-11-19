'''
nova versão

Crie um programa que verifica se uma pessoa pode ser doadora de sangue, 
considerando a idade e os critérios de saúde.

'''

pergunta = True

while pergunta:
    pergunta = float(input("Digite seu peso: ")) > 50
    pergunta = int(input("Digite sua idade: ")) in range(17, 69)
    pergunta = int(input("Quantas horas você dormiu hoje: ")) > 6
    break

if pergunta:
    print("\nVocê pode doar snague")
else:
    print("\nVocê não pode doar sangue")