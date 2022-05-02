'''
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
'''

print("**********************************")
print("*******INSIRA***NUMEROS***!*******")
print("**********************************")

lista_numeros = []

for i in range(5):
    numero = int(input(f'Digite o {i + 1}º numero:   '))
    lista_numeros.append(numero)

print(lista_numeros)