'''
Escreva um programa que crie um dicionário com as informações de 5 livros, 
    como título, autor, ano de lançamento e número de páginas. 
    
    Em seguida, exiba apenas os autores dos livros.

'''

# base
livros = [
    {
        'titulo': '1984',
        'autor': 'George Orwell',
        'ano_lancamento': 1949,
        'num_paginas': 328
    },
    {
        'titulo': 'Cem Anos de Solidão',
        'autor': 'Gabriel García Márquez',
        'ano_lancamento': 1967,
        'num_paginas': 417
    },
    {
        'titulo': 'O Senhor dos Anéis: A Sociedade do Anel',
        'autor': 'J.R.R. Tolkien',
        'ano_lancamento': 1954,
        'num_paginas': 576
    },
    {
        'titulo': 'A Revolução dos Bichos',
        'autor': 'George Orwell',
        'ano_lancamento': 1945,
        'num_paginas': 144
    },
    {
        'titulo': 'Dom Quixote',
        'autor': 'Miguel de Cervantes',
        'ano_lancamento': {'parte_1': 1605, 'parte_2': 1615},
        'num_paginas': 'Varia dependendo da edição'
    }
    ]


class Consulta():
    def buscar(self, __nome : str) -> dict:
        self.__nome = __nome
        return livros[self.__nome]
    
if __name__ == "__main__":
    c = Consulta()
    for i in livros:
        print(i["autor"])
        