'''
Leet spek generator. Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. 
A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de 
computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. 
Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak.
'''

print("*********************************")
print("***LEET***SPEK***GENERATOR***!***")
print("*********************************")


letras = (' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
leet = ('  ','4', '8', '<', '[)', '3', 'I=', '6', '#', '1', 'j', '|<', '|_', '|\/|', '/\/', '0', 'I^', '9', 'l2', '5', '7',
        'v', 'V', 'vv', '><', '`/', '2')


frase = str(input('Digite alguma frase:   ')).upper()

for i in range(25):
    frase = frase.replace(letras[i],leet[i])
    
print(frase)
