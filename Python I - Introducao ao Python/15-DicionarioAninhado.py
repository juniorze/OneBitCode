"""
Dicionários Aninhados
Dicionários aninhados são estruturas de dados onde um dicionário contém outro dicionário
como valor de uma de suas chaves. Essa estrutura é extremamente útil para representar
dados hierárquicos ou complexos de forma organizada e acessível.

Características principais:
1. Hierarquia: Permite criar estruturas de dados multinível.
2. Flexibilidade: Cada dicionário interno pode ter sua própria estrutura.
3. Acesso em cadeia: Elementos podem ser acessados usando múltiplas chaves.
4. Mutabilidade: Tanto o dicionário externo quanto os internos podem ser modificados.

Usos comuns:
- Representação de dados JSON
- Configurações complexas
- Estruturas de dados para aplicações (ex: informações de usuários, produtos)
- Mapeamento de dados relacionados (ex: países e suas cidades)

Vantagens:
- Organização clara de dados relacionados
- Fácil expansão e modificação
- Eficiente para busca e recuperação de dados aninhados

Considerações:
- Pode se tornar complexo se aninhado em muitos níveis
- Requer cuidado ao acessar dados para evitar erros de KeyError

A seguir, veremos exemplos práticos de como criar, acessar e manipular dicionários aninhados.
"""

"""
Dicas para trabalhar com dicionários aninhados:
1. Use o método .get() para acessar valores, fornecendo um valor padrão para evitar KeyError.
2. Considere usar bibliotecas como pprint para uma visualização mais clara de estruturas complexas.
3. Ao acessar dados profundamente aninhados, verifique a existência de chaves intermediárias para evitar erros.
4. Para estruturas muito complexas, considere criar funções auxiliares para acessar e modificar dados.
"""

import pprint 

# Exemplo 1: Dicionário de jogos
gamesDict = {
    "fifa 23": {
        "yearLaunch": 2022,
        "classification": 8.5,
        "genre": ["esporte", "família"]
    },
    "mario odyssey": {
        "yearLaunch": 2017,
        "classification": 10.0,
        "genre": ["aventura", "3d"]
    },
    "donkey kong country": {
        "yearLaunch": 1996,
        "classification": 9.5,
        "genre": ["aventura", "plataforma"]
    }
}

# Usando PrettyPrinter para uma exibição formatada
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

# 1 - Buscando informação dentro de um dicionário aninhado
print(gamesDict["mario odyssey"]["genre"])

# 2 - Adicionando novo item a um dicionário interno
gamesDict["mario odyssey"]["players"] = 1
print(gamesDict['mario odyssey'])

# 3 - Excluindo um dicionário interno
del gamesDict["fifa 23"]
pp.pprint(gamesDict)

# Exemplo 2: Dicionário de países e cidades
countries = {
    "Brasil": {
        "capital": "Brasília",
        "population": 211000000,
        "major_cities": {
            "São Paulo": 12.18,
            "Rio de Janeiro": 6.32,
            "Salvador": 2.9
        },
        "languages": ["Português"]
    },
    "Estados Unidos": {
        "capital": "Washington, D.C.",
        "population": 331000000,
        "major_cities": {
            "New York": 8.42,
            "Los Angeles": 3.9,
            "Chicago": 2.71
        },
        "languages": ["Inglês", "Espanhol"]
    }
}

# Exibindo o dicionário completo
pp.pprint(countries)

# Acessando dados aninhados
print(f"População do Brasil: {countries['Brasil']['population']} milhões")

# Adicionando uma nova cidade ao Brasil
countries["Brasil"]["major_cities"]["Belo Horizonte"] = 2.51

# Modificando um valor aninhado
countries["Estados Unidos"]["population"] = 332000000

# Acessando e modificando um dicionário profundamente aninhado
print(f"População de São Paulo: {countries['Brasil']['major_cities']['São Paulo']} milhões")
countries["Brasil"]["major_cities"]["São Paulo"] = 12.33

# Removendo um item de um dicionário interno
del countries["Estados Unidos"]["major_cities"]["Chicago"]

# Exibindo o dicionário atualizado
pp.pprint(countries)
