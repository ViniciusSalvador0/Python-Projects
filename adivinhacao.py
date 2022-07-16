import random

def imprimir_menu():
    print('=-=' * 10)
    print('   ◆ JOGO DA ADIVINHAÇÃO ◆')
    print('=-=' * 10)
    print('DIFICULDADE')
    print('','[1] Fácil','[2] Médio','[3] Difícil','', sep='\n')

def escolher_dificuldade(msg):

    dificuldade = input(msg)
    dificuldade = validar_dificuldade(dificuldade)

    match dificuldade:
        case '1':
            tentativas = 20
        case '2':
            tentativas = 10
        case '3':
            tentativas = 5
    return tentativas

def validar_dificuldade(dificuldade):

    while dificuldade not in '123':
        dificuldade = input('> Dificuldade inválida, tente novamente: ')
    return dificuldade

def imprimir_dica(chute, numero_secreto):

    if numero_secreto > chute:
        print('◆ Dica: O Número que estou pensando é MAIOR que o chute')
    else:
        print('◆ Dica: O Número que estou pensando é MENOR que o chute')
    print('=-=' * 10)

def verificar_status(status):
    if status == False:
        print('| Suas chances acabaram, Você Perdeu!')
    else:
        print('| Você venceu o Jogo!')

def imprimir_pontuacao(pontuacao_atual, pontos_perdidos):
    pontuacao_atual -= pontos_perdidos
    print(f'| Pontuação atual: {pontuacao_atual}')
    return pontuacao_atual

def imprimir_final():
    print('=-=' * 10)
    enter = input('Pressione ENTER Para sair')
    print('=-=' * 10)

def jogar():

    # Variaveis
    pontuacao_atual = 1000
    pontos_perdidos = 0

    numero_limite = 100
    numero_secreto = random.randrange(0, numero_limite)

    status = False

    imprimir_menu()

    tentativas = escolher_dificuldade('> Escolha a dificuldade do Jogo: ')
    print('=-=' * 10)

    for tentativa_atual in range(0,tentativas):

        chute = int(input('> Qual número estou pensando: '))
        pontos_perdidos += abs(numero_secreto - chute)
        if (chute == numero_secreto):
            print('| Resultado: Você acertou o número {} na {}º tentativa!'.format(numero_secreto, tentativa_atual))
            status = True
            break
        else:
            print('| Resultado: Você errou!')
            imprimir_dica(chute, numero_secreto)
    verificar_status(status)
    pontuacao_atual = imprimir_pontuacao(pontuacao_atual, pontos_perdidos)

    imprimir_final()