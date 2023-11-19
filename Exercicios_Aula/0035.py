'''
Escreva um programa que leia o
Nome, idade e sexo de 4 pessoas. No final mostre:

    A média de idade do grupo
    Qual é o homem mais velho
    Quantas mulheres têm menos de 20 anos

'''

class Pessoa():

    def nome(self):
        nome = input("Digite o nome: ")
        return nome

    def idade(self):
        idade = int(input("Digite a idade: "))
        return idade

    def sexo(self):
        sexo = input("Digite o sexo, sendo M para masculino e F para feminino: ").upper()
        return sexo


soma_idade = 0
qtd = 0
conta_F20 = 0
homem_mais_velho_n = ""
homem_mais_velho_i = 0

p = Pessoa()
for i in range(1, 5):
    nome = p.nome()
    idade = p.idade()
    sexo = p.sexo()

    soma_idade += idade
    qtd += 1

    if sexo == "F" and idade < 20:
        conta_F20 += 1

    if sexo == "M" and idade > homem_mais_velho_i:
        homem_mais_velho_n = nome
        homem_mais_velho_i = idade


print(f"A media do grupo é: {soma_idade/qtd}")
print(f"Qual é o homem mais velho é: {homem_mais_velho_n}")
print(f"A quantidade de mulheres que têm menos de 20 anos é: {conta_F20}")

