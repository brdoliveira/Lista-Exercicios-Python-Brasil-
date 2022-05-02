'''
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto 
você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de 
dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e
valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
'''

print('***********************************************')
print('*******Altura****Média****e****Peso****!*******')
print('***********************************************')


codigo = -1
total_clientes = 0
soma_alturas = 0.0
soma_pesos = 0.0

lista_codigo = []
lista_altura = []
lista_peso = []

while (codigo != 0):
    codigo = int(input('Informe o codigo do cliente: '))
    if (codigo != 0):
        altura = float(input('Informe a altura do cliente: '))
        peso = float(input('Informe o peso do cliente:'))
        lista_codigo.append(codigo)
        lista_altura.append(altura)
        lista_peso.append(peso)
        
maior_altura = max(lista_altura)
codigo_maior_altura = lista_codigo[lista_altura.index(maior_altura)]

menor_altura = min(lista_altura)
codigo_menor_altura = lista_codigo[lista_altura.index(menor_altura)]

maior_peso = max(lista_peso)
codigo_maior_peso = lista_codigo[lista_peso.index(maior_peso)]


menor_peso = min(lista_peso)
codigo_menor_peso = lista_codigo[lista_peso.index(menor_peso)]

media_altura = sum(lista_altura) / len(lista_altura)
media_peso = sum(lista_peso) / len(lista_peso)
        
print(f'Maior altura {maior_altura} o codigo dele é {codigo_maior_altura}')
print(f'Menor altura {menor_altura} o codigo dele é {codigo_menor_altura} \n \n')
print(f'Maior peso {maior_peso} o codigo dele é {codigo_maior_peso}')
print(f'Menor peso {menor_peso} o codigo dele é {codigo_menor_peso} \n \n')
print (f'Media da altura dos clientes: {media_altura}')
print (f'Media dos pesos dos clientes: {media_peso}')