from datetime import datetime


class Projeto:
    def __init__(self,nome):
        self.nome=nome
        self.tarefas=[]

    def add(self,descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if tarefa is not tarefa.feito]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s)).'

    def procurar(self,descricao):
        # Possível Index Error!!
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]
   

class Tarefa:
    def __init__(self,descricao):
        self.descricao=descricao
        self.feito=False
        self.criacao=datetime.now()

    def concluir(self):
        self.feito=True

    def __str__(self):
        return self.descricao + (' (Concluído) ' if self.feito else '')

def main():
    casa=Projeto('Tarefas de Casa')
    casa.add('Passar Roupa')
    casa.add('Lavar Prato')
    print(casa)

    casa.procurar('Lavar Prato').concluir()
    for tarefa in casa.tarefas:
        print(f' - {tarefa}') 
    print(casa)

    # Testes  
    print(Tarefa('Passar Roupa').feito)
    print(Tarefa('Lavar Prato').feito)

    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas Secas')
    mercado.add('Carne')
    mercado.add('Tomate')

    mercado.procurar('Tomate').concluir()

    print(mercado)
    for tarefa in mercado.tarefas:
        print(f' - {tarefa}') 
    print(mercado)

main()
