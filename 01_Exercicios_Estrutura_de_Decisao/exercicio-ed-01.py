'''
Faça um Programa que peça dois números e imprima o maior deles.
'''

print("**********************************")
print("*INSIRA**NUMERO**PARA**COMPARAÇÃO*")
print("**********************************")

numero_um = float(input("INSIRA O PRIMEIRO NUMERO:  "))
numero_dois = float(input("INSIRA O SEGUNDO NUMERO:  "))

if numero_um > numero_dois:
    print("Primeiro numero é maior que o segundo !")
elif numero_dois > numero_um:
    print("Segundo numero é maior que o primeiro !")
elif numero_um == numero_dois:
    print("Primeiro numero é igual o segundo numero !")
else:
    print("Algum erro apresentado no programa !")