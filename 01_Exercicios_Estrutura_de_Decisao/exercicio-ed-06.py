'''
Faça um Programa que leia três números e mostre o maior deles.
'''

print("**********************************")
print("*INSIRA**NUMERO**PARA**COMPARAÇÃO*")
print("**********************************")

numero_um = float(input("INSIRA O PRIMEIRO NUMERO:  "))
numero_dois = float(input("INSIRA O SEGUNDO NUMERO:  "))
numero_tres = float(input("INSIRA O TERCEIRO NUMERO:   "))

if numero_um > numero_dois:
    if numero_um > numero_tres:
        print("O PRIMEIRO NUMERO É O MAIOR DE TODOS")
    else:
        print("O TERCEIRO NUMERO É O MAIOR DE TODOS")   
elif numero_dois > numero_um:
    if numero_dois > numero_tres:
        print("O SEGUNDO NUMERO É O MAIOR DE TODOS")
    else:
        print("O TERCEIRO NUMERO É O MAIOR DE TODOS")           
else:
    print("Algum erro apresentado no programa !")