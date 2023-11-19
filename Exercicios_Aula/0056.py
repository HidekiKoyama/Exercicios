'''
Usando tuplas, leia um número de 0 a 15, e

    retorne esse número escrito por extenso


'''

class Extenso():
    def __init__(self):
        self.tup = ('zero', 'um', 'dois','três', 'quatro', 'cinco'
                    ,'seis', 'sete', 'oito', 'nove', 'dez',
                    'onze', 'doze','treze','quatrorze','quinze')

    def escolha(self, n):
        ex = self.tup[n]
        return ex

if __name__ == "__main__":
    e = Extenso()
    print(e.escolha(15))


