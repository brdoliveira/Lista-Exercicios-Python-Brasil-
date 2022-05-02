'''
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
'''


print("**********************************")
print("********NOTAS***BIMESTRAIS********")
print("**********************************")

numero_um = int(input("Primeiro Numero:  "))
numero_dois = int(input("Segundo Numero:  "))
numero_tres = int(input("Terceiro Numero:  "))
numero_quatro = int(input("Quarto Numero:  "))

lista_notas = [numero_um,numero_dois,numero_tres,numero_quatro]
soma_notas = sum(lista_notas)
media_notas = soma_notas / len(lista_notas)
print('A nota das médias é {}'.format(media_notas))
