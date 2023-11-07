d= {}
for i in range(5):
    nome = input(f"Digite seu nome: ")
    idade = int(input(f"Digite digite sua idade: "))
    d[nome] = idade
    idades = list (d.values())
    media = sum(idades)/len(idades)
maior_nome = ""
media_idade = media

for nome, idade in d.items():
     if idade > media_idade:
        print(f"Nome: {nome}")