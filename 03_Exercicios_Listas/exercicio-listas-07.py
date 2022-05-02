'''
Faça um programa que leia um vetor de 5 numeros inteiros, mostre a soma, a multiplicação e os numeros.
'''

print("**********************************")
print("****SOMA**E**MULTIPLICAÇÃO**!*****")
print("**********************************")

lista_numeros = []
multiplicacao = 1

for i in range(5):
    numero = int(input(f'Digite o {i + 1}º numero:  '))
    lista_numeros.append(numero)
    multiplicacao *= numero
    
print(f'\n\
A soma dos numeros é {sum(lista_numeros)} \n\
A multiplicacao do numeros é {multiplicacao} \n\
Os numeros utilizados são {lista_numeros}')