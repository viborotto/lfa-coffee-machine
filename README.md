# :coffee: lfa-coffee-machine
Projeto python para matéria de LFA da UFABC 1.2024

## 1. Definição do Problema
Primeiro, definiremos claramente o problema que o seu autômato (a máquina de café) precisa resolver. Isso inclui identificar os estados possíveis da máquina (por exemplo, esperando seleção, pagamento recebido, café sendo feito, etc.) e os eventos ou entradas que causam transições entre esses estados (por exemplo, seleção de um tipo de café, inserção de dinheiro, etc.).

## 2. Modelagem do Autômato
**Estados**: Identificar todos os estados possíveis que a máquina de café pode ter. Alguns exemplos sugeridos pelo grupo:

- Esperando seleção (q0)
- Esperando pagamento (q1)
- Preparando café (q2)
- Entregando café (q3)
- Devolvendo troco (q4)
- Cancelando Pedido (q5)
  
**Alfabeto**: Determinar as entradas (símbolos do alfabeto) que a máquina aceitará. Isso pode incluir:

- 0:Falso
- 1:Verdadeiro
Quando a condição estabelecida pela máquina é atendida, o caracter 1 do alfabeto é colocado na entrada do autômato. Caso contrário, o caracter 0 é inserido.


**Transições**: Definir as transições entre estados baseadas nas entradas. Por exemplo, passar do estado de "Esperando pagamento" para "Preparando café" após o pagamento adequado.

**Estado Inicial e Estados Finais**: Identificar claramente qual é o estado inicial (provavelmente "Esperando seleção") e quais são os estados finais (possivelmente "Entregando café" ou "Devolvendo troco").

# Esboco de MVP
A ideia é começar com um projeto menos complexo com poucos estados e transicoes, e evoluir ao longo do quadrimestre

**Estados**
Vamos considerar um conjunto simplificado de estados pelos quais a máquina de café pode passar:

1. Esperando Seleção (q0): O estado inicial onde a máquina está pronta para que o usuário faça sua seleção de café.
2. Esperando Pagamento (q1): O usuário selecionou um tipo de café e agora deve inserir o pagamento.
3. Preparando Café (q2): O pagamento foi recebido; a máquina está preparando o café selecionado.
4. Entregando Café (q3): O estado final onde o café é entregue ao usuário.
5. Devolvendo Troco (q4): Estado final após entregar o café e devolver o troco, se necessário.
6. Cancelando Pedido (q5): Um estado transitório para quando um pedido é cancelado, levando de volta ao estado inicial.


**Alfabeto (Entradas)**
O alfabeto consiste em símbolos que representam as ações ou entradas possíveis na máquina:

- 0:Falso
- 1:Verdadeiro
Quando a condição estabelecida pela máquina é atendida, o caracter 1 do alfabeto é colocado na entrada do autômato. Caso contrário, o caracter 0 é inserido.

**Transições**
As transições entre estados são definidas pelas ações do usuário representadas no alfabeto:

![image](https://github.com/viborotto/lfa-coffee-machine/assets/60987091/ac46a610-a659-4d4b-9317-534f2e11e452)


**Estado Inicial**
Esperando Seleção (q0): A máquina começa neste estado, esperando que o usuário faça uma seleção.

**Estados Finais**
Entregando Café (q3)*: O café está pronto e é entregue ao usuário (estado final).
Devolvendo Troco (q4)*: O estado opcional onde a máquina devolve o troco, se o pagamento excedeu o valor do café (estado final).

### Diagrama AFD
![diagrama](https://github.com/viborotto/lfa-coffee-machine/blob/main/DFA%20Visualization.gv.png)
