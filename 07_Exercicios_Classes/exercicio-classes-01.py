'''
Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
'''

print("**********************************")
print('********CLASSE***BOLA***!*********')
print("**********************************")

class Bola():
    def __init__(self,cor,circunferencia,material):
        self.cor = cor
        self.circuferencia = circunferencia
        self.material = material
    
    def trocaCor(self,cor):
        self.cor = cor
    
    def mostraCor(self):
        return self.cor
    

bolita = Bola('Vermelho',5,'Bronze')
print(bolita.mostraCor())       
bolita.trocaCor('Verde')
print(bolita.mostraCor())       