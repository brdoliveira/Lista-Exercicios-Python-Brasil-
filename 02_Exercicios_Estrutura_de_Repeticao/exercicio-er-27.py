'''
Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
'''

print('*************************************')
print('****Quantidade***de***turmas***!*****')
print('*************************************')


quantidade = 0
while (quantidade <= 0):
    quantidade = int(input('Informe a quantidade de turmas: '))
    if (quantidade <= 0):
        print('A quantidade deve ser positiva!')

soma = 0
for i in range(0, quantidade):
    alunos = -1
    while (alunos < 0) or (alunos > 40):
        alunos = int(input('Informe a quantidade de alunos da turma: '))
        if (alunos < 0) or (alunos > 40):
            print('A turma deve ter ate 40 alunos')
    soma += alunos

media = soma / float(quantidade)

print('Media de alunos por turma é:', media)