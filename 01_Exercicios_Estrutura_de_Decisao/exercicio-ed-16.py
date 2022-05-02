'''
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
    a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, 
    sendo encerrado;
    b. Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
'''

print("****************************************")
print("*******EQUAÇÃO**DE**SEGUNDO**GRAU*******")
print("****************************************")

a = int(input("DIGITE O VALOR DE A:   "))
b = int(input("DIGITE O VALOR DE B:   "))
c = int(input("DIGITE O VALOR DE C:   "))

delta = ((b ** 2) - (4 * a * c))

# if delta  0:
#     print("O Delta é negativo ou igual a zero !")
# else:
x1 = (-b + delta ** (1 / 2)) / (2 * a)
x2 = (-b - delta ** (1 / 2)) / (2 * a)   
print(f'O valor de bhaskara dá x² = {x1} e x² = {x2} , e delta dá {delta}')
    
    
