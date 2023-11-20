'''
print(1 + 2) # Soma
print( 2 * 4) # Multiplicacao
print( 5 / 6) # Divisao
print(2 ** 2) #Potencia

#####################################
x = 'Teste texto teste'
print(x)

idade = 43
print(f'Sua idade é {idade}')

############################

idade = 19
nome = 'Hideki'

print(f'Seu nome é {nome}, e sua idade é {idade}')

##########################

idade = input('Digite sua idade: ')
print(f'Sua idade é {idade}')

####################

nome = 'Gabriel'
sobrenome = 'Hideki'

Nome_completo = nome  +' ' + sobrenome

print(f'Seu nome completo é: {Nome_completo}')



n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite outro numero: '))

soma = (n1 + n2)
print(f'Sua a soma de {n1} + {n2} é igual a {soma}')
class Calcula():
    def soma(n1, n2):
        return (n1 + n2)


n1 = int(input())
n2 = int(input())
obj = Calcula



print(obj.soma(n1,n2))




Nome = input('Digite seu nome: ')
Nome = Nome.strip()

#Aqui estamnos retornando a primeira posição de uma cadeia de caracter
print(f'A primeira letra do seu nome é: {Nome[0]}')

# funcao len() diz a quantidade de caracter de sua string
print(f'A quanrtidade de letras do seu nome é: {len(Nome)}')

#Separa nossa string em uma lista
Nome = Nome.split()
print(f'Seu primeiro nome é: {Nome[0]}')


teste = [1,2,3,4,5,6,7,8,9]
a = 0
for i in teste:
    a = a + i
    print(f"Conta somada: {a}")
    print(f"Contagem {i}")

w = 0
while w <= 10:
    print(w)
    w += 1


#------------------------------------------------------------------------------------- listas
# Funcoes de string
Para manipular strings se usa funcaoes abaixo
    para deixar em maiusculo se usa as 'upper()'
    caso queira tudo minusculo se usa a funcao 'lower()'


Nome = ['Gabriel', 'Hideki', 'Koyama']
Nome = ' '.join(Nome)

print(f'Seu nome completeo é: {Nome}'
      f'\nSeu nome todo maiusculo é: {Nome.upper()}'
      f'\nSeu nome todo minuscuo é: {Nome.lower()}')

#------------------------------------------------------------------------------------- try except
Aula de try except


try:
    x = 10 / a

except ZeroDivisionError:
    print("Erro: Divisao por zero!!")

except ValueError:
    print("Digite apenas números!!")

except:
    print("Erro não categorizado!!")


def  texto():
    print('-*-' * 10)
texto()

def textoBonito(text):
    print('-*-' * 10)
    print(text)
    print('-*-' * 10)
textoBonito("olaaa")
def soma(a, b):
    return a + b

print(soma(50, 50))

#------------------------------------------------------------------------------------- tuplas
# tuplas sao imutaveis
# tuplas sao definidas por parenteses
# tuplas sao indexadas por numeros
# tuplas sao ordenadas

carro = ('Ferrari', 'Vermelha', '2023')
print(carro)

for ele in carro:
   print(ele)

for count in range(0, len(carro)):
   print(carro[count])

for pos, carac in enumerate(carro):
   print(f'Ordem de compra {carac} Cod: {pos}')


a = (1,2,3)
b = (4,5,6)

c = a + b
print(c)
del(c)
print(c)


# Mutáveis
# Representadas por []


carro = ['Ferrari', 'Vermelha', '2023']
carro [1] = 'Amarelo'
carro.append('Gasolina')     # cria no final da lista
carro.insert(1, '797 cv ')   # insere na posição 1
carro.pop(1)                 # remove o item na posição 1
carro.remove('Vermelha')     # remove o valor 'vermelha'
len(carro)                   # retorna o tamanho da lista
'''