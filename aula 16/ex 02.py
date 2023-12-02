lista = []

def primo(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

def cont_primo(n):
    qtd = 0
    for i in range(1, n+1):
        if primo(i):
            qtd = qtd +1
            lista.append(i)
    return qtd

def soma_lista(qtd):
    total = 0
    for i in qtd[::]:
        total += i
    return total


valor = int(91)
print(primo(valor))
print(f" A quantidade de primos é : {cont_primo(valor)} ")
print(lista)
print(soma_lista(lista))


