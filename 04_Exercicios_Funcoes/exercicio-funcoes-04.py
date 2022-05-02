'''
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, 
se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
'''

print("**********************************")
print('***NEGATIVO***OU***POSITIVO***!***')
print("**********************************")

def positivo_negativo(n):
    if n < 0:
        print('N')
    elif n > 0:    
        print('P')
    else:
        print('O numero é 0')

n = positivo_negativo(int(input('Digite um numero:   ')))

