'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500.
'''

print('*************************************')
print('**********Fibbonacci********!********')
print('*************************************')

primeira_parte = 0
segunda_parte = 1

lista_fibbonacci = []

while primeira_parte < 500:
    fibonacci = primeira_parte + segunda_parte
    segunda_parte = primeira_parte
    primeira_parte = fibonacci
    lista_fibbonacci.append(fibonacci)
    
print(lista_fibbonacci)