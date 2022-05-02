'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, 
B ou C ou “REPROVADO” se o conceito for D ou E.
'''

print("****************************************")
print("**********LEITURA***DE***NOTAS**********")
print("****************************************")

primeira_nota = float(input("PRIMEIRA NOTA:   ")) 
segunda_nota = float(input("SEGUNDA NOTA:   ")) 

media = (primeira_nota + segunda_nota) // 2
conceito = 'A'

if media > 9 and media <= 10:
    print(f'Você foi APROVADO , e o seu conceito foi {conceito}')
elif media > 7.5 and media <= 9:
    print(f'Você foi APROVADO , e o seu conceito foi {conceito}')
elif media > 6 and media <= 7.5:
    conceito = 'C'
    print(f'Você foi APROVADO , e o seu conceito foi {conceito}')
elif media > 4 and media <= 6:
    conceito = 'D'
    print(f'Você foi REPROVADO , e o seu conceito foi {conceito}')
elif media <= 4:
    conceito = 'E'
    print(f'Você foi REPROVADO , e o seu conceito foi {conceito}')
else:
    print("Algum erro nas notas inseridas !")