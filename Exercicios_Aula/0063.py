'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
    Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

'''

class ValidaExpressao():
    def __init__(self, expr) -> None:
        self.expr = expr

    def validador(self):
        for _1 in range(0, len(self.expr)):
            if self.expr[_1] == "(":
                for _2 in range(_1+1, len(self.expr)):
                    self.expr = self.expr.replce("(", "", 1)
                    self.expr = self.expr.replce(")", "", 1)
                    
                    
    