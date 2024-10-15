def wellcome():
    print("Hello World")

def create_game():
    name = input("Digite o nome do jogo \n")
    yearLaunch = int(input("Digite o ano de lançamento\n"))
    gamePrice = float(input("Digite o preço do jogo\n"))
    noteRating = float(input("Digite a nota de avaliação do jogo\n"))
    print(name)
    print(yearLaunch)
    print(gamePrice)
    print(noteRating)

wellcome()
create_game()

#### Meus exemplos ####

# Função para calcular a área de um retângulo
def calcular_area_retangulo():
    largura = float(input("Digite a largura do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    area = largura * altura
    print(f"A área do retângulo é: {area}")

# Função para converter temperatura de Celsius para Fahrenheit
def celsius_para_fahrenheit():
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit}°F")

# Função para verificar se um número é par ou ímpar
def verificar_par_impar():
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        print(f"{numero} é par")
    else:
        print(f"{numero} é ímpar")

# Função para calcular a média de três números
def calcular_media():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))
    media = (num1 + num2 + num3) / 3
    print(f"A média dos números é: {media:.2f}")

# Função para contar vogais em uma palavra
"""
# um forma avançada de fazer um loop for em python nessa função.
count = 0
for letra in palavra:
    if letra in vogais:
        count += 1
"""
def contar_vogais():
    palavra = input("Digite uma palavra: ").lower()
    vogais = "aeiou"
    count = sum(1 for letra in palavra if letra in vogais)
    print(f"A palavra '{palavra}' tem {count} vogais")

# Função para gerar uma saudação personalizada
def saudacao_personalizada():
    nome = input("Digite seu nome: ")
    hora = int(input("Digite a hora atual (0-23): "))
    if 5 <= hora < 12:
        print(f"Bom dia, {nome}!")
    elif 12 <= hora < 18:
        print(f"Boa tarde, {nome}!")
    else:
        print(f"Boa noite, {nome}!")

# Chamando as funções
calcular_area_retangulo()
celsius_para_fahrenheit()
verificar_par_impar()
calcular_media()
contar_vogais()
saudacao_personalizada()