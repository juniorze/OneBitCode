"""
Laço While:
O laço while executa um bloco de código enquanto uma condição for verdadeira.
#############################################
"""
import random

# Exemplo curso: Cálculo de média de avaliações de um jogo
print("Exemplo 1: Cálculo de média de avaliações de um jogo")
gameName = input("Digite o nome do jogo\n")
qtdRating = 0
totalRating = 0
rating = 0
average = 0
while(rating != -1):
    rating = float(input("Informe a nota do jogo (ou -1 para sair)\n"))
    if(rating != -1):
        totalRating += rating
        qtdRating += 1
        average = totalRating / qtdRating
print(f"Média das avaliações do jogo {gameName} é: {average:.2f}")

# Exemplo 2: Jogo de adivinhação com número aleatório
print("\nExemplo 2: Jogo de adivinhação com número aleatório")
numero_secreto = random.randint(1, 100)
tentativas = 0
palpite = 0
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 100.")
while palpite != numero_secreto:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1
    if palpite < numero_secreto:
        print("Muito baixo! Tente um número maior.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente um número menor.")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas!")

# Exemplo 3: Calculadora de juros compostos
print("\nExemplo 3: Calculadora de juros compostos")
principal = float(input("Digite o valor principal inicial: "))
taxa_juros = float(input("Digite a taxa de juros anual (em decimal): "))
anos = int(input("Digite o número de anos: "))
saldo = principal
ano_atual = 0
while ano_atual < anos:
    saldo += saldo * taxa_juros
    ano_atual += 1
    print(f"Saldo após o ano {ano_atual}: R${saldo:.2f}")
print(f"\nSaldo final após {anos} anos: R${saldo:.2f}")

# Exemplo 4: Conversor de temperatura com opção de continuar
print("\nExemplo 4: Conversor de temperatura com opção de continuar")
continuar = "s"
while continuar.lower() == "s":
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C é igual a {fahrenheit:.1f}°F")
    continuar = input("Deseja converter outra temperatura? (s/n): ")
print("Obrigado por usar o conversor de temperatura!")