'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

print("**********************************")
print("******CALCULE**O**PESO**IDEAL*****")
print("**********************************")
print("(1) Homem (2) Mulher")

h_ou_m = int(input("Digite:   "))
altura_inserida = float(input("Digite sua altura:  "))

if h_ou_m == 1:
    peso = (72.2 * altura_inserida) - 58
elif h_ou_m == 2:
    peso = (62.1 * altura_inserida) - 44.7


print(" A altura é {} e o pesoa ideal é {:.1f}".format(altura_inserida,peso))