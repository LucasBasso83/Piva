nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
notaexame = 0
media = (nota1 + nota2 + nota3) /3

if media < 3.0:
    print(f"Média {media:5.2f} Reprovado")
else:
    if media < 7:
        print(f"Média {media:5.2f} Exame")
        print("Você tem que tirar no mínimo: ", 12 - media)
    else:
        if media < 10:
            print(f"Média {media:5.2f} Aprovado")
if notaexame !=0:
    print(f"Tem que tirar no mínimo {notaexame:5.2f}")

