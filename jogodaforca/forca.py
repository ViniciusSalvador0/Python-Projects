import random

def jogar():
    imprimir_menu()
    tema = escolher_tema()

    palavra_secreta = carregar_palavra(tema)
    letras_acertadas = ['_' for letra in palavra_secreta]

    erros = 0
    letra_chutes = ''

    ganhou = False
    perdeu = False

    while (not ganhou and not perdeu):
        imprimir_forca(erros)
        print(letras_acertadas)
        print(f'Palavras que já foram: {letra_chutes}')

        chute = validar_chute('Digite uma letra: ', letra_chutes)
        letra_chutes += chute

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        perdeu = erros == 6
        ganhou = '_' not in letras_acertadas

    if ganhou:
        print('Parabens, você venceu!')
    else:
        print('Puxa, você foi enforcado!')
        print(f'A palavra era {palavra_secreta}')

def validar_chute(msg, letra_chutes):
    chute = input(msg)
    while (not chute.isalpha()) or (chute in letra_chutes):
        chute = input('Chute invalido, tente novamente:')
    print('=-=' * 10)
    return chute

def carregar_palavra(tema):
    palavras = []
    nome_arquivo = pegar_arquivo(tema)
    arquivo = open(nome_arquivo, 'r', encoding="utf-8")

    for linha in arquivo:
        linha = linha.strip('\n')
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0,len(palavras))
    return palavras[numero].upper()

def pegar_arquivo(tema):
    if __name__ == '__main__':
        path = './palavras/'
    else:
        path = './jogodaforca/palavras/'

    match tema:
        case '1':
            nome_arquivo = (path + 'animais.txt')
        case '2':
            nome_arquivo = (path + 'frutas.txt')
        case '2':
            nome_arquivo = (path + 'objetos.txt')
    return nome_arquivo

def escolher_tema():
    imprimir_temas()
    tema = input('Escolha um dos temas: ')
    while tema not in '123':
        tema = input('Informe um tema válido: ')
    print('=-=' * 10)
    return tema

def imprimir_temas():
    print('TEMAS DISPONIVEIS ')
    print('','[1] Animais','[2] Frutas','[3] Objetos', '', sep='\n')

def imprimir_menu():
    print('=-=' * 10)
    print('      ◆ JOGO DA FORCA ◆')
    print('=-=' * 10)


def imprimir_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |       |    ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if (__name__ == "__main__"):
    jogar()
    a = input('a')