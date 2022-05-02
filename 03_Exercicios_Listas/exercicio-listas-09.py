'''
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
'''

print("**********************************")
print("****NUMEROS**AO**QUADRADO**!******")
print("**********************************")

lista_numeros = []
lista_numeros_ao_quadrado = []

for i in range(10):
    numero = int(input(f'Digite o {i +1}º numero:   '))
    lista_numeros.append(numero)
    lista_numeros_ao_quadrado.append(numero ** 2)
    
print(f'\n\
A lista dos vetores : {lista_numeros}  \n\
A lista dos vetores ao quadrado: {lista_numeros_ao_quadrado}')