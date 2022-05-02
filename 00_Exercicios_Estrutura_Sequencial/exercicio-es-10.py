'''
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
'''

print("**********************************")
print("****CONVERSÃO**C°**PARA**F°**!****")
print("**********************************")

temperatura_c = float(input("Qual é a temperatura (em celsius)?   "))

temperatura_f = (temperatura_c * 9 / 5) + 32

print(" A temperatura inserida foi {} °C em Fahreinheit é {:.1f} °C !".format(temperatura_c,temperatura_f))
