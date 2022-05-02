'''
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
'''

print("****************************************")
print("**INSIRA*UM*VALOR*POSITIVO*OU*NEGATIVO**")
print("****************************************")

numero_inserido = float(input("DIGITE UM NUMERO POSITIVO OU NEGATIVO:  "))

if numero_inserido == 0:
    print("O NUMERO É IGUAL A ZERO(0) !")
elif numero_inserido <= 0:
    print("NUMERO É NEGATIVO !")
elif numero_inserido >= 0:
    print("NUMERO É POSITIVO !")
else:
    print("ERROS APRESENTADOS !")