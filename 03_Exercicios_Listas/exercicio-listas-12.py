'''
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem 
altura inferior à média de altura desses alunos.
'''

print("**********************************")
print("****MÉDIA****DE****ALTURA****!****")
print("**********************************")

aluno_idade = []
aluno_altura = []

for i in range(5):
    aluno_idade.append(int(input('Informe a idade do aluno:   ')))
    aluno_altura.append(float(input('Informe a altura do aluno:   ')))
    
media = sum(aluno_altura) / len(aluno_altura)
alunos_altos = 0

for i in range(5):
    if (aluno_idade[i] >= 13) and (aluno_altura[i] >= media):
        alunos_altos += 1
        
print(f'Existem {alunos_altos} alunos com mais de 13 anos acima de altura media')