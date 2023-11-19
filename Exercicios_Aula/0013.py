'''
Crie um programa que leia uma frase e mostre:
    Quantas vezes aparece a letra “a”
    Em que posição ela aparece a primeira vez
    Em que posição ela aparece na última vez

'''


class TrataString():
    def ContagemA(self, texto):
        return texto.lower().count('a')

    def PosicaoPrimeraOcorrencia(self, texto):
        return texto.lower().find('a')

    def PosicaoUlimaOcorrencia(self, texto):
        return texto.lower().rfind('a')

texto = TrataString()

frase = input('Escreva uma frase qualquer: ').strip()

print(f'A quantidade de vezes que o a letra "A" aparece são : {texto.ContagemA(frase)}')
print(f'A primeira vez que a letra "A" aparece é: {texto.PosicaoPrimeraOcorrencia(frase)}')
print(f'A ultima vez que a letra "A" aparece é: {texto.PosicaoUlimaOcorrencia(frase)}')
