PALAVRAS_PROIBIDAS = {'futebol', 'religião', 'política'}  # Conjunto

textos = [
    'João gosta de futebol e política',
    'A praia foi divertida',
]

for frase in textos:
    # Tranforma a frase em um conjunto de palavras
    palavras_na_frase = set(frase.lower().split())
    # nterseção entre os conjuntos de plavras
    intersecao = PALAVRAS_PROIBIDAS.intersection(palavras_na_frase)
    if intersecao:
        print('O texto possui pelo menos uma palavra proibida:', intersecao)
    else:
        print('Texto autorizado:', frase)
