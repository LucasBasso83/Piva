# Definição de funções
qtd = 5
x = 10
def desenha(qtd):
    # print ("--------------------")
    print(qtd, "dentro", x)
    for i in range(0, qtd):
        print("-", end="")
    print()

desenha (25)
print(qtd, "fora", x)
print(" ** usando funções ** ")
desenha(30)
