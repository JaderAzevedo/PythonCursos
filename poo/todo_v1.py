from datetime import datetime

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
    casa=[]
    casa.append(Tarefa('Passar Roupa'))
    casa.append(Tarefa('Lavar Prato'))

    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar Prato']
    for tarefa in casa:
        print(f'- {tarefa}')

main()
