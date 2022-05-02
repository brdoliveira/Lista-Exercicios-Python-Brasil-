'''
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
'''

print("**********************************")
print('***QUANTIDADE***DE***DIGITOS**!***')
print("**********************************")

def quantidade_digitos(numero):
    return len(str(numero))

numero = int(input('Digite um numero:   '))

print('Quantidade de dígitos:  ', quantidade_digitos(numero))