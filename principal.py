import adivinhacao
from jogodaforca import forca

print('=-=' * 10)
print('PROJETOS:')
print('=-=' * 10)
print('''
[1] Jogo da Adivinhação
[2] Jogo da Forca
''')
escolha = int(input('Qual projeto deseja abrir: '))

if ( escolha == 1):
    adivinhacao.jogar()

if ( escolha == 2 ):
    forca.jogar()


