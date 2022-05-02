'''
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
'''

print("***********************************")
print("***IMPRIMA***AS***CONSOANTES***!***")
print("***********************************")

letras = []
vogais = ['A', 'E', 'I', 'O', 'U']

for i in range(0, 10):
    letras.append(input('Informe uma letra:   ').upper())

total_consoantes = 0
lista_consoantes = []
for i in range(0, 10):
    if letras[i] not in vogais:
        lista_consoantes.append(letras[i])
        total_consoantes += 1
    
print(f'O numero de consoantes foi de {total_consoantes} elas são {lista_consoantes}')