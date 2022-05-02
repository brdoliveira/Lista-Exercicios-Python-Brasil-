'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa 
que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no 
salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento.
'''

print("**********************************")
print("*****ORGANIZAÇÃO*****TABAJARA*****")
print("**********************************")

salario = float(input("DIGITE O SALÁRIO:  "))
porcentagem = 0
aumento = 0
novo_salario = 0

if salario < 280:
    porcentagem = 20
    aumento =  salario * 0.2
    novo_salario = salario + aumento
elif salario >= 280 and salario < 700:
    porcentagem = 15
    aumento =  salario * 0.15
    novo_salario = salario + aumento
elif salario >= 700 and salario < 1500:
    porcentagem = 10
    aumento =  salario * 0.1
    novo_salario = salario + aumento
else:
    porcentagem = 5
    aumento =  salario * 0.05
    novo_salario = salario + aumento
    
print(f'O salário antes do reajuste: {salario}, o porcentual do aumento foi de {porcentagem}% , valor do aumento em reais foi de R$ {aumento}, resultando {novo_salario} ')