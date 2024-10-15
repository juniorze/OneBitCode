"""
Tuplas:
Tuplas são similares às listas, mas são imutáveis (não podem ser alteradas após a criação).
# Não possibilita adicionar, remover, ordenar valores na tupla
Exemplo:
"""

gamesTuple = ("Fifa23", "Red Dead 2", "Star Wars", "The Legend of Zelda", "Red Dead 2")
print(gamesTuple)
print(type(gamesTuple))

exampleTuple = ("Fifa23")
exampleTuple2 = ("Fifa23", 20, True )
print(type(exampleTuple2))
print(exampleTuple2)

# Busque os dois primeiros itens da lista
print(gamesTuple[0:2])

# Busque o último item da lista
print(gamesTuple[-1])

# Busca jogos até uma posição
print(gamesTuple[:2])

# Busca jogos de uma posição em diante
print(gamesTuple[2:])

# Recupera um item da tupla pelo índice
print(gamesTuple.index("Fifa23"))

