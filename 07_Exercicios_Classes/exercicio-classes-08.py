'''
Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos comer(), verBucho() 
e Digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes
e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal? 
'''

print("**********************************")
print('*******CLASSE***MACACO***!********')
print("**********************************")

class Macaco:
    
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)
        print(f'{self.nome} comeu {comida}')

    def verBucho(self):
        print(f'Estômago do {self.nome} - {self.bucho}')

    def digerir(self):
        if (len(self.bucho) > 0):
            print(f'{self.nome} digeriu {self.bucho[-1]}')
            self.bucho.pop(0)


macaco1 = Macaco('Macaquinho Bariloche')
macaco2 = Macaco('Macaco do Latino')

macaco1.comer('Uva')
macaco1.verBucho()
macaco1.comer('Morango')
macaco1.verBucho()
macaco1.comer('Galinha')
macaco2.comer('Maca')
macaco1.verBucho()
macaco1.digerir()
macaco1.verBucho()
macaco2.comer('Formiga')
macaco2.comer('Limão')
macaco2.comer(macaco1)
macaco2.verBucho()