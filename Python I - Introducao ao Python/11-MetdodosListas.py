"""
Métodos Listas:
Listas têm vários métodos para manipulação.

Exemplo:
"""

gamesList = ["Fifa23", "Star Wars", "The Legend of Zelda", "Red Dead 2"]

# 1 - Tamanho da lista
print(len(gamesList))

# 2 - Recupera um item da lista pelo índice
print(gamesList.index("Star Wars"))

# 3 - Adiciona item ao final da lista
gamesList.append("Gta V")
print(gamesList)

# 4 - Ordena lista
gamesList.sort()
print(gamesList)

# 5 - Copia os itens de uma lista para outra
gamesReset = gamesList.copy()
gamesReset.remove('Fifa23')
gamesReset.remove('Star Wars')
print(gamesReset)

# 6 - Remove todos os itens da lista
gamesList.clear()
print(gamesList)

# 7 - Conta o número de ocorrências de um item na lista
gamesList = ["Fifa23", "Star Wars", "The Legend of Zelda", "Red Dead 2", "Star Wars"]
print(gamesList.count("Star Wars"))

# 8 - Estende a lista adicionando elementos de outra lista
newGames = ["Cyberpunk 2077", "Elden Ring"]
gamesList.extend(newGames)
print(gamesList)

# 9 - Insere um item em uma posição específica da lista
gamesList.insert(2, "God of War")
print(gamesList)

# 10 - Remove e retorna o último item da lista
lastGame = gamesList.pop()
print(f"Último jogo removido: {lastGame}")
print(gamesList)

# 11 - Remove a primeira ocorrência de um item específico
gamesList.remove("Fifa23")
print(gamesList)

# 12 - Inverte a ordem dos elementos na lista
gamesList.reverse()
print(gamesList)

# 13 - Retorna uma cópia da lista ordenada sem modificar a original
sortedGames = sorted(gamesList)
print("Lista ordenada:", sortedGames)
print("Lista original:", gamesList)

# 14 - Cria uma lista de tuplas com índices e valores
for index, game in enumerate(gamesList):
    print(f"Índice: {index}, Jogo: {game}")

# 15 - Verifica se um item está na lista
print("Star Wars" in gamesList)

# 16 - Acessa elementos com índices negativos (contagem reversa)
print("Último jogo:", gamesList[-1])
print("Penúltimo jogo:", gamesList[-2])

# 17 - Fatia a lista para obter uma sublista
print("Três primeiros jogos:", gamesList[:3])
print("Jogos do meio:", gamesList[2:-2])

# 18 - Cria uma cópia rasa da lista
gamesCopy = gamesList[:]
print("Cópia da lista:", gamesCopy)

# 19 - Concatena listas
moreGames = ["Minecraft", "Fortnite"]
allGames = gamesList + moreGames
print("Lista concatenada:", allGames)

# 20 - Limpa a lista e adiciona novos elementos
gamesList.clear()
gamesList.extend(["Hades", "Hollow Knight", "Celeste"])
print("Nova lista de jogos:", gamesList)