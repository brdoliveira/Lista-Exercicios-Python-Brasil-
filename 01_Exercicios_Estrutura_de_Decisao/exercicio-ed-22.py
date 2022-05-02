'''
Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
'''

print("****************************************")
print("***********PAR***OU***IMPAR***!*********")
print("****************************************")

numero = float(input("Digite o numero desejado:  "))

validacao_par = numero % 2 == 0

if validacao_par:
    print("O numero é par!")
else:
    print("O numero é impar!")
    