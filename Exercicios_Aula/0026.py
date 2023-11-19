'''
Crie um programa para analisar o IMC de uma pessoa,
    e classifique se ela está entre a faixa ideal,
        acima
        ou abaixo do IMC ideal.

'''

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

result = peso / (altura*altura)

if (result >= 18.5 and result <= 24.99):
    print(f"Esta com o peso ideal, seu imc é {result:.2f}")
elif result < 18.5:
    print(f"Esta com o peso abaixo do ideal, seu imc é {result:.2f}")
else:
    print(f"Esta com o peso acima ideal, seu imc é {result:.2f}")