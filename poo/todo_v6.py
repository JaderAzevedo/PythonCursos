from datetime import datetime ,timedelta


class Projeto:
    def __init__(self,nome):
    def __init__(self,nome):
        self.nome=nome
        self.tarefas=[]

    def __iter__(self):
        return self.tarefas.__iter__()


    #  Simulando o Over-Load em Python
    # Usando o método add para chamar os métodos _add_tarefa e _add_nova_terafa

    def add(self,tarefa,vencimento=None,**kwargs):
        funcao_escolhida= self._add_tarefa if isinstance(tarefa,Tarefa) \
            else self._add_nova_tarefa
        kwargs['vencimento']=vencimento
        funcao_escolhida(tarefa,**kwargs)
        #self.tarefas.append(Tarefa(descricao,vencimento))


    # Medotos 'Privados' em começão com _(underline), 
    # é apenas uma convenção, pois não existe método privado em Python
    #
    def _add_tarefa(self,tarefa,**kwargs):
        self.tarefas.append(tarefa)

    # Medotos 'Privados' em começãm com _(underline),
    # é apenas uma convenção, pois não existe método privado em Python
    
    def _add_nova_tarefa(self,descricao,**kwargs):
        self.tarefas.append(Tarefa(descricao,kwargs.get('vencimento',None)))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]
              

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


class TarefaRecorrente(Tarefa):     #TarefaRecorrente é uma subclasse de Tarefa\
                                    # Herança
    
    
    def __init__(self,descricao,vencimento,dias=7):
        super().__init__(descricao,vencimento)
        self.dias=dias

    def concluir(self):
        super().concluir()
        novo_vencimento=datetime.now() + timedelta(days=self.dias)
        return TarefaRecorrente(self.descricao,novo_vencimento,self.dias)
    


def main():
    casa=Projeto('Tarefas de Casa')
    casa.add('Passar Roupa',datetime.now())
    casa.add('Lavar Prato')
    casa.add('Lavar Louça')
    casa.add(TarefaRecorrente('Trocar Lençois', datetime.now(),7))
    casa.add(casa.procurar('Trocar Lençois').concluir())
    print(casa)

    casa.procurar('Lavar Prato').concluir()
    for tarefa in casa:
        print(f' - {tarefa}') 
    print(casa)

    # Testes  
    print(Tarefa('Passar Roupa').feito)
    print(Tarefa('Lavar Prato').feito)

    mercado = Projeto('Compras no mercado')
    mercado.add('Frutas Secas',datetime.now() + timedelta(days=3,minutes=12))
    mercado.add('Carne')
    mercado.add('Tomate',datetime.now() + timedelta(days=3,minutes=12))

    mercado.procurar('Tomate').concluir()
    comprar_carne = mercado.procurar('Carne')
    comprar_carne.concluir()
    print(mercado)
    for tarefa in mercado:
        print(f' - {tarefa}') 
    print(mercado)

main()
