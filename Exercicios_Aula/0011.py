'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
    O nome com todas as letras maiúsculas
    O nome com todas minúsculas
    Quantas letras ao todo (sem considerar os espaços)
    Quantas letras tem o primeiro nome

'''


class TrataString():
    def Maiuscula(self, texto):
        return texto.upper()

    def Minuscula(self, texto):
        return texto.lower()

    def Contaletras(self, texto):
        return len(texto.replace(' ', ''))

    def ContaLetraPrimeiroNome(self, texto):
        return len(texto.split()[0])

texto = TrataString()

frase = input('Escreva uma frase qualquer: ').strip()

print(f"Sua frase em maiusculo: {texto.Maiuscula(frase)}")
print(f"Sua frase em minusculo: {texto.Minuscula(frase)}")
print(f"Sua frase contem {texto.Contaletras(frase)} caracteres")
print(f"A primera palavra de sua frase contem {texto.ContaLetraPrimeiroNome(frase)} caracter")


'''


class TrataString():
    def ContagemA(self, texto):
        quantidade = texto.count('a')
        return quantidade

    def Posicao(self, texto):
        posicao = texto.find('a')
        return posicao

    def ContaLetraPrimeiroNome(self, texto):
        nome = len(texto.split()[0])
        return nome

texto = TrataString()

frase = input('Escreva uma frase qualquer: ')

print(f'A primeira posicao do seu texto é: {texto.Posicao(frase)}')
print(f'')
'''