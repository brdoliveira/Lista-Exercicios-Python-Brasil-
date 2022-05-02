'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a. o produto do dobro do primeiro com metade do segundo .
    b. a soma do triplo do primeiro com o terceiro.
    c. o terceiro elevado ao cubo.

'''

print("**********************************")
print("******INSIRA***TRÊS***NUMEROS*****")
print("**********************************")

numero_um = int(input("Insira o primeiro numero inteiro:   "))
numero_dois = int(input("Insira o segundo numero inteiro:   "))
numero_tres = float(input("Insira o primeiro numero real:   "))

primeiro_calculo = (numero_um * 2) * ( numero_dois / 2)
segundo_calculo = (numero_um * 3) + numero_tres
terceiro_calculo = numero_tres ** 3

print(f'O produto do dobro de {numero_um} com metade de {numero_dois} é {primeiro_calculo} , a soma do triplo de {numero_um} com o {numero_tres} é {segundo_calculo} , e {numero_tres} elevado ao cubo é {terceiro_calculo} !')