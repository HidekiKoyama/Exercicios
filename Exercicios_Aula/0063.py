'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta


'''

p = str(input("digite sua expressão: "))

for i in range(0, len(p)):
    if p[i] == "(":
        for i2 in range(i + 1, len(p)):
            if p[i2] == ")":
                p.replace("(", "a", 1)
                p.replace(")", "b", 1)

print(p)
if "(" in p or ")" in p:
    print("expressão inválida!!")

else:
    print("Expressão válida!")
