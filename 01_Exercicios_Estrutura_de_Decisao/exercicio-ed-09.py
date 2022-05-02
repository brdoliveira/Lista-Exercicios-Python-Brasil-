'''
Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

print("**********************************")
print("*INSIRA**NUMERO**PARA**COMPARAÇÃO*")
print("**********************************")

numero_um = float(input("INSIRA O PRIMEIRO NUMERO:  "))
numero_dois = float(input("INSIRA O SEGUNDO NUMERO:  "))
numero_tres = float(input("INSIRA O TERCEIRO NUMERO:   "))

maior = 0
medio = 0
menor = 0

if numero_um > numero_dois:
    if numero_um > numero_tres:
        if numero_tres > numero_dois:
            maior = numero_um
            medio = numero_tres
            menor = numero_dois
        else:
            maior = numero_um
            medio = numero_dois
            menor = numero_tres
    else:
        maior = numero_tres
        medio = numero_um
        menor = numero_dois

elif numero_dois > numero_um:
    if numero_dois > numero_tres:
        if numero_tres > numero_um:
            maior = numero_dois
            medio = numero_tres
            menor = numero_um
        else:
            maior = numero_dois
            medio = numero_um
            menor = numero_tres
    else:
        maior = numero_tres
        medio = numero_dois
        menor = numero_um
else:
    print("Algum erro apresentado no programa !")
    
print(f'MENOR: {menor}, MEDIO: {medio}, MAIOR: {maior}')