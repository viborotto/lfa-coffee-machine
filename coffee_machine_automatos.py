from automathon import DFA

class CoffeMachine:
    def __init__(self):
        
        self.caixa = 1000
        
        self.opcoes = {
            'Café filtrado': (7.50, 3),
            'Café late': (8, 3.50),
            'Café frappé': (14.50, 4.25),
            'Chocolate quente': (9.50, 5),
            'Chá': (6.50, 2)
        }
        
        self.Q = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5'}
        self.sigma = {'0', '1'}
        self.delta = {
            'q0': {'0': 'q5', '1': 'q1'},
            'q1': {'0': 'q5', '1': 'q2'},
            'q2': {'0': 'q2', '1': 'q3'},
            'q3': {'0': 'q3', '1': 'q4'},
            'q4': {'0': 'q4', '1': 'q4'},
            'q5': {'0': 'q5', '1': 'q5'}
        }
        self.initial_state = 'q0'
        self.F = {'q3', 'q4'}
        
        self.automata = DFA(self.Q, self.sigma, self.delta, self.initial_state, self.F)
        
    def exibe_opcoes(self):
        i = 0
        print('Número - Opção: Preço')
        for key, item in self.opcoes.items():
            print(f'{i} - {key}: {item[0]}')
            i+=1
        print('')
        
    def check_pagamento(self, cliente):
        return self.opcoes.get(cliente.opcao_desejada)[0] <= cliente.pagamento
        
    def get_troco(self, cliente):
        return cliente.pagamento - self.opcoes.get(cliente.opcao_desejada)[0]
    
    def check_caixa(self, cliente):
        return self.caixa > (cliente.pagamento + self.opcoes.get(cliente.opcao_desejada)[1] + self.get_troco(cliente))
    
    def att_caixa(self):
        self.caixa = self.caixa + cliente.pagamento - self.opcoes.get(cliente.opcao_desejada)[1] - self.get_troco(cliente)
    
    def exibe_caixa(self):
        print(f'O caixa está em: {self.caixa}')
    
    def atualiza_caixa(self, cliente):
        self.caixa = self.caixa + cliente.pagamento - self.opcoes.get(cliente.opcao_desejada)[1]
        
    def check_automato(self, cliente):
        
        entrada = '1' + str(int(self.check_pagamento(cliente))) + str(int(self.check_caixa(cliente))) + '1' + str(int(self.get_troco(cliente)>0))
        
        if self.automata.accept(entrada):
            print('Pedido aprovado!')
            self.att_caixa()
        else:
            print('Pedido não aprovado')
        
        if not self.check_caixa(cliente):
            print('Caixa insuficiente!')
        
        cliente.set_troco(self.get_troco(cliente))

class Cliente:
    def __init__(self, opcao_desejada, pagamento):
        self.opcao_desejada = opcao_desejada
        self.pagamento = pagamento
        
    def set_troco(self, troco):
        self.troco = troco
        
    def exibe_troco(self):
        if self.troco > 0:
            print(f'Seu troco é de: {self.troco}')

maq = CoffeMachine()
maq.automata.is_valid()

# estilo default
maq.automata.view("DFA Visualization")

maq.automata.view(
    file_name="DFA Visualization_personalizado",
    node_attr={'fontsize': '20'},
    edge_attr={'fontsize': '20pt'}
)

## Funcionamento dos pedidos
print('Entre com -1 para sair\n')
maq.exibe_opcoes()

while True:
    opcao = int(input('Selecione o número da opção desejada: '))
    
    if opcao < 0:
        print('Obrigado por ser nosso cliente! Até mais!')
        break
    if opcao > 4:
        print('Não há essa opção no cardápio\n')
        continue
        
    pagamento = float(input('Entre com o pagamento: '))

    opcao_desejada = list(maq.opcoes.keys())[opcao]

    cliente = Cliente(opcao_desejada, pagamento)

    resultado = maq.check_automato(cliente)
    cliente.exibe_troco()
    maq.exibe_caixa()
    
    print()
