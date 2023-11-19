'''
Escreva um programa que tenha uma função, maior(), que receba vários parâmetros e retorne qual é o maior deles
'''

class funcaoMaior():
    def requestData(self, *n):
        list = []
        try:
            for i in n:
                list.append(i)
            print(max(list))

        except ValueError:
            print("Apenas números, por favor!!")

        except:
            print("Algum erro não esperado aconteceu!")

if __name__ == "__main__":
    i = funcaoMaior()
    i.requestData(20, 30, 1, 50, 90, 99, 60)

