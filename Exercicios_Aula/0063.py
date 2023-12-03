'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
    Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta
'''

class ValidaExpressao():
            
    def validador(self, expr):
        for i in range(0, len(expr)):
            if expr[i] == "(":
                for j in range(i + 1, len(expr)):
                    if expr[j] == ")":
                        expr = expr.replace("(", " ", 1) 
                        expr = expr.replace(")", " ", 1) 
                    
        return expr
   
if __name__ == "__main__":
    v = ValidaExpressao()
    expr = input("Digite uma expressão: ")
    if "(" in v.validador(expr) or ")" in v.validador(expr):
        print("Expressão invalida!")
    else:
        print("Expressão valida!")
    