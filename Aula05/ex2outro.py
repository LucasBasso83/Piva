nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
notaexame = 0
media = (nota1 + nota2 + nota3) /3

if media < 3.0:
    resultado = "Reprovado"
else:
    if media < 7:
        resultado = "Exame"
        notaexame = 12 - media
    else:
        resultado = "Aprovado"

print(f"Média {media:5.2f} - {resultado}")
if notaexame !=0:
    print(f"Tem que tirar no mínimo {notaexame:5.2f}")

