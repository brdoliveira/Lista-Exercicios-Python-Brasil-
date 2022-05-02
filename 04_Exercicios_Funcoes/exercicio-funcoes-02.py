'''
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
'''

print("**********************************")
print('*****FUNÇÃO****PIRAMIDE*****!*****')
print("**********************************")

def piramide(n):
    for i in range(1 , n + 1):
        linha_numeros = ''
        for m in range(1 , i + 1):
            numero = f'{m}  ' 
            linha_numeros += numero
        print(linha_numeros)

numero_inserido = piramide(int(input('Digite um numero:   ')))