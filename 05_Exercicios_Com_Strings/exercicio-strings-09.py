'''
Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número
válido ou inválido através da validação dos dígitos verificadores e dos caracteres de formatação.
'''

print("**********************************")
print("****VERIFICAÇÃO***DE***CPF***!****")
print("**********************************")
cpf = input('Informe o CPF:   ')


def validaCPF(cpf):
    
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    if (len(cpf) != 11):
        return False

    fator = 10
    soma = 0
    for i in range(0, 9):
        soma += (int(cpf[i]) * fator)
        fator -= 1

    resto = soma % 11

    if (resto < 2):
        digito1 = 0
    else:
        digito1 = 11 - resto

    fator = 11
    soma = 0
    for i in range(0, 10):
        soma += (int(cpf[i]) * fator)
        fator -= 1

    resto = soma % 11

    if (resto < 2):
        digito2 = 0
    else:
        digito2 = 11 - resto

    if (int(cpf[9]) == digito1) and (int(cpf[10]) == digito2):
        return True

    return False


if (validaCPF(cpf)):
    print('CPF VÁLIDO !!!')
else:
    print('CPF INVÁLIDO !!!')


