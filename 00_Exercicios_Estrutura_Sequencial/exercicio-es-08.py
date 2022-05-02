'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês
'''

print("**********************************")
print("**CALCULAR*O*SALÁRIO*DO*INDÍVIDUO*")
print("**********************************")

horas_trabalhadas = int(input("Quantas horas você trabalha por dia?   "))
salario_por_hora = int(input("Qual é o seu salário po hora?   "))

salario = (horas_trabalhadas * 22) * salario_por_hora

print(" Você trabalha {} por dia, e recebe R${} por hora, dando {} por mês".format(horas_trabalhadas,salario_por_hora,salario))