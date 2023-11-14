def valida_cpf(cpf):
    soma1 = (int(cpf[0]) * 10) + (int(cpf[1]) * 9) + (int(cpf[2]) * 8) + (int(cpf[4]) * 7) + (int(cpf[5]) * 6) + (
            int(cpf[6]) * 5) + (int(cpf[8]) * 4) + (int(cpf[9]) * 3) + (int(cpf[10]) * 2)
    resto1 = soma1 % 11
    if resto1 < 2:
        dig1 = 0
    else:
        dig1 = 11 - resto1
    if dig1 != int(cpf[12]):
        return False

    soma2 = (int(cpf[0]) * 11) + (int(cpf[1]) * 10) + (int(cpf[2]) * 9) + (int(cpf[4]) * 8) + (int(cpf[5]) * 7) + (
            int(cpf[6]) * 6) + (int(cpf[8]) * 5) + (int(cpf[9]) * 4) + (int(cpf[10]) * 3) + (int(cpf[12]) * 2)
    resto2 = soma2 % 11
    if resto2 < 2:
        dig2 = 0
    else:
        dig2 = 11 - resto2
    if dig2 != int(cpf[13]):
        return False
    return True


cpf_input = input("Digite o CPF (XXX.XXX.XXX-XX):")

if valida_cpf(cpf_input):
    print("CPF válido")
else:
    print('CPF inválido')
