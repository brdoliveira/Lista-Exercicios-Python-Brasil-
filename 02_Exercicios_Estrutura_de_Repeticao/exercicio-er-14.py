'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
'''

print('*************************************')
print('**Quantidade**de**par**ou**impar**!**')
print('*************************************')

quantidade_pares = 0
quantidade_impares = 0

for i in range(1,11):
    numero = int(input(f'Digite o {i}º numero:   '))
    if numero % 2 == 0:
        quantidade_pares += 1
    else:
        quantidade_impares += 1
        
print(f'A quantidade de numeros pares é {quantidade_pares} e a quantidade de impares é {quantidade_impares}')