# Aprendendo sobre decoradores

def letras(maior):
    def qualquer():
        f = maior()
        letra = f.upper()
        return letra

    return qualquer()


@letras
def armazena():
    return "Ola pessoal, meu nome é Silas!!"

print(armazena)
