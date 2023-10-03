palavra = input('Digite sua frase: ')
palavra.lower()
vogais = palavra.count("a") + palavra.count("e") + palavra.count("i") + palavra.count("o") + palavra.count("u")
print(f"A frase possui {vogais} vogais")