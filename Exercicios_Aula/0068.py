'''
Escreva um programa que crie um dicionário com as informações de 5 países, como nome, capital, população e idioma oficial. 

Em seguida, permita que o usuário digite o nome de um país e exiba suas informações.

'''

# base
paises = {
    "Brasil":{
        "Capital": "Brasília",
        "População": 213000000,
        "Idioma Oficial": "Português"},

    "Japão":{
        "Capital": "Tóquio",
        "População": 126000000,
        "Idioma Oficial": "Japonês"},

    "Austrália":{
        "Capital": "Camberra",
        "População": 25000000,
        "Idioma Oficial": "Inglês"},

    "Egito":{
        "Capital": "Cairo",
        "População": 104000000,
        "Idioma Oficial": "Árabe"},

    "França":{
        "Capital": "Paris",
        "População": 67000000,
        "Idioma Oficial": "Francês"}
}


class Consulta():
    def buscar(self, __nome : str) -> dict:
        self.__nome = __nome
        return paises[self.__nome]
    
if __name__ == "__main__":
    c = Consulta()
    for i in paises:
        print(i)
    nome = input("Escreva o nome de um país: ")
    print(c.buscar(nome))
    