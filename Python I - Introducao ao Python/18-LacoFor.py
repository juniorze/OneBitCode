"""
Laço For:
O laço for é usado para iterar sobre uma sequência (lista, tupla, string, etc.).
"""

# Lista de jogos para os exemplos
gamesList = ["Fifa", "God of War", "Red Dead 2", "Uncharted"]

# 1. Iteração simples sobre uma lista
print("1. Iteração simples sobre uma lista:")
for game in gamesList:
    print(game)

print("\n2. Loop com break:")
# 2. Loop com break
for game in gamesList:
    if game == "God of War":
        break
    print(game)

print("\n3. Loop com continue:")
# 3. Loop com continue
for game in gamesList:
    if game == "God of War":
        continue
    print(game)

print("\n4. Loop com range() e cálculo de média:")
# 4. Loop com range() e cálculo de média
gameName = input("Digite o nome do jogo: ")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo: "))

sum = 0
for i in range(gameRating):
    note = float(input(f"Digite a nota {i+1} para o jogo: "))
    sum += note
print(f"Média de avaliação do jogo {gameName} é: {sum/gameRating:.2f}")

print("\n5. Contagem regressiva com range():")
# 5. Contagem regressiva com range()
countdown = int(input("Digite um número para iniciar a contagem regressiva: "))
for i in range(countdown, 0, -1):
    print(i)
print("Lançamento!")

print("\n6. Loop com enumerate():")
# 6. Loop com enumerate()
games = ["Mario", "Zelda", "Metroid", "Pokémon"]
for index, game in enumerate(games, start=1):
    print(f"{index}. {game}")

print("\n7. Cálculo de fatorial:")
# 7. Cálculo de fatorial
number = int(input("Digite um número para calcular o fatorial: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"O fatorial de {number} é {factorial}")

print("\n8. Iteração sobre uma string:")
# 8. Iteração sobre uma string
word = input("Digite uma palavra: ")
for char in word:
    print(f"A letra '{char}' aparece {word.count(char)} vez(es) na palavra.")