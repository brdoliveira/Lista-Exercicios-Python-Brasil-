'''
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.
'''

print("**********************************")
print("******ALTURA***E***IDADES**!******")
print("**********************************")

lista_altura = [] 
lista_idades = []

for i in range(5):
    altura = float(input(f'Digite a {i + 1}º altura:   '))
    idade = int(input(f'Digite a {i + 1}º idade:    '))
    lista_altura.append(altura)
    lista_idades.append(idade)
    

print(f'Lista de altura ordem inversa {lista_altura[::-1]} \n\
Lista de idade ordem inversa {lista_idades[::-1]}')