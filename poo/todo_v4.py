from datetime import datetime ,timedelta



class Projeto:
    def __init__(self,nome):
        self.nome=nome
        self.tarefas=[]

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self,descricao,vencimento=None):
        self.tarefas.append(Tarefa(descricao,vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]
        
        # Errei bantante aqui!!
        #        [tarefa for tarefa in self.tarefas if not tarefa.feito] 
        #[tarefa for tarefa in self.tarefas if tarefa is not tarefa.feito]

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s)).'

    def procurar(self,descricao):
        # Possível Index Error!!
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]
   

class Tarefa:
    def __init__(self,descricao,vencimento=None):
        self.descricao=descricao
        self.feito=False
        self.criacao=datetime.now()
        self.vencimento=vencimento

    def concluir(self):
        self.feito=True

    def __str__(self):
        status=[]
        if self.feito:
            status.append('(Concluída)')
        elif self.vencimento:
            if datetime.now() > self.vencimento: 
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')
        return f'{self.descricao}' + ' ' .join(status)

def main():
    casa=Projeto('Tarefas de Casa')
    casa.add('Passar Roupa',datetime.now() + timedelta(days=3,minutes=12))
    casa.add('Lavar Prato')
    print(casa)

    casa.procurar('Lavar Prato').concluir()
    for tarefa in casa:
        print(f' - {tarefa}') 
    print(casa)

    # Testes  
    #print(Tarefa('Passar Roupa').feito)
    #print(Tarefa('Lavar Prato').feito)

    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas Secas',datetime.now() + timedelta(days=3,minutes=12))
    mercado.add('Carne')
    mercado.add('Tomate',datetime.now() + timedelta(days=3,minutes=12))

    mercado.procurar('Tomate').concluir()

    print(mercado)
    for tarefa in mercado:
        print(f' - {tarefa}') 
    print(mercado)

main()
