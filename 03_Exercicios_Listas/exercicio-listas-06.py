'''
Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o numero de aluno
com média maior ou igual a 7.0
'''

lista_media_alunos = []

print("**********************************")
print("******MEDIA**DOS**ALUNOS**!*******")
print("**********************************")

for i in range(10):
    media = 0
    print(f'{i + 1}º Aluno !')
    for n in range(4):
        nota = float(input(f'Digite a {n + 1}º nota:  '))
        media += nota
    media = media / 4
    lista_media_alunos.append(media)
    

for m in range(10):
    media_aluno = lista_media_alunos[m]
    if media_aluno >= 7:
        print(f'O {m + 1}º aluno teve a nota {media_aluno:.2f}')