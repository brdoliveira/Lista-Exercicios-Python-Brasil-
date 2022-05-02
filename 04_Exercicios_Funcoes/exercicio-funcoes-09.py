'''
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
'''

print("**********************************")
print('********NUMERO***INVERSO***!******')
print("**********************************")

def inverter(numero):
    invertido = int(numero[::-1])
    return invertido

numero = str(input('Digite um numero:   '))

print('O numero é {} e ele invertido é {}'.format(numero, inverter(numero)))
    