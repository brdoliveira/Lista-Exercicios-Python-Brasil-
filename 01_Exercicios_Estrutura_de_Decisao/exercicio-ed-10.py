'''
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

print("**************************************************")
print("**INSIRA*VESPERTINO*(V)*MATUTINO*(M)*NOTURNO*(N)**")
print("**************************************************")

letra_inserida = input("DIGITE A LETRA ESCOLHIDA:  ")
letra_inserida = letra_inserida.upper()

if letra_inserida == "M":
    print("BOM DIA !")
elif letra_inserida == "V":
    print("BOA TARDE !")
elif letra_inserida == "N":
    print("BOA NOITE !")
else:
    print("VALOR NÃO IDENTIFICADO!")