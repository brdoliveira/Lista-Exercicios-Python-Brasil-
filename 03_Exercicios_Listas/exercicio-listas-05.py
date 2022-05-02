'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números
IMPARES no vetor impar. Imprima os três vetores.
'''

print("***********************************")
print("*****IMPARES****E****PARES****!****")
print("***********************************")

lista_numeros = []
lista_impares = []
lista_pares = []

for i in range(20):
    numero = int(input(f'Digite o {i + 1}º numero:   '))
    lista_numeros.append(numero)
    if numero % 2 == 0:
        lista_pares.append(numero)
    if numero % 2 == 1:
        lista_impares.append(numero)
        
print(f'\n\
Os numeros são {lista_numeros} \n\
A lista de pares são {lista_pares} \n\
E os impares são {lista_impares}')