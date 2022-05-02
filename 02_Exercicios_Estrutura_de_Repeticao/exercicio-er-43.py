'''
O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item 
(preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
''' 

print('***********************************************')
print('***Cardápio****de****uma****lanchonete****!****')
print('***********************************************')

lista_codigo = [100,101,102,103,104,105]
lista_preco = [1.2,1.3,1.5,1.2,1.3,1]
lista_produtos = []
codigo = 99

while codigo >= 99 and codigo <= 105:
    print('\n\
O cardápio de uma lanchonete é o seguinte: \n\
    Especificação   Código    Preço \n\
    Cachorro Quente  100     R$ 1,20 \n\
    Bauru Simples    101     R$ 1,30 \n\
    Bauru com ovo    102     R$ 1,50 \n\
    Hambúrguer       103     R$ 1,20 \n\
    Cheeseburguer    104     R$ 1,30 \n\
    Refrigerante     105     R$ 1,00 \n\
    PARA TERMINAR A COMPRA DIGITE ALGUM CODIGO QUE NÃO ESTA AQUI!')

    codigo_digitado = int(input('Digite o codigo do produto:   '))
    codigo = codigo_digitado
    
    if codigo >= 100 and codigo <= 105:
        quantidade_digitada = int(input('Digite o quantidade do produto:   '))

        preco = lista_preco[lista_codigo.index(codigo_digitado)]

        lista_produtos.append(preco * quantidade_digitada)
    else:
        print('Compra Finzalizada!')

print(f'O resultado foi de {sum(lista_produtos)} reais')
