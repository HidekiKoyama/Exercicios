'''
Crie uma tupla preenchida com os 10 filmes mais assistidos de todos os tempos, e depois mostre:

    Apenas os 3 primeiros mais assistidos
    Os últimos 2 mais assistidos
    A lista em ordem alfabética
    Em que posição está “O rei leão”

'''
class Calculo():

    def base(self):
        self.tup = (
            'Avatar'
            ,'Vingadores: Ultimato'
            ,'Avatar: O Caminho da Água'
            ,'Titanic'
            ,'Star Wars: O Despertar da Força'
            ,'Vingadores: Guerra Infinita'
            ,'Homem-Aranha: Sem Volta para Casa'
            ,'Jurassic World'
            ,'O Rei Leão'
            , 'Marvel Os Vingadores')

        for i in self.tup:
            print(i)

        return self.tup


    def buscaPosicao(self, p):
        a = self.tup[p-1]
        print(a)

    def buscaPosicaoNome(self, film):
        a = self.tup.index(film)
        print(a)

    def top3(self):
        for n, i in enumerate(self.tup):
            if n < 3 and i != None:
                print(i)

    def down2(self):
        for n, i in enumerate(self.tup):
            if n > 7 and i != None:
                print(i)

    def orderBy(self):
        a = sorted(self.tup)
        print(a)
        
if __name__ == "__main__":
    i = Calculo()
    print("*==*" * 10)
    print("Abaixo a lista dos filmes mais assistidos!!")
    m = i.base()
    print("\n\n\n")


    print("*==*" * 10)
    print("Os três mais assistidos da lista são: ")
    print(i.top3())

    print("*==*" * 10)
    print("Os dois ultimos da lista são: ")
    print(i.down2())

    print("*==*" * 10)
    print("Os filmes em ordem alfabetica: ")
    print(i.orderBy())

    p = m.index("O Rei Leão") + 1
    print(f"A posição do Filme Rei Leão é: {p}")


