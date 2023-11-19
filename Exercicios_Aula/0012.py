'''
Crie um programa que leia um nome, e mostre o primeiro e o último nome

Saída esperada:
    Luis Felipe Tatin Vlatkovic
    Primeiro nome: Luis
    Último nome: Vlatkovic
'''

class TrataString():
    def PegaPrimeiraPalavra(self, texto):
        return texto.split()[0]

    def PegaUltimaPalavra(self, texto):
        return texto.split()[-1]

nome = input('Digite seu nome: ').strip()

texto = TrataString()

print(f"Seu primeiro nome é: {texto.PegaPrimeiraPalavra(nome)}")
print(f"Seu primeiro nome é: {texto.PegaUltimaPalavra(nome)}")


