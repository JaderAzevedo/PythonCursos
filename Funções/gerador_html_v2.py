# classe e inline são  parametros opcionais
def tag_bloco(texto, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}"> {texto}</{tag}>'


print(tag_bloco('bloco'))
print(tag_bloco('Texto Exibido.', 'info', True))   # Classe e inline
print(tag_bloco('Texto Exibido.', inline=True))    # Inline
print(tag_bloco(classe='error', texto='Falhou.'))  # Classe e texto
