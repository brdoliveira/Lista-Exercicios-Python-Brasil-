'''
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''

print("**********************************")
print("*******INSIRA***NUMEROS***!*******")
print("**********************************")

lista_numeros = []

for i in range(10):
    numero = int(input(f'Digite o {i + 1}º numero:   '))
    lista_numeros.append(numero)

print(lista_numeros[::-1])