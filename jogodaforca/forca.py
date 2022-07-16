#Imports
import random
from pathlib import Path

#Variaveis
palavras = []
nome_arquivo = ''
nome_jogo = './jogodaforca'

def get_lines(nome_arquivo: str, path=nome_jogo):
    arquivo = Path(path).joinpath(nome_arquivo)
    if not arquivo.is_file():
        raise ValueError(f'Arquivo {arquivo} não existe')

    with open(arquivo, "r", encoding="utf-8") as fp:
        return [line.strip('\n') for line in fp.readlines()]

def TelaInicial():
    print('=-=' * 10)
    print(' BEM VINDO AO JOGO DA FORCA')
    print('=-=' * 10)

def ValidaTema(tema):
    while tema not in '123':
        tema = input('Informe um tema válido: ')

    match tema:
        case '1':
            nome_arquivo = 'animais.txt'
        case '2':
            nome_arquivo = 'frutas.txt'
        case '2':
            nome_arquivo = 'objetos.txt'

    palavras = get_lines(nome_arquivo)

def EscolhaTema():
    print('Temas Disponiveis: ')
    print('[1] Animais')
    print('[2] Frutas')
    print('[3] Objetos')
    tema = input('Escolha um tema: ')
    ValidaTema(tema)

def jogar():
    TelaInicial()
    EscolhaTema()