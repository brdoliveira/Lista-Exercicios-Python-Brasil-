'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes 
e limitando o fatorial a números inteiros positivos e menores que 16.
'''

print('*************************************')
print('***********Fatorial********!*********')
print('*************************************')

numero_escolhido = int(input('Digite o numero que deseja sabe o fatorial:   '))
lista_fatorial = []
fatorial = 1
if numero_escolhido >= 0 and numero_escolhido <= 16:
    for i in range(numero_escolhido,0,-1):
        lista_fatorial.append(i)
        fatorial *= i
else:
    print('O numero não está entre 0 e 16')

if len(lista_fatorial) != 0:
    print(f'{lista_fatorial} = {fatorial}')
    