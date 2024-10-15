"""
Dicionários de Dados:
São estruturas que armazenam pares de chave-valor. 
Eles são extremamente úteis para representar coleções de informações relacionadas.

Dicionários são extremamente versáteis e são frequentemente usados para:
- Armazenar configurações
- Representar objetos complexos
- Criar mapeamentos eficientes
- Implementar caches simples

Eles são uma parte fundamental da programação em Python e são amplamente utilizados
em muitas aplicações e bibliotecas.

Características principais:
1. Mutáveis: Podem ser modificados após a criação.
2. Não ordenados: A ordem dos elementos não é garantida (antes do Python 3.7).
3. Chaves únicas: Cada chave deve ser única no dicionário.
4. Chaves imutáveis: As chaves devem ser de tipos imutáveis (strings, números, tuplas).

Sintaxe básica:
dicionario = {chave1: valor1, chave2: valor2, ...}

Exemplos de uso:
"""
gameFifa = {
    "price": 90.55,
    "yearLaunch": 2022,
    "version": 2023,
    "classification": 8.5,
    "genre": ["esporte", "família"]
}
print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# 1 - Recuperando um elemento do dicionário
print(gameFifa['genre'])
print(gameFifa.get('classification'))

# 2 - Buscando apenas as chaves
print(gameFifa.keys())

# 3 - Buscando apenas os valores
print(gameFifa.values())

# 4 - Retorna itens do dicionário como tupla de uma lista 
print(gameFifa.items())

# 5 - Adicionando itens no dicionário
gameFifa["players"] = 2
print(gameFifa)

# 6 - Atualizando itens no dicionário
gameFifa.update({"players": 1})
print(gameFifa)

# 7 - Removendo item no dicionário
gameFifa.pop("players")
print(gameFifa)
