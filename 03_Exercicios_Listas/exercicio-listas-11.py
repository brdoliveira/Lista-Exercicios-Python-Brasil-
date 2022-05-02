'''
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
'''

print("**********************************")
print("***ELEMENTOS***INTERCALADOS***!***")
print("**********************************")

lista_A = []
lista_B = []
lista_C = []
lista_D = []

for i in range(10):
    vetor = int(input(f'Digite o {i + 1}º vetor da lista A:  '))
    lista_A.append(vetor)
    
for i in range(10):
    vetor = int(input(f'Digite o {i + 1}º vetor da lista B:  '))
    lista_B.append(vetor)
    
for i in range(10):
    vetor = int(input(f'Digite o {i + 1}º vetor da lista C:  '))
    lista_C.append(vetor)
    
for m in range(10):
    lista_D.append(lista_A[m])
    lista_D.append(lista_B[m])
    lista_D.append(lista_C[m])
    
print(f'\n\
A lista do vetor A: {lista_A} \n\
A lista do vetor B: {lista_B} \n\
A lista do vetor C: {lista_C} \n\
A lista de vetores intercaladas: \n\
{lista_D}')