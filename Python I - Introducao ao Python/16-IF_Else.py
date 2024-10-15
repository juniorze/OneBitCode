"""
Estruturas de Controle Condicional em Python: if, elif, else

Estas estruturas permitem que o código execute diferentes blocos baseados em condições específicas.

1. if:
   - Executa um bloco se a condição for verdadeira.
   - Sintaxe: if condição: # código

2. else:
   - Executa quando a condição do 'if' é falsa.
   - Sintaxe: 
     if condição: # código se verdadeiro
     else: # código se falso

3. elif:
   - Usado para verificar múltiplas condições.
   - Sintaxe:
     if condição1: # código
     elif condição2: # código
     else: # código

Características importantes:
- Indentação é crucial para definir blocos de código.
- Condições são avaliadas de cima para baixo.
- Usa expressões booleanas e operadores lógicos (and, or, not).

Boas práticas:
- Mantenha condições simples e legíveis.
- Use 'elif' para múltiplas condições.
- Evite muitos níveis de aninhamento.

Usos comuns: validação de entrada, tomada de decisões, lógica de negócios.

Essenciais para controle de fluxo, permitindo decisões baseadas em condições dinâmicas.
"""

name = input("Digite o nome do jogo\n")
yearLaunch = int(input("Informe o ano de lançamento do jogo\n"))
classification = float(input("Informe a nota de classificação do jogo\n"))

if classification > 8.0:
    print(f"O jogo {name} é bom. Recomendo jogá-lo.")
else:
    print(f"O jogo {name} ainda não atingiu uma boa nota, por isso não recomendo.")

a = 20
b = 30

if a != b:
    print("Os números são diferentes.")
else:
    print("Os números são iguais.")