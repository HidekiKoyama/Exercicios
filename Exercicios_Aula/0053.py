'''
Crie um programa que vai gerar 10 números aleatórios e coloque em uma tupla.

Depois disso mostre a listagem de números gerados e indique o menor e o maior que estão na tupla
'''

import random as r

class Calculo():

    def base(self):
        n1 = r.randint(1, 100)
        n2 = r.randint(1, 100)
        n3 = r.randint(1, 100)
        n4 = r.randint(1, 100)
        n5 = r.randint(1, 100)
        n6 = r.randint(1, 100)
        n7 = r.randint(1, 100)
        n8 = r.randint(1, 100)
        n9 = r.randint(1, 100)
        n10 = r.randint(1, 100)

        self.tup = (n1, n2, n3, n4, n5, n6, n7, n8, n9, n10)
        for i in self.tup:
            print(i)

    def maior(self):
        return max(self.tup)

    def menor(self):
        return min(self.tup)


if __name__ == "__main__":
    i = Calculo()
    print("*==*" * 10)
    print("Seus números gerados!!")
    i.base()
    print("*==*" * 10 + "\n")

    print("O maior dentre eles é: ")
    print(i.maior())
    print("O menor dentre eles é: ")
    print(i.menor())


