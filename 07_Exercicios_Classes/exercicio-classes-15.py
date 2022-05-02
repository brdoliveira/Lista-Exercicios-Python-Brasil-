'''
Classe Bichinho Virtual++: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao 
bichinho e por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.
'''

print("**********************************")
print('***CLASSE**BICHINHO**VIRTUAL**!***')
print("**********************************")

class BichinhoVirtual():
    def __init__(self, nome, fome, saude, idade):
        self.setNome(nome)
        self.setFome(fome)
        self.setSaude(saude)
        self.setIdade(idade)
        print(f'Nome: {self.nome} | Fome: {self.fome} | Saude: {self.saude} | Idade: {self.idade} | Humor: {self.getHumor()}')  

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setFome(self, fome):
        self.fome = fome

    def getFome(self):
        return self.fome

    def setSaude(self, saude):
        self.saude = saude

    def getSaude(self):
        return self.saude

    def setIdade(self, idade):
        self.idade = idade

    def getIdade(self):
        return self.idade

    def alimenta(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.fome -= self.fome * (quantidade / 100.0)

    def brincar(self, quantidade):
        if (quantidade >= 0) and (quantidade <= 100):
            self.saude += self.saude * (quantidade / 100.0)

    def getHumor(self):
        return self.getFome() * self.getSaude()

bicho = BichinhoVirtual('Cleber Coelho', 10, 10, 10)
print(f'Humor: {bicho.getHumor()}')
bicho.alimenta(30)
print(f'Humor: {bicho.getHumor()}')
bicho.brincar(20)
print(f'Humor: {bicho.getHumor()}')