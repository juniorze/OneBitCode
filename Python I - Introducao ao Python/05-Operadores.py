"""
Operadores Aritméticos:

Operadores aritméticos em Python são usados para realizar operações matemáticas básicas.
Eles trabalham com números (inteiros e de ponto flutuante) e, em alguns casos, com outros
tipos de dados.

Operadores Lógicos:
Python usa 'and', 'or', e 'not' para operações lógicas.
- and: Retorna True se ambas as condições forem verdadeiras
- or: Retorna True se pelo menos uma condição for verdadeira
- not: Inverte o resultado booleano
"""

# Operadores Aritméticos
print("Operadores Aritméticos:")
a, b = 10, 3

print(f"Adição: {a} + {b} = {a + b}")
print(f"Subtração: {a} - {b} = {a - b}")
print(f"Multiplicação: {a} * {b} = {a * b}")
print(f"Divisão: {a} / {b} = {a / b}")
print(f"Divisão inteira: {a} // {b} = {a // b}")
print(f"Módulo (resto): {a} % {b} = {a % b}")
print(f"Exponenciação: {a} ** {b} = {a ** b}")

# Operadores de Comparação
print("\nOperadores de Comparação:")
x, y = 5, 7

print(f"Igual a: {x} == {y} é {x == y}")
print(f"Diferente de: {x} != {y} é {x != y}")
print(f"Maior que: {x} > {y} é {x > y}")
print(f"Menor que: {x} < {y} é {x < y}")
print(f"Maior ou igual a: {x} >= {y} é {x >= y}")
print(f"Menor ou igual a: {x} <= {y} é {x <= y}")

# Operadores Lógicos
print("\nOperadores Lógicos:")
p, q = True, False

print(f"AND: {p} and {q} é {p and q}")
print(f"OR: {p} or {q} é {p or q}")
print(f"NOT: not {p} é {not p}")

# Operadores de Atribuição
print("\nOperadores de Atribuição:")
n = 10
print(f"Valor inicial de n: {n}")

n += 5  # Equivalente a: n = n + 5
print(f"Após n += 5: {n}")

n -= 3  # Equivalente a: n = n - 3
print(f"Após n -= 3: {n}")

n *= 2  # Equivalente a: n = n * 2
print(f"Após n *= 2: {n}")

n /= 4  # Equivalente a: n = n / 4
print(f"Após n /= 4: {n}")

# Operadores de Identidade
print("\nOperadores de Identidade:")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 is list2: {list1 is list2}")
print(f"list1 is list3: {list1 is list3}")
print(f"list1 is not list2: {list1 is not list2}")

# Operadores de Associação
print("\nOperadores de Associação:")
lista = [1, 2, 3, 4, 5]
print(f"Lista: {lista}")

print(f"3 in lista: {3 in lista}")
print(f"6 not in lista: {6 not in lista}")

# Operadores Bitwise
print("\nOperadores Bitwise:")
m, n = 60, 13  # 60 = 0011 1100, 13 = 0000 1101 em binário

print(f"AND bitwise: {m} & {n} = {m & n}")
print(f"OR bitwise: {m} | {n} = {m | n}")
print(f"XOR bitwise: {m} ^ {n} = {m ^ n}")
print(f"NOT bitwise: ~{m} = {~m}")
print(f"Deslocamento à esquerda: {m} << 2 = {m << 2}")
print(f"Deslocamento à direita: {m} >> 2 = {m >> 2}")