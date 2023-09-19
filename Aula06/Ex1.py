numero= int(input("Entre com número: "))

if numero % 3 == 0 and numero % 5 == 0:
    resultado = "Divisivel por 3 e por 5 ao mesmo tempo"
else:
    resultado = "Não divisivel por 3 e por 5 ao mesmo tempo"

print(f"Numero {numero} é {resultado}")