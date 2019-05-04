PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')

textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]


for frase in textos:
    found = False
    for palavra in frase.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('O texto possui pelo menos uma palavra proibida:', palavra)
            found = True
            break
    if not found:
        print('Texto autorizado:', frase)
