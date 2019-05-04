def tag_bloco(texto, classe='success'):  # classe é um parametro opcional
    return f'<div class="{classe}"> {texto}</div>'


print(tag_bloco('bloco'))
