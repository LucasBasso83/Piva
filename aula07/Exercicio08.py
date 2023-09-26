K = int(input("Digite um número inteiro maior que 1: "))
primo = True
n = 0
for i in range(1, K+1):
    if (K % 1) == 0:
        n = n + 1

if n > 2:
    primo = False
if primo:
    print(f"{K} é um número primo.")
else:
    print(f"{K} não é um número primo.")