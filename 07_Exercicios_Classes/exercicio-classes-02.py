'''
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''

print("**********************************")
print('******CLASSE***QUADRADO***!*******')
print("**********************************")

class Quadrado():
    def __init__(self,lado):
        self.lado = lado
                
    def MudarLado(self,lado):
        self.lado = lado
        return self.lado
        
    def RetornarLado(self):
        return self.lado
    
    def CalcularArea(self):
        area = self.lado ** 2
        return area
    
    
quadradinho = Quadrado(50)
print('Lado:\t', quadradinho.RetornarLado())
print('Mudando Lado:\t', quadradinho.MudarLado(60))
print('Lado:\t', quadradinho.RetornarLado())
print('Area:\t' , quadradinho.CalcularArea())