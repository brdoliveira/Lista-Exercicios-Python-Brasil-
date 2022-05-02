'''
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
'''

print("**********************************")
print('*****FUNÇÃO****PIRAMIDE*****!*****')
print("**********************************")

def piramide(n):
    for i in range(1 , n + 1):
        linha_numeros = ''
        for _ in range(0 , i) :
            numero = f'{i}  ' 
            linha_numeros += numero
        print(linha_numeros)

numero_inserido = piramide(int(input('Digite um numero:   ')))