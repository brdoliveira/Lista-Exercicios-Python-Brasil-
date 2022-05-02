'''
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser 
compostos pelos elementos intercalados dos dois outros vetores
'''

print("**********************************")
print("***ELEMENTOS***INTERCALADOS***!***")
print("**********************************")

lista_A = []
lista_B = []
lista_C = []

for i in range(10):
    vetor = int(input(f'Digite o {i + 1}º vetor da lista A:  '))
    lista_A.append(vetor)
    
    
    
for i in range(10):
    vetor = int(input(f'Digite o {i + 1}º vetor da lista B:  '))
    lista_B.append(vetor)
    
    
for m in range(10):
    lista_C.append(lista_A[m])
    lista_C.append(lista_B[m])
    
print(f'\n\
A lista do vetor A: {lista_A} \n\
A lista do vetor B: {lista_B} \n\
A lista de vetores intercaladas: \n\
{lista_C}')