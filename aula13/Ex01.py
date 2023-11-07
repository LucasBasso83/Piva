def par(numero):
    if (numero % 2 == 0):
        return True
    else:
        return False

numero = int(input("Digite o número: "))
if par(numero):
    print("O número é par!")
else:
    print("O número é impar!")