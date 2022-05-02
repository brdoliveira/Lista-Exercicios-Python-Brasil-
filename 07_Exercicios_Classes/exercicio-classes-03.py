'''
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local
'''

print("**********************************")
print('*****CLASSE***RETANGULO***!*******')
print("**********************************")

class Retangulo():
    def __init__(self,LadoA,LadoB):
        self.LadoA = LadoA
        self.LadoB = LadoB
        
    def MudarValorLados(self,LadoA,LadoB):
        self.LadoA = LadoA
        self.LadoB = LadoB
        return self.LadoA , self.LadoB
        
    def RetornarValorLados(self):
        return self.LadoA , self.LadoB 
    
    def CalcularArea(self):
        area = self.LadoA * self.LadoB
        return area
    def CalcularPerimetro(self):
        perimetro = (self.LadoA * 2) + (self.LadoB * 2)
        return perimetro
    
Rentagulo = Retangulo(5,10)
print(f'Area: {Rentagulo.CalcularArea()}')
print(f'Mudar valor: {Rentagulo.MudarValorLados(3,10)}')
print(f'Area: {Rentagulo.CalcularArea()}')
print(f'Perimetro: {Rentagulo.CalcularPerimetro()}')