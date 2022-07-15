print('=-=' * 20)
print(' ' * 25 + 'PROJETOS:')
print('=-=' * 20)
print('''
[1] Adivinhação
''')
escolha = int(input('Qual projeto deseja abrir: '))
print('=-=' * 20)

if ( escolha == 1 ):
    import jogodavelha
if ( escolha == 2 ):
    import jogodaforca


