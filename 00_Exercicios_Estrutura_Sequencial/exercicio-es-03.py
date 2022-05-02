'''
Faça um Programa que peça dois números e imprima a soma.
'''


print("**********************************")
print("*******INSIRA**DOIS**NUMERO*******")
print("**********************************")

numero_escolhido_um = input("Primeiro Numero Inserido:")
numero_escolhido_dois = input("Segundo Numero Inserido:")
soma = int(numero_escolhido_um) + int(numero_escolhido_dois)
print('A soma dos numeros {} e {} foi de {}'.format(numero_escolhido_um,numero_escolhido_dois,soma))