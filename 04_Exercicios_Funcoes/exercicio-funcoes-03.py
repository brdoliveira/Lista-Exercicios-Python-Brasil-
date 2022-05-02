'''
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
'''

print("**********************************")
print('*****SOMA****DE****TRÊS*****!*****')
print("**********************************")

def soma(um, dois, tres):
    soma = um + dois + tres
    return soma

um = int(input('Digite o primeiro numero:   '))
dois = int(input('Digite o segundo numero:    '))
tres = int(input('Digite o terceiro numero:   '))

print('A soma dos três:   ' , soma(um,dois,tres))