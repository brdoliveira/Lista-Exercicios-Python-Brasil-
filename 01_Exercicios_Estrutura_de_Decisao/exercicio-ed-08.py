'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato.
'''


print("***********************************")
print("**INSIRA*PRODUTOS*PARA*COMPARAÇÃO**")
print("***********************************")

numero_um = float(input("INSIRA O PRIMEIRO PRODUTO:  "))
numero_dois = float(input("INSIRA O SEGUNDO PRODUTO:  "))
numero_tres = float(input("INSIRA O TERCEIRO PRODUTO:   "))

if numero_um > numero_dois:
    if numero_um > numero_tres:
        print("O TERCEIRO PRODUTO TEM O MENOR VALOR DE TODOS")           
    else:
        print("O SEGUNDO PRODUTO TEM O MENOR VALOR DE TODOS")
elif numero_dois > numero_um:
    if numero_dois > numero_tres:
        print("O TERCEIRO PRODUTO TEM O MENOR VALOR DE TODOS")           
    else:
        print("O PRIMEIRO PRODUTO TEM O MENOR VALOR DE TODOS")
else:
    print("Algum erro apresentado no programa !")