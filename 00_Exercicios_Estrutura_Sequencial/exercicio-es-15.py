'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

print("**********************************")
print("**CALCULAR*O*SALÁRIO*DO*INDÍVIDUO*")
print("**********************************")

horas_trabalhadas = int(input("Quantas horas você trabalha por dia?   "))
salario_por_hora = int(input("Qual é o seu salário por hora?   "))

salario_bruto = (horas_trabalhadas * 22) * salario_por_hora

desconto_IR = salario_bruto * 0.11
desconto_INSS = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - (desconto_IR + desconto_INSS + desconto_sindicato)

print(f'Seu salário bruto é R$ {salario_bruto} e o seu salário liquido (tirando os descontos) é de R$ {salario_liquido}')