'''
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

    Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
        tipoCombustivel.
        valorLitro
        quantidadeCombustivel 
    Possua no mínimo esses métodos:
        abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
        abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
        alterarValor( ) – altera o valor do litro do combustível.
        alterarCombustivel( ) – altera o tipo do combustível.
        alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba. 
    OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba. 
'''

print("**********************************")
print('**CLASSE*BOMBA*DE*COMBUSTÍVEL**!**')
print("**********************************")


class BombaCombustivel():
    
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.setTipoCombustivel(tipoCombustivel)
        self.setValorLitro(valorLitro)
        self.setQuantidadeCombustivel(quantidadeCombustivel)
        print(f'\
| Tipo Combustivel: {self.tipoCombustivel} \
| Valor Litro: {self.valorLitro} \
| Quantidade Combustivel: {self.quantidadeCombustivel} |')

    def setTipoCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel
        return self.tipoCombustivel

    def setValorLitro(self, valorLitro):
        self.valorLitro = float(valorLitro)
        return self.valorLitro

    def setQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel
        return self.quantidadeCombustivel

    def abastecerPorValor(self, valor):
        totalLitros = valor / self.valorLitro
        if (totalLitros <= self.quantidadeCombustivel):
            self.setQuantidadeCombustivel(self.quantidadeCombustivel - totalLitros)
        return totalLitros

    def abastecerPorLitro(self, totalLitros):
        if (totalLitros <= self.quantidadeCombustivel):
            self.setQuantidadeCombustivel(
                self.quantidadeCombustivel - totalLitros)
        return totalLitros

GA = BombaCombustivel('Gasolina Aditivada', 3.03, 10000)
print()
print(f'Abastecendo (Litro): {GA.abastecerPorLitro(1000)} L')
print(f'Quantidade Bomba de Combustivel: \t {GA.quantidadeCombustivel}')
print(f'Abastecendo (Valor): {GA.abastecerPorValor(10000):.2f} L')
print(f'Quantidade Bomba de Combustivel: \t {GA.quantidadeCombustivel:.2f}')