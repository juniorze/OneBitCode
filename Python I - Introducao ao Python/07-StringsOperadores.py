"""
Strings com Operadores:
Strings podem ser manipuladas com vários operadores, como '+' para concatenação e '*' para repetição.
Exemplo:
"""
# Exemplo 1: Manipulação e formatação de strings
nome_jogo = "The Legend of Zelda"
ano_lancamento = 2023
preco = 299.99

print("=" * 40)
print("Exemplo 1: Manipulação e formatação de strings")
print("=" * 40)
print(f"Jogo: {nome_jogo.upper()}")
print(f"Lançamento: {ano_lancamento}")
print(f"Preço: R$ {preco:.2f}")
print(f"Primeiras 10 letras: {nome_jogo[:10]}")
print(f"Invertido: {nome_jogo[::-1]}")
print(f"Número de 'e's: {nome_jogo.count('e')}")
print(f"Substituindo: {nome_jogo.replace('Legend', 'Chronicles')}")
print("=" * 40)

# Exemplo 2: Splitting e joining strings
generos = "RPG,Ação,Aventura,Open World"
lista_generos = generos.split(",")

print("\nExemplo 2: Splitting e joining strings")
print("=" * 40)
print("Gêneros:")
for genero in lista_generos:
    print(f"- {genero.strip()}")

plataformas = ["PS5", "Xbox Series X", "Nintendo Switch", "PC"]
plataformas_string = " | ".join(plataformas)
print(f"\nDisponível para: {plataformas_string}")
print("=" * 40)

# Exemplo 3: Formatação avançada e alinhamento
titulo = "Ranking de Jogos"
jogos = [
    ("The Witcher 3", 9.8),
    ("Red Dead Redemption 2", 9.7),
    ("God of War", 9.9),
    ("Breath of the Wild", 9.6)
]

print("\nExemplo 3: Formatação avançada e alinhamento")
print("=" * 40)
print(f"{titulo:^40}")  # Centralizado em 40 caracteres
print("=" * 40)

for jogo, nota in jogos:
    print(f"{jogo:<30} {nota:>5.1f}")  # Alinhado à esquerda (30) e à direita (5)

print("=" * 40)


# Exemplo 1: Manipulação e formatação de strings
nome_jogo = "The Legend of Zelda"
ano_lancamento = 2023
preco = 299.99

print("=" * 40)
print("Exemplo 1: Manipulação e formatação de strings")
print("=" * 40)
print(f"Jogo: {nome_jogo.upper()}")
print(f"Lançamento: {ano_lancamento}")
print(f"Preço: R$ {preco:.2f}")
print(f"Primeiras 10 letras: {nome_jogo[:10]}")
print(f"Invertido: {nome_jogo[::-1]}")
print(f"Número de 'e's: {nome_jogo.count('e')}")
print(f"Substituindo: {nome_jogo.replace('Legend', 'Chronicles')}")
print("=" * 40)

# Exemplo 2: Splitting e joining strings
generos = "RPG,Ação,Aventura,Open World"
lista_generos = generos.split(",")

print("\nExemplo 2: Splitting e joining strings")
print("=" * 40)
print("Gêneros:")
for genero in lista_generos:
    print(f"- {genero.strip()}")

plataformas = ["PS5", "Xbox Series X", "Nintendo Switch", "PC"]
plataformas_string = " | ".join(plataformas)
print(f"\nDisponível para: {plataformas_string}")
print("=" * 40)

# Exemplo 3: Formatação avançada e alinhamento
titulo = "Ranking de Jogos"
jogos = [
    ("The Witcher 3", 9.8),
    ("Red Dead Redemption 2", 9.7),
    ("God of War", 9.9),
    ("Breath of the Wild", 9.6)
]

print("\nExemplo 3: Formatação avançada e alinhamento")
print("=" * 40)
print(f"{titulo:^40}")  # Centralizado em 40 caracteres
print("=" * 40)

for jogo, nota in jogos:
    print(f"{jogo:<30} {nota:>5.1f}")  # Alinhado à esquerda (30) e à direita (5)

print("=" * 40)