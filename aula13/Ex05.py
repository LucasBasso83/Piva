import math
def raio(n):
    multiplicar = (4*math.pi * n**3)/3
    return multiplicar


valor = float(input("Digite o número: "))
print(f"O volume é {raio(valor):.3f}")