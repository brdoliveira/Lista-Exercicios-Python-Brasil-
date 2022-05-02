'''
Faça um programa que leia 5 números e informe o maior número.
'''

print('***********************************')
print('****Digite****5****numeros****!****')
print('***********************************')

lista_numeros = []

for i in range(1,6):
    numeros = int(input(f'Digite o numero {i} :'))
    lista_numeros.append(numeros)

maior_numero = max(lista_numeros)    
print(f'O maior numero da lista é {maior_numero}')
