pesos = 0
alturas = 0
imcs = 0

for i in range(1, 6):
    peso = float(input(f"Digite o peso da pessoa {i + 1} (em kg): "))
    altura = float(input(f"Digite a altura da pessoa {i + 1} (em metros): "))

    pesos.append(peso)
    alturas.append(altura)

peso_medio = sum(pesos) / len(pesos)

altura_media = sum(alturas) / len(alturas)

for i in range(5):
    imc = pesos[i] / (alturas[i] ** 2)
    imcs.append(imc)

maior_imc = max(imcs)
menor_imc = min(imcs)

print(f"Peso Médio: {peso_medio:.2f} kg")
print(f"Altura Média: {altura_media:.2f} metros")
print(f"Maior IMC: {maior_imc:.2f}")
print(f"Menor IMC: {menor_imc:.2f}")