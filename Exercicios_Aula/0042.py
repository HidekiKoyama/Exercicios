'''

Simulação de um Caixa Eletrônico Este programa simula um
    caixa eletrônico, permitindo que o

        usuário faça
            depósitos,
            saques e
            consulte o saldo da conta,

        e sair

'''

class CaixaEletronico():

    def __init__(self):
        self.saldo = 0

    def deposito (self, valor):
        self.saldo = self.saldo + valor
    def saque(self, valor):
        if valor > self.saldo:
            print("Seu saldo é insulficiente!!"
                  "\n Tente outro valor ou faça um saque!!")
            pass
        else:
            self.saldo -= valor

    def consultar(self):
        return self.saldo

sys = True
c = CaixaEletronico()

while sys:
    acao = int(input("O que deseja realizar:"
                     "\n1 - Depósitos"
                     "\n2 - Saques"
                     "\n3 - Consultar Saldo"
                     "\n4 - Sair\n"))

    if acao == 1:
        valor = float(input("\nDigite o valor que deseja depositar: "))
        c.deposito(valor)

    elif acao == 2:
        valor = float(input("\nDigite o valor que deseja sacar: "))
        c.saque(valor)

    elif acao == 3:
        print(f"\nSeu saldo atual é: {c.consultar()}\n")

    else:
        break