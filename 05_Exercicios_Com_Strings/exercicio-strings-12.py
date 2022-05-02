'''
Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7
dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133
'''

print("*********************************")
print("**VALIDA**E**CORRIGE**TELEFONE!**")
print("*********************************")

def corrige_telefone(telefone):
    telefone_limpo = telefone.replace('-','')
    if(len(telefone_limpo) >= 4) and (len(telefone_limpo) <= 8):
        if (len(telefone_limpo) != 8):
            print(f'Telefone possui {len(telefone_limpo)} digitos. Vou acrescentar o digito {8 - len(telefone_limpo)} na frente.')
            
            primeira_parte = telefone_limpo
            segunda_parte = telefone_limpo[:(8 - (len(telefone_limpo)))]
            terceira_parte = segunda_parte + primeira_parte
            telefone_corrigido = terceira_parte[:4] + '-' + terceira_parte[4:]
            
            print(f'Telefone corrigo sem formatação: {telefone}')
            print(f'Telefone corrigo com formatação: {telefone_corrigido}')
        else:
            print(f'Telefone: {telefone}')
            print('O numero de telefone está correto!')
    else: 
        print('Numero não está dentro dos padrões!')
        
telefone = corrige_telefone(input('Digite um numero de telefone:   '))