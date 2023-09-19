x = float(input("Digite o valor: "))

if x <= 1000.00:
    print("Valor com desconto: ",int(x)*0.90)
elif (x > 1000.00) or (x <= 5000.00):
    print("Valor com desconto: ",int(x)*0.80)
elif x > 5000.00:
    print("Valor com desconto: ",int(x)*0.70)
else:
    print("Sem desconto")