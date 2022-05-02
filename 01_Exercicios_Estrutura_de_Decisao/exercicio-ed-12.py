'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês. 
Desconto do IR:
- Salário Bruto até 900 (inclusive) - isento
- Salário Bruto até 1500 (inclusive) - desconto de 5%
- Salário Bruto até 2500 (inclusive) - desconto de 10%
- Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

'''

print("**********************************")
print("*******FOLHA**DE**PAGAMENTO*******")
print("**********************************")


horas_trabalhadas = float(input("Quantas horas você trabalha por dia?   "))
salario_por_hora = float(input("Qual é o seu salário por hora?   "))

salario_bruto = horas_trabalhadas * salario_por_hora
ir = 0 
inss = 0
fgts = 0 
descontos = 0
salario_liquido = 0

if salario_bruto < 900:
    ir = salario_bruto * 0 
elif salario_bruto >= 900 and salario_bruto < 1500:
    ir = salario_bruto * 0.05
elif salario_bruto >= 1500 and salario_bruto < 2500:
    ir = salario_bruto * 0.1
else:
    ir = salario_bruto * 0.2
    
    
inss = salario_bruto * 0.1
fgts = salario_bruto  * 0.11    
descontos = inss + fgts + ir
salario_liquido = salario_bruto - descontos

print(f'Salário Bruto: ({horas_trabalhadas} * R${salario_por_hora})        : R$ {salario_bruto}')
print(f'(-) IR (5%)                     : R$ {ir}')      
print(f'(-) INSS ( 10%)                 : R$ {inss}')
print(f'FGTS (11%)                      : R$ {fgts}')
print(f'Total de descontos              : R$ {descontos}')
print(f'Salário Liquido                 : R$ {salario_liquido}')