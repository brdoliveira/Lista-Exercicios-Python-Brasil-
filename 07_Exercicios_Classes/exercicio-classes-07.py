'''
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade 

Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os 
atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela 
pode ser calculada a qualquer momento.
'''

print("**********************************")
print('***CLASSE**BICHINHO**VIRTUAL**!***')
print("**********************************")

class BichinhoVirtual():
    def __init__(self,nome):
        self.nome = nome
        self.fome = 10
        self.saude = 100
        self.idade = 1
        self.humor = 100
        print(f'Nome: {self.nome} | Fome: {self.fome} | Saude: {self.saude} | Idade: {self.idade} | Humor: {self.humor}')  
        
    def AlterarNome(self,nome):
        self.nome = nome
        return nome
    
    def Fome(self):
        if self.fome == 0:
            print('Morrendo de fome !')
            self.humor -= 50
        elif self.fome >= 1 and self.fome <= 4:
            print('Estou com fome !')
            self.humor -= 25 
        elif self.fome >= 5 and self.fome <= 7:
            self.humor -= 0
            print('Normal !')
        elif self.fome >= 5  and self.fome <= 7:
            self.humor += 25
            print('Satisfeito !')
        elif self.fome == 10:
            self.humor += 50
            print('Estou cheio !')
        if self.fome > 100:
            self.fome = 100
        self.Humor()
        return self.humor
            
    def Saude(self):
        if self.saude == 0:
            print('Morrendo !')
            self.humor -= 50
            
        elif self.saude >= 1 and self.saude <= 50:
            print('Estou morrendo !')
            self.humor -= 25
            
        elif self.saude >= 51 and self.saude <= 70:
            print('Estou com a saúde Razoável !')
            self.humor += 0
            
        elif self.saude >= 51 and self.saude <= 70:
            self.humor += 25
            
            print('Estou saudável!')
        elif self.saude == 100:
            self.humor += 50
            print('Estou muito saudável !')
            
        if self.saude > 100:
            self.saude = 100
            
        self.Humor()
        return self.saude
            
    def Idade(self):
        self.idade += 1
        return self.idade
    
    def Humor(self):
        if self.humor > 100:
            self.humor = 100
             
        if self.humor == 0:
            print('Morri !')
            
        elif self.humor >= 1 and self.humor <= 25:
            print('Estou morrendo !')
            
        elif self.humor >= 26 and self.humor <= 50:
            print('Não estou bem !')
            
        elif self.humor >= 51 and self.humor <= 75:
            print('Estou normal !')
            
        elif self.humor >= 76 and self.humor <= 99:
            print('Estou bem !')

        elif self.humor == 100:
            print('Estou muito bem !')
        return self.humor
    
tamatam = BichinhoVirtual('Tamagoshi')
print('Idade (Aumentou): {}'.format(tamatam.Idade()))
print('Idade (Aumentou): {}'.format(tamatam.Idade()))
print('Fome: {}'.format(tamatam.Fome()))
print('Saude: {}'.format(tamatam.Saude()))
print('Humor: {}'.format(tamatam.Humor()))