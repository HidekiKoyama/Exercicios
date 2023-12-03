'''
Faça um programa que leia o nome e o QI de várias pessoas, 
    guardando tudo e uma lista. No final mostre:

Quantas pessoas foram cadastradas
Uma listagem com as pessoas com o maior QI
Uma listagem com as pessoas de menor QI

'''

class Cadastro():
    def __init__(self) -> None:
        self.__lista_qi = [[], []]

    def incluirNome(self, nome) -> None:
        self.__nome = nome
        self.__lista_qi[0].append(self.__nome)
        
    def incluirQI(self, qi) -> None:
        self.__qi = qi
        self.__lista_qi[1].append(self.__qi)
    
    def pegarLista(self) -> list:
        return self.__lista_qi
    
    def totalPessoas(self):
        pessoas_cadastradas = len(self.__lista_qi[0])
        return pessoas_cadastradas
    
    def maiorQI(self) -> None:
        lista_ordenada = sorted(self.__lista_qi[1], reverse=True)
        
        for elemento in lista_ordenada:
            posicao = self.__lista_qi[1].index(elemento)
            print(self.__lista_qi[0][posicao])

    def menorQI(self) -> None:
        lista_ordenada = sorted(self.__lista_qi[1], reverse=False)
        
        for elemento in lista_ordenada:
            posicao = self.__lista_qi[1].index(elemento)
            print(self.__lista_qi[0][posicao])


if __name__ == "__main__":
    c = Cadastro()
    
    while True:
        nome = input("Digite um nome ou para sair digite (sair): ")
        if nome == "sair":
            break
        while True:
            try:
                qi = int(input(f"Digite o Qi do(a) {nome}: "))
                break
            except ValueError:
                print("Só aceitamos números!")
                
        c.incluirNome(nome)
        c.incluirQI(qi)
    
    print(f"O total de pessoas é: {c.totalPessoas()}")    
    print("\nA lista de pessoas com o maior QI: ")
    c.maiorQI()
    print("\nA lista de pessoas com o menor QI: ")
    c.menorQI()
