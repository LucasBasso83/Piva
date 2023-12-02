def calcular_animais(cabecas, pes):

    patos = (pes - 4 * cabecas)
    coelhos = cabecas - patos

    return int(patos), int(coelhos)

cabecas = 91
pes = 136


resultado = calcular_animais(cabecas, pes)
print(f"Número de patos: {resultado[0]}, Número de coelhos: {resultado[1]}")
