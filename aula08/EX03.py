while True:
    valor = input('Digite os números: ')
    if valor.isnumeric() and len(valor) == 9:
        break
    if len(valor) !=9:
        print("Tem que ter 9 digitos!!")
    else:
        print('Digite apenas numeors!!')

novo_valor = valor[0] + '.' + valor[1:4] + '.' + valor[4:7] + ',' + valor[7]+valor[8]
print(f"{novo_valor}")

