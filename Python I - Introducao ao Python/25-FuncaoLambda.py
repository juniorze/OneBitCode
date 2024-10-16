"""
Funções Lambda em Python

Funções lambda, também conhecidas como funções anônimas, são pequenas funções que podem
ter qualquer número de argumentos, mas podem ter apenas uma expressão. 
Elas são úteis quando você precisa de uma função simples por um curto período de tempo.

Características principais:
- Sintaxe concisa: lambda argumentos: expressão
- Podem ser usadas em linha, sem necessidade de definir uma função formal
- Úteis para operações simples e de curta duração
- Comumente usadas com funções como map(), filter(), e sort()

Usabilidades:
1. Funções de ordem superior: Como argumentos para funções como map() e filter()
2. Ordenação personalizada: Como key em funções de ordenação
3. Callbacks: Em GUIs e outras situações que requerem funções simples como callbacks
4. Operações rápidas: Para transformações simples de dados sem definir uma função completa

Limitações:
- Restritas a expressões simples
- Não podem conter múltiplas expressões ou declarações complexas
- Menos legíveis para operações complexas
"""

# Função lambda para elevar um número ao quadrado
power = lambda num: num ** 2

# Função lambda para verificar se um número é par
pair = lambda x: x % 2 == 0

# Função lambda para dividir dois números
divNum = lambda x, y: x / y

# Função lambda para inverter uma string
reverse = lambda s: s[::-1]

# Função lambda para calcular o comprimento de uma string
length = lambda s: len(s)

# Função lambda para verificar se um número está em um intervalo
in_range = lambda x, start, end: start <= x <= end

# Testando as funções lambda
print("Quadrado de 5:", power(5))
print("Quadrado de 9:", power(9))
print("27 é par?", pair(27))
print("30 é par?", pair(30))
print("10 dividido por 2:", divNum(10, 2))
print("7 dividido por 2:", divNum(7, 2))
print("'Função' invertida:", reverse("Função"))
print("'Tecnologia' invertida:", reverse("Tecnologia"))
print("Comprimento de 'Python':", length("Python"))
print("Comprimento de 'Lambda':", length("Lambda"))
print("5 está entre 1 e 10?", in_range(5, 1, 10))
print("15 está entre 1 e 10?", in_range(15, 1, 10))

# Exemplo de uso de lambda com map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("Lista original:", numbers)
print("Lista com quadrados:", squared)

# Exemplo de uso de lambda com filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Números originais:", numbers)
print("Números pares:", evens)