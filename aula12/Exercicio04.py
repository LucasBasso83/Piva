lista1 = []
lista2 = []
for i in range(1,6):
    lista1.append(int(input("Digite o numeroda primeira lista: ")))

for i in range(1,6):
    lista2.append(int(input("Digite o numero das segunda lista: ")))

uniao = set(lista1).union(set(lista2))
print(f"{uniao}")