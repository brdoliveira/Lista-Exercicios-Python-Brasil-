'''
Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';
'''

print('***********************************')
print('************Validações**!**********')
print('***********************************')

nome = ''
idade = 1000
salario = 0 
sexo = ''
estado_civil = 'A'

# Verificação nome
while (len(nome) < 3):
    nome = input('Digite um nome com mais de 3 letras:   ')
    if len(nome) < 3:
        print('Digite um nome maior !')
        
        
# Verificação idade
while (idade < 0) or (idade > 150):
    idade = int(input('Digite uma idade valida:   '))
    if (idade < 0) or (idade > 150):
        print('A idade ainda não está correta !')
        
# Verificação salario
while salario <= 0:
    salario = int(input('Digite o seu salario:   '))
    if salario <= 0:
        print(' Salário inválido !')
        
# Verificacao sexo
while (sexo != 'F') and (sexo != 'M'):
    sexo = input('Informe o sexo: ').upper()
    if (sexo != 'F') and (sexo != 'M'):
        print('O sexo deve ser infomado como M (masculino) ou F (feminino)')
        
# Verificacao estado civil
while ('SCVD'.find(estado_civil) < 0 ):
    estado_civil = input('Informe o estado civil:   ').upper()
    if ('SCVD'.find(estado_civil) < 0 ):
        print('Estado civil deve ser informado como: \n\
             S (solteiro) \n\
             C (casado) \n\
             V (viuvo)\n\
             D (divorciado)')
        
print('Todas as informações estão corretas !!!')