# lfa-coffee-machine
Projeto python para matéria de LFA da UFABC 1.2024

## 1. Definição do Problema
Primeiro, definiremos claramente o problema que o seu autômato (a máquina de café) precisa resolver. Isso inclui identificar os estados possíveis da máquina (por exemplo, esperando seleção, pagamento recebido, café sendo feito, etc.) e os eventos ou entradas que causam transições entre esses estados (por exemplo, seleção de um tipo de café, inserção de dinheiro, etc.).

## 2. Modelagem do Autômato
**Estados**: Identificar todos os estados possíveis que a máquina de café pode ter. Alguns exemplos sugeridos pelo grupo:

- Esperando seleção
- Esperando pagamento
- Preparando café
- Entregando café
- Devolvendo troco (se aplicável)
  
**Alfabeto**: Determinar as entradas (símbolos do alfabeto) que a máquina aceitará. Isso pode incluir:

- Seleção de tipo de café (expresso, com leite, etc.)
- Inserção de diferentes valores de dinheiro
- Botão de cancelamento

**Transições**: Definir as transições entre estados baseadas nas entradas. Por exemplo, passar do estado de "Esperando pagamento" para "Preparando café" após o pagamento adequado.

**Estado Inicial e Estados Finais**: Identificar claramente qual é o estado inicial (provavelmente "Esperando seleção") e quais são os estados finais (possivelmente "Entregando café" ou "Devolvendo troco").

