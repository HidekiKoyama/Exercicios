'''
Faça um programa com uma função maior e menor, 
    que leia uma lista com 5 valores informados pelo usuário 
    e retorne esses valores e a posição deles
'''

class Lista():
    def __init__(self) -> None:
        self.lista = []
        
    def insere(self, valor):
        self.lista.append(valor)
        
    def maior(self):
        maximo = max(self.lista)
        posicao = self.lista.index(maximo)
        return (maximo, posicao)
    
    def menor(self):
        minimo = min(self.lista)
        posicao = self.lista.index(minimo)
        return (minimo, posicao)
    
    def __del__(self):
        print("Seu objeto foi destruido!!")
        
if __name__ == "__main__":
    l = Lista()
    for _ in range(5):
        l.insere(int(input("Digite um valor: ")))
    print(l.maior())
    print(l.menor())
    del l