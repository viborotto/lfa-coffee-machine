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

# Esboco de MVP
A ideia é começar com um projeto menos complexo com poucos estados e transicoes, e evoluir ao longo do quadrimestre

**Estados**
Vamos considerar um conjunto simplificado de estados pelos quais a máquina de café pode passar:

1. Esperando Seleção (ES): O estado inicial onde a máquina está pronta para que o usuário faça sua seleção de café.
2. Esperando Pagamento (EP): O usuário selecionou um tipo de café e agora deve inserir o pagamento.
3. Preparando Café (PC): O pagamento foi recebido; a máquina está preparando o café selecionado.
4. Entregando Café (EC): O estado final onde o café é entregue ao usuário.

**Alfabeto (Entradas)**
O alfabeto consiste em símbolos que representam as ações ou entradas possíveis na máquina:

- Seleção de Café (S): Representa a ação de selecionar um tipo de café. Para simplificar, podemos considerar apenas um tipo de café neste MVP.
- Pagamento Correto (P): Representa a inserção de um pagamento adequado para o café selecionado.
- Pagamento Insuficiente (I): Representa a inserção de um pagamento insuficiente.

**Transições**
As transições entre estados são definidas pelas ações do usuário representadas no alfabeto:
- ES --S-->EP: De "Esperando Seleção" para "Esperando Pagamento" após a seleção de café.
- EP --P-->PC: De "Esperando Pagamento" para "Preparando Café" após receber o pagamento correto.
- EP --I--> EP: Permanece em "Esperando Pagamento" se o pagamento for insuficiente.
- PC ----> EC: De "Preparando Café" para "Entregando Café", transição automática uma vez que o café está pronto.

**Estado Inicial**
Esperando Seleção (ES): A máquina começa neste estado, esperando que o usuário faça uma seleção.

**Estados Finais**
Entregando Café (EC): Considerado um estado final, onde a máquina entregou o café e o processo está completo.
