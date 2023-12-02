numero = '3011392323043'
def calcular_soma(numero):
    soma = 0
    qtd = len(numero)
    for i in range(0, qtd):
        soma += int(numero[i])
    return soma

def calcular_multiplicacao(numero):
    multi = 1

    qtd = len(numero)
    for i in range(0, qtd):
        multi *= int(numero[i])

    return multi

print(calcular_soma(numero))
print(calcular_multiplicacao(numero))
