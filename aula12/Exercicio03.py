d= {}
for i in range(5):
    sobrenome = input(f"Digite seu sobrenome: ")
    idade = int(input(f"Digite digite sua idade: "))
    d[sobrenome] = idade

maior_sobrenome = ""
maior_idade = 0
for sobrenome, idade in d.items():
     if idade > maior_idade:
        maior_idade = idade
        maoir_sobrenome = sobrenome

print(f"O sobrenome com o maior valor é {maior_sobrenome}")

