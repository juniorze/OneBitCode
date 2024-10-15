"""
List Comprehension é uma característica poderosa e concisa do Python que permite criar novas listas 
baseadas em listas existentes ou outros iteráveis em uma única linha de código.
Ela combina um loop for com uma expressão condicional opcional, resultando em código mais legível e eficiente.

As principais vantagens do List Comprehension incluem:
1. Concisão: Permite expressar operações complexas em uma única linha.
2. Legibilidade: Quando usado adequadamente, torna o código mais claro e direto.
3. Eficiência: Geralmente mais rápido que loops for tradicionais para criar listas.

No entanto, é importante usar List Comprehension com moderação. Para operações muito complexas ou 
quando a legibilidade é comprometida, pode ser melhor optar por um loop for tradicional.
List Comprehension é mais adequado para transformações e filtragens simples de dados.

Em resumo, List Comprehension é uma ferramenta valiosa no arsenal de um programador Python,
permitindo escrever código mais elegante e eficiente quando usado apropriadamente.
"""
#################################################################################
gamesList = ["Mario Odyssey", "Donkey Kong Country", "Luigi's mansion", "Kirby"]

# Exemplo 1: Filtrando jogos que contêm a letra 'a'
newList = [x for x in gamesList if "a" in x]
print("Jogos com a letra 'a':", newList)

# Exemplo 2: Criando uma lista de jogos excluindo 'Kirby'
gamesFinished = [x for x in gamesList if x != "Kirby"] 
print("Jogos finalizados (sem Kirby):", gamesFinished)

# Exemplo 3: Criando uma lista de números menores que 4
listNumbers = [x for x in range(10) if x < 4]
print("Números menores que 4:", listNumbers)

# Exemplo 4: Criando uma lista com o comprimento de cada nome de jogo
gameLengths = [len(game) for game in gamesList]
print("Comprimento dos nomes dos jogos:", gameLengths)

# Exemplo 5: Criando uma lista de jogos em maiúsculas
upperGames = [game.upper() for game in gamesList]
print("Jogos em maiúsculas:", upperGames)

# Exemplo 6: Criando uma lista de tuplas (jogo, comprimento)
gameInfo = [(game, len(game)) for game in gamesList]
print("Informações dos jogos (nome, comprimento):", gameInfo)

# Exemplo 7: Criando uma lista de jogos que começam com 'L' ou 'M'
lmGames = [game for game in gamesList if game.startswith(('L', 'M'))]
print("Jogos que começam com 'L' ou 'M':", lmGames)

