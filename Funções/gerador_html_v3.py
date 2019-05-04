# classe e inline são  parametros opcionais
def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}"> {conteudo}</{tag}>'


def tag_lista(*itens):
    lista = ''.join(f'<li>{iten}</li'for iten in itens)  # Generator
    return f'<ul>{lista}</ul>'


print(tag_bloco('bloco'))
print(tag_bloco('Texto Exibido.', 'info', True))   # Classe e inline
print(tag_bloco('Texto Exibido.', inline=True))    # Inline
print(tag_bloco(classe='error', conteudo='Falhou.'))  # Classe e texto
print(tag_bloco(tag_lista('Iten 1', 'Iten 2'), classe='info'))
