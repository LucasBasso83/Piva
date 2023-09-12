numero= int(input("Entre com número: "))

if numero % 2 == 0:
    resultado = "Par"
else:
    resultado = "Impar"

print(f"Numero {numero} é {resultado}")