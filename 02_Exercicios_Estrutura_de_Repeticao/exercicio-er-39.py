'''
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura 
em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com 
suas alturas.
'''

print('***********************************************')
print('*******Tamanho******dos******Aluno*****!*******')
print('***********************************************')

lista_codigo = []
lista_altura = []

for i in range(0,10):
    codigo = int(input(f'{i+1}° Código:   '))
    altura = int(input(f'{i+1}° Altura:   '))
    
    lista_codigo.append(codigo)
    lista_altura.append(altura)
    

maior_altura = max(lista_altura)
codigo_maior_altura = lista_codigo[lista_altura.index(maior_altura)]

menor_altura = min(lista_altura)
codigo_menor_altura =  lista_codigo[lista_altura.index(menor_altura)]

print(f'Menor altura é {menor_altura} e {codigo_menor_altura} \n\
Maior altura é {maior_altura} e {codigo_maior_altura}')