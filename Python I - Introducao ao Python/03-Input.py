"""
Input:
A função input() é usada para receber entrada do usuário. Ela sempre retorna uma string. Exemplo:
"""

gameName = input("\nDigite o nome do jogo: \n")
yearLaunch = int(input("Digite o ano de lançamento: \n"))
gamePrice = float(input("Digite o preço do jogo: \n"))
noteRating= float(input("Digite a nota de avaliação do jogo: \n"))

print("\nInformações do Jogo:")
print("Nome:", gameName)
print("Ano Lançamento:", yearLaunch)
print(f"Preço R$: {gamePrice:.2f}")
print(f"Nota: {noteRating:.2f}")

print("\nTipos de dados:")
print(type(gameName))
print(type(yearLaunch))
print(type(gamePrice))
print(type(noteRating))

# Exemplo 2: Informações de um carro
model = input("\nDigite o modelo do carro: \n")
year = int(input("Digite o ano de fabricação: \n"))
price = float(input("Digite o preço do carro: \n"))
mileage = float(input("Digite a quilometragem do carro: \n"))
is_electric = input("O carro é elétrico? (True/False): \n").lower() == 'true'

print("\nInformações do carro:")
print("Modelo:", model)
print("Ano:", year)
print("Preço: R$", price)
print("Quilometragem:", mileage, "km")
print("É elétrico?", is_electric)

print("\nTipos de dados:")
print(type(model))
print(type(year))
print(type(price))
print(type(mileage))
print(type(is_electric))

# Exemplo 3: Informações de um estudante
name = input("\nDigite o nome do estudante: \n")
age = int(input("Digite a idade do estudante: \n"))
grade = float(input("Digite a média do estudante: \n"))
height = float(input("Digite a altura do estudante em metros: \n"))
is_enrolled = input("O estudante está matriculado? (True/False): \n").lower() == 'true'

print("\nInformações do estudante:")
print("Nome:", name)
print("Idade:", age)
print("Média:", grade)
print("Altura:", height, "m")
print("Está matriculado?", is_enrolled)

print("\nTipos de dados:")
print(type(name))
print(type(age))
print(type(grade))
print(type(height))
print(type(is_enrolled))