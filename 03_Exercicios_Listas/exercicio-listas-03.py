'''
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''

print("**********************************")
print("*******NOTAS**E**MEDIAS***!*******")
print("**********************************")

lista_notas = []

for i in range(4):
    notas = int(input(f'Digite a {i + 1}º nota:   '))
    lista_notas.append(notas)
    
media = sum(lista_notas) / len(lista_notas) 

print(f'A notas são {lista_notas} e a média é {media}')