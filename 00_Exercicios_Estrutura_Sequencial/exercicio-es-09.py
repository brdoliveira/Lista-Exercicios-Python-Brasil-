'''
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
'''


print("**********************************")
print("****CONVERSÃO**F°**PARA**C°**!****")
print("**********************************")

temperatura_f = float(input("Qual é a temperatura (em fahrenheit)?   "))

temperatura_c = 5 * ((temperatura_f - 32) / 9 )

print(" A temperatura inserida foi {} °F em Celsius é {:.1f} °C !".format(temperatura_f,temperatura_c))