'''
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''

print("**********************************")
print("*******Dias****da****Semana*******")
print("**********************************")

semana = ['Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sabado']

numero_inserido = int(input("DIGITE O NUMERO ESCOLHIDO (1 a 7):  "))

if numero_inserido >= 1 and numero_inserido <= 7:
    dia_semana = semana[numero_inserido - 1]
    print(f'Numero escolhido foi {numero_inserido} e o dia da semana é : {dia_semana}')
else:
    print(f'Numero Invalido! O numero digitado foi {numero_inserido}')