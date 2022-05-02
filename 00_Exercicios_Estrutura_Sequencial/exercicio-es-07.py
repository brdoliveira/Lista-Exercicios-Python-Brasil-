'''
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
'''

print("**********************************")
print("********AREA**DO**QUADRADO********")
print("**********************************")

# área A = b (base) . h (altura)
base = input("Digite a base do quadrado:    ")
altura = input("Digite a altura do quadrado:    ")

area = int(base) * int(altura)

print("A area do quadrado é {} e o dobro é {}".format(area, (area * 2)))