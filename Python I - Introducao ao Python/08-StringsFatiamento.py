"""
Strings Fatiamento:
O fatiamento permite extrair partes de uma string usando a sintaxe [start:end:step].
"""

# Exemplos de Geração de Substrings em Python
gameName = 'Fifa23'
gameDescription = '''
Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports
e que possibilita jogar 
localmente ou online.
                '''
# string[início:fim] - índice começa com 0 | índice final -1

# Busque toda string a partir da primeira posição
print(gameName[0:])

# Busque toda string até a última posição
print(gameName[:6])

# Busque toda string da primeira até a última posição
print(gameName[0:6])

"""
string[início:fim:passo] - índice começa com 0 | índice final -1 | 
passo - determina o incremento. Por padrão esse número é o 1
"""

#Busque toda a string de 2 em 2 caracteres.
print(gameName[::2])

# Inverta uma string de trás pra frente
print(gameName[::-1])

# Imprime os caracteres nos índices ímpares
print(gameName[1::2])





texto_original = "Python é uma linguagem de programação poderosa e versátil"

print("Texto original:")
print(texto_original)
print("=" * 60)

# Exemplo 1: Fatiamento básico
print("1. Fatiamento básico:")
print(f"Primeiros 6 caracteres: '{texto_original[:6]}'")
print(f"Últimos 8 caracteres: '{texto_original[-8:]}'")
print(f"Do 7º ao 15º caractere: '{texto_original[6:15]}'")
print("=" * 60)

# Exemplo 2: Fatiamento com passo
print("2. Fatiamento com passo:")
print(f"Caracteres alternados: '{texto_original[::2]}'")
print(f"String invertida: '{texto_original[::-1]}'")
print(f"A cada 3 caracteres: '{texto_original[::3]}'")
print("=" * 60)

# Exemplo 3: Extração de palavras
print("3. Extração de palavras:")
palavras = texto_original.split()
print(f"Primeira palavra: '{palavras[0]}'")
print(f"Última palavra: '{palavras[-1]}'")
print(f"Terceira e quarta palavras: '{' '.join(palavras[2:4])}'")
print("=" * 60)

# Exemplo 4: Usando find() e índices
print("4. Usando find() e índices:")
inicio = texto_original.find("linguagem")
fim = texto_original.find("poderosa")
print(f"Substring entre 'linguagem' e 'poderosa': '{texto_original[inicio:fim].strip()}'")
print("=" * 60)

# Exemplo 5: Extração com condições
print("5. Extração com condições:")
vogais = ''.join([char for char in texto_original if char.lower() in 'aeiou'])
consoantes = ''.join([char for char in texto_original if char.isalpha() and char.lower() not in 'aeiou'])
print(f"Apenas vogais: '{vogais}'")
print(f"Apenas consoantes: '{consoantes}'")
print("=" * 60)

# Exemplo 6: Substring entre dois caracteres específicos
print("6. Substring entre dois caracteres específicos:")
inicio = texto_original.index('é')
fim = texto_original.index('poderosa')
print(f"Entre 'é' e 'poderosa': '{texto_original[inicio+1:fim].strip()}'")
print("=" * 60)

# Exemplo 7: Extração de substrings de tamanho fixo
print("7. Extração de substrings de tamanho fixo:")
tamanho = 10
for i in range(0, len(texto_original), tamanho):
    print(f"Substring de {tamanho} caracteres: '{texto_original[i:i+tamanho]}'")