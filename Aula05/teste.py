# Altura das paredes
altura_paredes = 2.80

# Dimensões da porta
largura_porta = 0.80
altura_porta = 2.10

# Área total das paredes
largura_parede = float(input("Digite a largura das paredes em metros: "))
comprimento_parede = float(input("Digite o comprimento das paredes em metros: "))
area_total_paredes = 2 * altura_paredes * (largura_parede + comprimento_parede) - (largura_porta * altura_porta)

# Rendimento de tinta por metro quadrado
rendimento_tinta = float(input("Digite o rendimento de tinta por metro quadrado: "))

# Calcula a quantidade de tinta necessária
quantidade_tinta = area_total_paredes * rendimento_tinta

# Rendimento de uma lata de tinta (em litros)
rendimento_lata = float(input("Digite o rendimento de uma lata de tinta em litros: "))

# Calcula o número de latas necessárias
numero_latas = quantidade_tinta / rendimento_lata

print(f"Você precisará de {numero_latas:.2f} latas de tinta.")