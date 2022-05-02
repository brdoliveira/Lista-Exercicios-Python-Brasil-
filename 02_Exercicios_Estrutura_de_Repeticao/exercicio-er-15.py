'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo.
'''

print('*************************************')
print('**********Fibbonacci********!********')
print('*************************************')

numero_final = int(input('Digite um numero:   '))

primeira_parte = 0
segunda_parte = 1

lista_fibbonacci = []

for i in range(1 , numero_final):
    fibonacci = primeira_parte + segunda_parte
    segunda_parte = primeira_parte
    primeira_parte = fibonacci
    lista_fibbonacci.append(fibonacci)
    
print(lista_fibbonacci)