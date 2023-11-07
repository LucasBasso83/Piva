
def conv_horas(x,y,z):
    hora = x * 3600
    minuto = y * 60
    segundo = z
    return hora+minuto+segundo

valor1 = int(input("Entre com as horas: "))
valor2 = int(input("Digite com os minutos: "))
valor3 = int(input("Digite com os segundos: "))
print(f"Os segundos são {conv_horas(valor1, valor2, valor3)}")
