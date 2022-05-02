'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
a. A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
b. A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
c. A mensagem "Aprovado com Distinção", se a média for igual a 10.
'''


print("****************************************")
print("**********LEITURA***DE***NOTAS**********")
print("****************************************")

primeira_nota = float(input("PRIMEIRA NOTA:   ")) 
segunda_nota = float(input("SEGUNDA NOTA:   ")) 
terceira_nota = float(input("TERCEIRA NOTA:   "))

media = (primeira_nota + segunda_nota + terceira_nota) // 3
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