"""
Métodos Strings:
Strings têm vários métodos úteis para manipulação.

Exemplo:
"""

gameName = 'Fifa23'
gameDescription = '''
Fifa 23 é um jogo de futebol
desenvolvido pela EA Sports,
e que possibilita jogar 
localmente ou online.
'''

# Métodos básicos de manipulação
print(gameName.lower())  # Converte para minúsculas
print(gameName.upper())  # Converte para maiúsculas
print(gameName.capitalize())  # Primeira letra maiúscula
print(gameName.title())  # Primeira letra de cada palavra maiúscula
print(gameName.swapcase())  # Inverte maiúsculas e minúsculas

# Métodos de remoção de espaços e caracteres
print(gameDescription.strip())  # Remove espaços no início e fim
print(gameDescription.lstrip())  # Remove espaços à esquerda
print(gameDescription.rstrip())  # Remove espaços à direita
print(gameName.strip('3'))  # Remove '3' do início e fim

# Métodos de busca e substituição
print(gameDescription.count('a'))  # Conta ocorrências de 'a'
print(gameDescription.find('futebol'))  # Encontra a posição de 'futebol'
print(gameDescription.rfind('a'))  # Encontra a última ocorrência de 'a'
print(gameDescription.index('EA'))  # Similar a find, mas lança exceção se não encontrar
print(gameDescription.rindex('a'))  # Última ocorrência, lança exceção se não encontrar
print(gameDescription.replace('Fifa', 'PES'))  # Substitui 'Fifa' por 'PES'

# Métodos de verificação
print(gameName.startswith('Fifa'))  # Verifica se começa com 'Fifa'
print(gameName.endswith('23'))  # Verifica se termina com '23'
print(gameName.isalnum())  # Verifica se é alfanumérico
print(gameName.isalpha())  # Verifica se é alfabético
print(gameName.isdigit())  # Verifica se é composto por dígitos
print(gameName.islower())  # Verifica se está em minúsculas
print(gameName.isupper())  # Verifica se está em maiúsculas
print(gameName.istitle())  # Verifica se está no formato de título
print(gameName.isspace())  # Verifica se é composto apenas por espaços
print(gameName.isdecimal())  # Verifica se todos os caracteres são decimais
print(gameName.isnumeric())  # Verifica se todos os caracteres são numéricos
print(gameName.isprintable())  # Verifica se todos os caracteres são imprimíveis

# Métodos de formatação
print(gameName.center(10))  # Centraliza em um campo de 10 caracteres
print(gameName.ljust(10))  # Justifica à esquerda em 10 caracteres
print(gameName.rjust(10))  # Justifica à direita em 10 caracteres
print(gameName.zfill(10))  # Preenche com zeros à esquerda até 10 caracteres

# Métodos de divisão e junção
print(gameDescription.split())  # Divide a string em uma lista de palavras
print(gameDescription.rsplit(',', 1))  # Divide a partir da direita
print(gameDescription.splitlines())  # Divide em linhas
print('-'.join(gameName))  # Junta os caracteres com '-'

# Métodos de codificação e decodificação
print(gameName.encode('utf-8'))  # Codifica em UTF-8
print(b'Fifa23'.decode('utf-8'))  # Decodifica de UTF-8

# Métodos de tradução
print(gameName.translate(str.maketrans('i', 'y')))  # Traduz 'i' para 'y'

# Métodos de remoção de prefixo e sufixo (Python 3.9+)
print(gameName.removeprefix('Fifa'))  # Remove o prefixo 'Fifa' se existir
print(gameName.removesuffix('23'))  # Remove o sufixo '23' se existir

# Outros métodos úteis
print(gameDescription.expandtabs(4))  # Expande tabs para 4 espaços
print(gameName.casefold())  # Similar a lower(), mas mais agressivo
print(max(gameName))  # Retorna o caractere com maior valor ASCII
print(min(gameName))  # Retorna o caractere com menor valor ASCII

# Métodos de formatação avançada
print("Jogo: {}, Ano: {}".format(gameName[:4], gameName[4:]))
print(f"Jogo: {gameName[:4]}, Ano: {gameName[4:]}")  # f-string (Python 3.6+)

# Métodos de partição
print(gameDescription.partition('futebol'))  # Divide em 3 partes na primeira ocorrência
print(gameDescription.rpartition('a'))  # Divide em 3 partes na última ocorrência