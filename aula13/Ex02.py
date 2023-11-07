def ehprimo(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

valor = int(input("Digite o número: "))
if ehprimo(valor):
    print("O número é primo!")
else:
    print("O número não é primo!")