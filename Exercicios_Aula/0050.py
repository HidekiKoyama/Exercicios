'''
Escreva um programa que leia uma frase, e mostre uma formatação adaptável de acordo com o
    tamanho da frase, coordenado por uma função


Exemplo:
       ----------------------------
            Senai Show de bola
       ----------------------------
'''

class Frase():
    def requestData(self):
        try:
            #Recebe frase
            self.f1 = input("Digite sua frase: ")
            qdt = len(self.f1) + 10
            print("-"*qdt)
            print(" "*4, self.f1)
            print("-"*qdt)

        except:
            print("Algum erro não esperado aconteceu!")


            '''
            
            poderia ser ultilizado a funcao center()
            de acordo com o tamanho da frase
            
            '''

if __name__ == "__main__":
    while True:
        i = Frase()
        i.requestData()

        print("\n\n\n")
