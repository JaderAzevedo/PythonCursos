class HtmlToStringMixin():
    def __str__(self):
        # Conversão para HTML
        html = super().__str__()\
            .replace('(', '<strong>(')\
            .replace(')', ')<strong>')
        return f'<span>{html}</span>'


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


class Animal:
    def __init__(self, nome, pet=True):
        self.nome = nome
        self.pet = pet

    def __str__(self):
        return self.nome + '(pet)' if self.pet else ''


class PessoaHTML(HtmlToStringMixin, Pessoa):
    pass


class AnimalHTML(HtmlToStringMixin, Animal):
    pass


# A ordem influencia no resultado
# class PessoaHTML(Pessoa, HtmlToStringMixin):
#     pass


# class AnimalHTML(Animal, HtmlToStringMixin):
#     pass


p1 = Pessoa('Maria Eduarda')
print(p1)

p2 = PessoaHTML('Roberto Carlos')
print(p2)

toto = AnimalHTML('Toto')
print(toto)
