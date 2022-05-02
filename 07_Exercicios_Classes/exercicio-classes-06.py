'''
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. 
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
'''

print("**********************************")
print('*********CLASSE***TV***!**********')
print("**********************************")

class TV():
    def __init__(self,canal,volume):
        self.canal = canal
        self.volume = volume
        print(f'Canal: {self.canal} | Volume: {self.volume}')
        
    def AumentarVolume(self):
        self.volume += 1
        return self.VerificacaoVolume()
        
    def DiminuirVolume(self):
        self.volume -= 1
        return self.VerificacaoVolume()
        
        
    def VerificacaoVolume(self):
        if self.volume > 0 and self.volume < 20:
            return self.volume
        elif self.volume <= 0:
            print('O volume está no mínimo !')
            return self.volume
        elif self. volume >= 20:
            print('O volume está no máximo !')
            return self.volume
        else:
            print('Algum erro apresentado !')
            return self.volume
        
    def VerificacaoCanal(self):
        if self.canal > 1 and self.canal < 200:
            return self.volume
        elif self.canal == 0 :
            self.canal = 200
        elif self.canal == 201:
            self.canal = 0
            
canal = TV(199,10)
print(f'Volume (Aumentar): {canal.AumentarVolume()}')
print(f'Volume (Aumentar): {canal.AumentarVolume()}')
print(f'Volume (Diminuir): {canal.DiminuirVolume()}')
print(f'Volume (Diminuir): {canal.DiminuirVolume()}')
print(f'Volume (Diminuir): {canal.DiminuirVolume()}')