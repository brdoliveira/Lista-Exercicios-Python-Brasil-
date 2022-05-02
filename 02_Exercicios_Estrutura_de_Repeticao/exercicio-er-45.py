'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta
de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por
resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema.
Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:
01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos
alunos usarem o programa.
'''
print('*************************************')
print('****GABARITO****DA****PROVA****!*****')
print('*************************************')


continua = 'S'
total_acertos = 0
somaAcertos = 0
lista_acertos = []

while (continua.upper() == 'S'):
    acertos = 0
    print('Informe a resposta de cada questao:')
    resposta = input('Questao 1: ').upper()
    if (resposta == 'A'):
        acertos += 1
    resposta = input('Questao 2: ').upper()
    if (resposta == 'B'):
        acertos += 1
    resposta = input('Questao 3: ').upper()
    if (resposta == 'C'):
        acertos += 1
    resposta = input('Questao 4: ').upper()
    if (resposta == 'D'):
        acertos += 1
    resposta = input('Questao 5: ').upper()
    if (resposta == 'E'):
        acertos += 1
    resposta = input('Questao 6: ').upper()
    if (resposta == 'E'):
        acertos += 1
    resposta = input('Questao 7: ').upper()
    if (resposta == 'D'):
        acertos += 1
    resposta = input('Questao 8: ').upper()
    if (resposta == 'C'):
        acertos += 1
    resposta = input('Questao 9: ').upper()
    if (resposta == 'B'):
        acertos += 1
    resposta = input('Questao 10: ').upper()
    if (resposta == 'A'):
        acertos += 1

    lista_acertos.append(acertos)
    print('Total de Acertos: %d' % acertos)

    total_acertos += 1

    continua = input('Deseja continuar (S/N): ').upper()

print(f'Maior acerto: {max(lista_acertos)}')
print(f'Menor acerto: {min(lista_acertos)}')
print(f'Total de alunos que utilizaram o sistema: {total_acertos}')
print('Media de acertos: {:.2f}'.format(somaAcertos / float(total_acertos)))