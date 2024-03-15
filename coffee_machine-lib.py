from automata.fa.dfa import DFA

# Definindo o autômato
maquina_cafe = DFA(
    states={'ES', 'STC', 'EP', 'PC', 'EC', 'CP', 'DT'},
    input_symbols={'S', 'Expresso', 'Cappuccino', 'Latte', 'P', 'I', 'Cancelar', 'Excedente'},
    transitions={
        'ES': {'S': 'STC'},
        'STC': {'Expresso': 'EP', 'Cappuccino': 'EP', 'Latte': 'EP', 'Cancelar': 'ES'},
        'EP': {'P': 'PC', 'I': 'EP', 'Cancelar': 'ES', 'Excedente': 'DT'},
        'PC': {'': 'EC'},
        'EC': {'': 'DT'},
        'DT': {'': 'ES'},  # Transição automática de volta ao estado inicial após a entrega e devolução do troco
        'CP': {'': 'ES'}  # Supondo que CP possa ser um estado para lidar com ações adicionais após o cancelamento
    },
    initial_state='ES',
    final_states={'DT'}
)

def simular_maquina_cafe(entradas):
    estado_atual = 'ES'
    for entrada in entradas:
        if entrada in ['Expresso', 'Cappuccino', 'Latte'] and estado_atual == 'STC':
            print(f"{entrada} selecionado.")
            estado_atual = 'EP'
        elif entrada == 'P' and estado_atual == 'EP':
            print("Pagamento recebido. Preparando café.")
            estado_atual = 'PC'
        elif entrada == 'I' and estado_atual == 'EP':
            print("Pagamento insuficiente. Tente novamente.")
        elif entrada == 'Cancelar':
            print("Pedido cancelado. Por favor, faça uma nova seleção.")
            estado_atual = 'ES'
        elif entrada == 'Excedente' and estado_atual == 'EP':
            print("Pagamento excedente recebido. Preparando café.")
            estado_atual = 'DT'
        elif estado_atual == 'PC':
            print("Café pronto. Entregando café.")
            estado_atual = 'EC'
        elif estado_atual == 'DT':
            print("Café entregue. Devolvendo troco. Aproveite!")
            estado_atual = 'ES'
            break  # Assumindo que a máquina é resetada após a entrega e troco.
        else:
            print("Ação inválida para o estado atual.")
            break

    if estado_atual != 'EC' and estado_atual != 'DT':
        print("Processo não completado.")

# Exemplo de uso
simular_maquina_cafe(['S', 'Expresso', 'P'])  # Simula o processo de seleção de Expresso e pagamento
simular_maquina_cafe(['S', 'Latte', 'Excedente'])  # Pagamento excedente para Latte
simular_maquina_cafe(['S', 'Cappuccino', 'I'])  # Pagamento insuficiente para Cappuccino
simular_maquina_cafe(['S', 'Expresso', 'Cancelar'])  # Cancelamento após seleção de Expresso