from automata.fa.dfa import DFA

# Definindo o autômato
maquina_cafe = DFA(
    states={'ES', 'EP', 'PC', 'EC'},
    input_symbols={'S', 'P', 'I'},
    transitions={
        'ES': {'S': 'EP'},
        'EP': {'P': 'PC', 'I': 'EP'},
        'PC': {'': 'EC'},  # Transição automática para EC uma vez que o café está pronto
        'EC': {}  # Não são necessárias transições de EC, pois é um estado final
    },
    initial_state='ES',
    final_states={'EC'}
)

# Exemplo de uso
def simular_maquina_cafe(entradas):
    estado_atual = maquina_cafe.initial_state
    for entrada in entradas:
        estado_atual = maquina_cafe.transitions[estado_atual][entrada]
        if estado_atual == 'EC':
            print("Café entregue. Aproveite!")
            break
        elif estado_atual == 'EP':
            print("Aguardando pagamento.")
        elif estado_atual == 'PC':
            print("Preparando café.")
    if estado_atual != 'EC':
        print("Processo não completado.")

simular_maquina_cafe(['S', 'P'])  # Simula o processo de seleção de café e pagamento
