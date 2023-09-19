x = float(input("Defina o valor de x: "))
y = float(input("Defina o valor de y: "))
z = float(input("Defina o valor de z: "))

if (x < y + z) and (y < x + z) and (z < x + y):
    print(f"As medidas: {x}, {y}, {z} formam um triângulo")
    if (x == y) and (x == z):
          print("Equilátero")
    elif (x == y) or (x == z) or (y == z):
          print("Isósceles")
    else:
        print("Escaleno")
else:
    print(f"As medidas: {x}, {y}, {z} não formam um triângulo")