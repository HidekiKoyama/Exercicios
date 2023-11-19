class Objeto():
    def __init__(self, idade):
        self.idade = idade
        self.animiais = ['cachorro', 'gato', 'papagaio', 'peixe']

    def showData(self):
        print(f"Sua idade é {self.idade}")

# o __del__ é chamado quando o objeto é destruido

    def __del__(self):
        print("Seu objeto foi desconstruido!!")
        
# o __add__ é chamado quando o objeto é somado
    def __add__(self, outro):
        return Objeto(self.idade + outro.idade)
   
#Serve para mostrar o objeto como string 
    def __str__(self):
        return f"Olha só, a idade é {self.idade}"

#o   serve para mostrar o tamanho do objeto
    def __len__(self):
        return len(self.animiais)

if __name__ == "__main__":
    o = Objeto(25)
    o1 = Objeto(36)
    ger = o + o1
    del o, o1
    print(ger)
    print(len(ger))