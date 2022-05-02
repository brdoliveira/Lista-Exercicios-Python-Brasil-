'''
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
'''

print("**********************************")
print("******CALCULE**O**PESO**IDEAL*****")
print("**********************************")

altura_inserida = float(input("Digite sua altura:  "))

peso = (72.2 * altura_inserida) - 58

print(" A altura é {} e o pesoa ideal é {:.1f}".format(altura_inserida,peso))