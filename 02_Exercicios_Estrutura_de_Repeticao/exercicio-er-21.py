'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
'''

print('*************************************')
print('*******Numero****Primo*****!*********')
print('*************************************')

numero_escolhido = int(input('Digite o numero que deseja sabe é primo :   '))
quantidade_divisiveis = 0

for i in range(1,numero_escolhido):
    if (numero_escolhido % i == 0):
        quantidade_divisiveis += 1
        
        
if quantidade_divisiveis > 2:
    print(f'O numero não é primo !')    
else:
    print('O numero é primo !')