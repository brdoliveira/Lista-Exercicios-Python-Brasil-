'''
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
'''

print('*************************************')
print('****NUMEROS*****INVERTIDOS*****!*****')
print('*************************************')

numero_digitado = str((input('DIGITE UM NUMERO:   ')))
numero_inverso = numero_digitado[::-1]
    
print(f'NUMERO INVERTIDO:   {numero_inverso}')
    