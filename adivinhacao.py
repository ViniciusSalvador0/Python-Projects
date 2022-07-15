#Imports
import random

#Variaveis
tentativas = 0
pontuacaoatual = 1000
pontos_perdidos = 0
dificuldade = ''
chute = 0

#Menu
print('JOGO DA ADIVINHAÇÃO!')
print('=-=' * 20)
print('''
Dificuldade

[1] Fácil
[2] Médio
[3] Dificil
''')

def ValidaDificuldade(msg):
    while True:
        dificuldade = input(msg)
        if (dificuldade == '1'):
            tentativas = 20
            break
        elif(dificuldade == '2'):
            tentativas = 10
            break
        elif(dificuldade == '3'):
            tentativas = 5
            break
        else:
            print('\033[0;31mEscolha uma dificuldade válida!\033[m')
    return tentativas

tentativas = ValidaDificuldade('Escolha a dificuldade do jogo: ')
print('=-=' * 20)
escolha_pc = random.randrange(0,100)

for i in range (1,tentativas + 1):
    chute = int(input('Tentativa {} de {}, qual número estou pensando: '.format(i, tentativas)))

    pontos_perdidos = pontos_perdidos + abs(escolha_pc - chute)
    if (chute == escolha_pc):
        print('Parabens! Você acertou!')
        pontuacaoatual = pontuacaoatual - pontos_perdidos
        print('Pontuação atual {}'.format(pontuacaoatual))
        break
    else:
        print('Você errou!')
        if(chute > escolha_pc):
            print('Dica: O valor que eu pensei é menor que seu chute!')
        else:
            print('Dica: O valor que eu pensei é maior que seu chute!')
print('=-=' * 20)
