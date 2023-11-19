'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).

    Depois, deve mostrar para cada palavra, suas vogais

'''

class Letra():
    def __init__(self):
        self.tup = ('cachorro', 'papagaio','gurila', 'galinha', 'pavao','serpente')

    def vogais(self):
        for _ in self.tup:
            print(_)
            for i in _:
                if i in "aeiou":
                    print(i)


if __name__ == "__main__":
    l = Letra()
    l.vogais()