#Imports
import random
from pathlib import Path

#Variaveis
nome_arquivo = ''


def perguntar_letra():
    letra = input('Digite a letra: ')
    return letra



def jogar():

    imprimir_menu()

    tema = escolher_tema()
    nome_arquivo = pegar_nome_arquivo(tema)
    palavra_secreta = pegar_palavra_secreta(nome_arquivo)

    letras_acertadas = ['_' for letras in palavra_secreta]

    erros = 0
    venceu = False
    perdeu = False
    print(palavra_secreta)
    print(type(palavra_secreta))
    while (not venceu and not perdeu):
        chute = input('Informe a letra: ')
        for letras in palavra_secreta:
            if chute == palavra_secreta[letras]:
                letras_acertadas[letras] == chute
            else:
                erros += 1
        perdeu = (erros == 6)



    print(palavra_secreta)
    print(letras_acertadas)

def pegar_linhas(nome_arquivo: str):
    path = './jogodaforca/palavras'
    arquivo = Path(path).joinpath(nome_arquivo)
    if not arquivo.is_file():
        raise ValueError(f'Arquivo {arquivo} não existe')

    with open(arquivo, "r", encoding="utf-8") as fp:
        return [line.strip('\n') for line in fp.readlines()]

def pegar_palavra_secreta(nome):
    palavras = pegar_linhas(nome)
    numero_palavra = random.randrange(0, len(palavras))
    return palavras[numero_palavra]

def pegar_nome_arquivo(tema):
    match tema:
        case '1':
            nome_arquivo = 'animais.txt'
        case '2':
            nome_arquivo = 'frutas.txt'
        case '2':
            nome_arquivo = 'objetos.txt'
    return nome_arquivo

def imprimir_temas():
    print('TEMAS DISPONIVEIS ')
    print('','[1] Animais','[2] Frutas','[3] Objetos', '', sep='\n')

def escolher_tema():
    imprimir_temas()
    tema = input('Escolha um dos temas: ')
    while tema not in '123':
        tema = input('Informe um tema válido: ')
    return tema

def imprimir_menu():
    print('=-=' * 10)
    print('      ◆ JOGO DA FORCA ◆')
    print('=-=' * 10)

if __name__ == '__main__':
    jogar()
    a = input('digite uma letra')


