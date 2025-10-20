# calculadora.py
# Projeto colaborativo - GitHub Desktop
# Autor: Cristiana e Tiago

def soma(a,b):
    """Retorna a soma de dois números. """
    return a+b

def subtrai(a,b):
    """Retorna a subtração de dois números."""
    return a - b
print("Calculadora colaborativa!")
print("Soma: ", soma(5, 3))
print("Substração: ", subtrai(10,4))

def multiplica(a,b):
    """Retorna o produto de dois números. """
    return a*b

def divide(a,b):
    """Retorna a divisão de dois números, se possível. """
    if b!=0:
        return a/b
    else:
        return "Erro: Divisão por 0!"

print("Multiplicação: ", multiplica(2, 6))
print("Divisão: ", divide(10,2))


def potencia(a,b):
    """Retorna a potência de dois números. """
    a=1
    for i in range(b):
        a=a*b
    return a^b

print("Potência: ", potencia(10,2))