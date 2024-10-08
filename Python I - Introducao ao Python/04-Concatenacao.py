# Coletando informações sobre um jogo
name = input("Digite o nome do jogo: \n")
yearLaunch = int(input("Digite o ano de lançamento do jogo: \n"))
gamePrice = float(input("Digite o preço do jogo: \n"))
planIncluded = input("Está incluso no serviço mensal? (Sim/Não): \n")

print("\n===== Dados do Jogo =====\n")

# Alternativa 1
print("Nome do Jogo:", name)
print("Ano do Jogo:", yearLaunch)
print("Preço do Jogo:", gamePrice)
print("Está incluído no plano?", planIncluded)

# Alternativa 2
print("Nome do Jogo:", name, "\nAno de lançamento:", yearLaunch,
    "\nPreço do Jogo:", gamePrice, "\nEstá incluso no serviço?", planIncluded)

# Usando o método format()
print("Nome: {}\nAno de Lançamento: {}\nPreço: R$ {:.2f}\nIncluso no serviço: {}".format(name, yearLaunch, gamePrice, planIncluded))
# Usando concatenação com '+'
print("\nO jogo " + name + ", lançado em " + str(yearLaunch) + ", custa R$ " + str(gamePrice) + " e " + ("está" if planIncluded.lower() == "sim" else "não está") + " incluso no serviço mensal.")
# Usando f-strings (como no exemplo original)
print(f"\nResumo: {name} ({yearLaunch}) - Preço: R$ {gamePrice:.2f} - Incluso no serviço: {planIncluded}")


# Coletando informações sobre um filme
titulo = input("Digite o título do filme: ")
diretor = input("Digite o nome do diretor: ")
ano = int(input("Digite o ano de lançamento: "))
nota = float(input("Digite a nota do filme (0-10): "))

print("\n===== Informações do Filme =====")
# Usando o método format()
print("Título: {}\nDiretor: {}\nAno: {}\nNota: {:.1f}".format(titulo, diretor, ano, nota))
# Usando concatenação com '+'
print("\nO filme " + titulo + ", dirigido por " + diretor + ", foi lançado em " + str(ano) + " e recebeu uma nota de " + str(nota) + ".")
# Usando f-strings (como no exemplo original)
print(f"\nResumo: {titulo} ({ano}) - Direção: {diretor} - Nota: {nota:.1f}")