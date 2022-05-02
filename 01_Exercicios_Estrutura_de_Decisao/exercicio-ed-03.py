'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

print("****************************************")
print("**INSIRA*FEMININO*(F)*OU*MASCULINO*(M)**")
print("****************************************")

letra_inserida = input("DIGITE A LETRA ESCOLHIDA:  ")
letra_inserida = letra_inserida.upper()

if letra_inserida == "F":
    print("LETRA ESCOLHIDA FOI F, DE FEMININO!")
elif letra_inserida == "M":
    print("LETRA ESCOLHIDA FOI M, DE MASCULINO!")
else:
    print("SEXO NÃO IDENTIFICADO!")