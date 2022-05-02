'''
Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
'''
from math import floor

print("**********************************")
print("****NUMERO***POR***EXTENSO***!****")
print("**********************************")


def numero_extenso(numero):
    dezenas = ['', '', 'vinte', 'trinta', 'quarenta',
        'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
    primeira_dezena = ['dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
    unidades = ['zero', 'um', 'dois', 'tres', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove']
    
    if (numero < 0) or (numero > 99):
        print('O numero informado deve estar entre 0 e 99')
    else:
        dezena = floor(numero / 10)
        unidade = floor(numero % 10)

        if (numero >= 20):
            print('%s' % dezenas[dezena], end="")
            if (unidade != 0):
                print(' e %s' % unidades[unidade], end="")
            print
        elif (numero >= 10):
            print('%s' % primeira_dezena[unidade], end="")
        else:
            print('%s' % unidades[unidade], end="")

numero = int(input('Digite um numero:   '))
numero_extenso(numero)

