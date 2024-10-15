def full_name(fname, lname):
    print(f"{fname} {lname}")

def sum(a, b):
    print(a + b)

def address(country="Brasil"):
    print(f"Eu moro no {country}")

full_name("Rodrigo", "Macedo")
sum(20, 10)
address()
address("Canadá")

def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo\n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo \n"))
        sum += note
    print(f"Média de avaliação do jogo {game_name} é: {sum/qtdRating}")

rating = int(input("Digite quantas avaliações deseja fazer no jogo\n"))
rating_game(rating)


### Meus exemplos ###
# Exemplo 1: Função para calcular o preço final de um produto com desconto

def calcular_preco_com_desconto(preco_original, percentual_desconto=0):
    desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - desconto
    print(f"Preço original: R${preco_original:.2f}")
    print(f"Desconto: {percentual_desconto}%")
    print(f"Preço final: R${preco_final:.2f}")

# Chamadas da função
calcular_preco_com_desconto(100, 10)  # Com desconto de 10%
calcular_preco_com_desconto(50)       # Sem desconto (usa o valor padrão de 0%)

# Exemplo 2: Função para criar um perfil de usuário

def criar_perfil_usuario(nome, idade, cidade="Não informada", hobby=None):
    perfil = f"Nome: {nome}\nIdade: {idade}\nCidade: {cidade}"
    if hobby:
        perfil += f"\nHobby: {hobby}"
    else:
        perfil += "\nHobby: Não informado"
    
    print("Perfil do Usuário:")
    print(perfil)

# Chamadas da função
criar_perfil_usuario("Ana", 25, "São Paulo", "Leitura")
criar_perfil_usuario("Carlos", 30)
criar_perfil_usuario("Mariana", 28, hobby="Natação")