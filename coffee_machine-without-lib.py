class SimuladorMaquinaCafe:
    def __init__(self):
        self.estado_atual = 'ES'  # Estado inicial

    def selecionar_cafe(self):
        if self.estado_atual == 'ES':
            print("Café selecionado. Por favor, insira o pagamento.")
            self.estado_atual = 'EP'
        else:
            print("Seleção de café não permitida no momento.")

    def inserir_pagamento(self, pagamento):
        if self.estado_atual == 'EP':
            if pagamento == 'P':
                print("Pagamento aceito. Preparando café.")
                self.estado_atual = 'PC'
                self.preparar_cafe()
            elif pagamento == 'I':
                print("Pagamento insuficiente. Por favor, tente novamente.")
        else:
            print("Pagamento não permitido no momento.")

    def preparar_cafe(self):
        if self.estado_atual == 'PC':
            print("Café pronto. Entregando café.")
            self.estado_atual = 'EC'
            self.entregar_cafe()

    def entregar_cafe(self):
        if self.estado_atual == 'EC':
            print("Café entregue. Aproveite!")
            self.resetar_maquina()
        else:
            print("Não é possível entregar o café no momento.")

    def resetar_maquina(self):
        print("Máquina pronta para novo pedido.")
        self.estado_atual = 'ES'

# Exemplo de uso
maquina = SimuladorMaquinaCafe()

# Fluxo de uso
maquina.selecionar_cafe()  # Usuário seleciona café
maquina.inserir_pagamento('P')  # Usuário insere pagamento suficiente ('P' para pagamento correto, 'I' para insuficiente)
