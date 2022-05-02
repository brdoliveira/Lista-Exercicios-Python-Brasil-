'''
Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

print('***********************************')
print('****Digite****5****numeros****!****')
print('***********************************')

lista_numeros = []

for i in range(1,6):
    numeros = int(input(f'Digite o numero {i} :'))
    lista_numeros.append(numeros)

soma = sum(lista_numeros)
media = soma / len(lista_numeros)

print(f' A soma é {soma} e a media é {media}')
