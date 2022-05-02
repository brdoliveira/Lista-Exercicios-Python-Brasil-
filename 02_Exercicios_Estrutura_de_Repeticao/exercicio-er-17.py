'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
'''

print('*************************************')
print('***********Fatorial********!*********')
print('*************************************')

numero_escolhido = int(input('Digite o numero que deseja sabe o fatorial:   '))
lista_fatorial = []
fatorial = 1

for i in range(numero_escolhido,0,-1):
    lista_fatorial.append(i)
    fatorial *= i
    
print(f'{lista_fatorial} = {fatorial}')
    