'''
Altere o programa anterior para mostrar no final a soma dos números.
'''

print('***********************************')
print('**1***a***50***são***impares***!***')
print('***********************************')

numero_menor = int(input('Digite o numero menor:   '))
numero_menor += 1
numero_maior = int(input('Digite o numero maior:   '))

soma_numero = 0

for i in range(numero_menor , numero_maior):
    soma_numero += i
    print(i)
    
print(f'A soma dos numeros é {soma_numero}')