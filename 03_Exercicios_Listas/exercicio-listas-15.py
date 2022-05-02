'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for 
informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
    - Mostre a quantidade de valores que foram lidos;
    - Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    - Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    - Calcule e mostre a soma dos valores;
    - Calcule e mostre a média dos valores;
    - Calcule e mostre a quantidade de valores acima da média calculada;
    - Calcule e mostre a quantidade de valores abaixo de sete;
    - Encerre o programa com uma mensagem;
'''

print("**********************************")
print("**********CALCULOS****!***********")
print("**********************************")

valores = []
valor = 0

while (valor != -1):
    valor = int(input('Informe um valor:   '))
    if (valor != -1):
        valores.append(valor)

print(f'Quantidade de valores lidos: {len(valores)}')
print(valores)
valores.reverse()
print(valores)

media = sum(valores) / float(len(valores))

print(f'Soma dos Valores: {sum(valores)}')
print(f'Media dos Valores: {media:.2f}')

valores_acima_media = 0
valores_acima_de_sete = 0
for valor in valores:
    if (valor >= media):
        valores_acima_media += 1
    if (valor >= 7):
        valores_acima_de_sete += 1

print(f'Valores acima da media: {valores_acima_media}')
print(f'Valores acima de sete: {valores_acima_de_sete}')