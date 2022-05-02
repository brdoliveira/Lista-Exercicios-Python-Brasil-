'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e 
voltando a pedir as informações.
'''

print('***********************************')
print('******USUARIO*****E*****SENHA******')
print('***********************************')

nome_usuario = ''
senha = ''

while (nome_usuario == senha):
    nome_usuario = input('Digite um nome de usuário:   ')
    senha = input('Digite uma senha:   ')
    if (nome_usuario == senha):
        print('Os valores inseridos são iguais !')