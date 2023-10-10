lista = []

for i in range(10):
    lista.append(int(input(f"Digite o n° {i+1}: ")))

lista.reverse()

for i in lista [::-1]:
    print (i, end=" ")

print(lista)