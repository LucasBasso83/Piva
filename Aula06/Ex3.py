Largura = float(input("Digite a largura em metros: "))
Comprimento = float(input("Digite o comprimento em metros: "))
Altura = 2.80
Larguraporta = 0.80
Alturaporta = 2.10
Areatotal = 2 * Altura * (Largura + Comprimento) - (Larguraporta*Alturaporta)
Rendimentotinta = 0.33
Quantidade_tinta = Areatotal * Rendimentotinta
Rendimento_lata = float(input("Digite o rendimento de uma lata de tinta em litros: "))
Numerolatas = Quantidade_tinta / Rendimento_lata

print(f"Você precisará de {Numerolatas:.2f} latas de tinta.")