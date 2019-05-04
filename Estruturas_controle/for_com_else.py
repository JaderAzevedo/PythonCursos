PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')

textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for frase in textos:
    for palavra in frase.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('O texto possui pelo menos uma palavra proibida:', palavra)
            break
    else:
        print('Texto autorizado:', frase)
