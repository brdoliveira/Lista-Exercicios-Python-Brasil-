'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

print('*************************************')
print('*******Numero****Primo*****!*********')
print('*************************************')

numero_escolhido = int(input('Digite o numero que deseja sabe é primo :   '))
lista_divisiveis = []

for i in range(1,numero_escolhido):
    if (numero_escolhido % i == 0):
        lista_divisiveis.append(i)
        
        
if len(lista_divisiveis) > 2:
    print(f'O numero não é primo , é são divisiveis são {lista_divisiveis}')    
else:
    print('O numero é primo !')