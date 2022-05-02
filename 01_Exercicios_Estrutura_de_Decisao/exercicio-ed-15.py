'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes;
'''

print("****************************************")
print("**************TRIANGULO**!**************")
print("****************************************")

lado_um = int(input("INSIRA O PRIMEIRO LADO:   "))
lado_dois = int(input("INSIRA O SEGUNDO LADO:   "))
lado_tres = int(input("INSIRA O TERCEIRO LADO:   "))

primeira_verificacao = (lado_dois == lado_um)
segunda_verificacao = (lado_dois == lado_tres)
terceira_verificacao = (lado_um == lado_tres)

if lado_um == lado_dois == lado_tres:
    print("Todos os lados inseridos são iguais !")   
elif primeira_verificacao or segunda_verificacao or terceira_verificacao:
    print("Temos apenas dois lados iguais !")
elif lado_um != lado_dois != lado_tres:
    print("Não tem nenhum lado igual !")
else:
    print("Algum erro apresentado !")