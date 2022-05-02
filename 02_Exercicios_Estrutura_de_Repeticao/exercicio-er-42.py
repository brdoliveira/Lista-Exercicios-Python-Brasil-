'''
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: 
[0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
'''
print('***********************************************')
print('***Intervalos******de******numeros******!******')
print('***********************************************')

numero = 0

intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

while (numero >= 0):
    numero = int(input('Informe um numero: '))

    if (numero >= 0):
        if (numero <= 25):
            intervalo_0_25 += 1
        elif (numero <= 51):
            intervalo_26_50 += 1
        elif (numero <= 75):
            intervalo_51_75 += 1
        elif (numero <= 100):
            intervalo_76_100 += 1

print(f'{intervalo_0_25} numeros no intervalo [0-25]')
print(f'{intervalo_26_50} numeros no intervalo [26-50]')
print(f'{intervalo_51_75} numeros no intervalo [51-75]')
print(f'{intervalo_76_100} numeros no intervalo [75-100]')