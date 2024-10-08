"""## Aumento salário funcionário
Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
15%.
"""
## Cálculo da Distância
dist = float(input("Digite a distância a percorrer: \n"))
if dist <= 200:
    valor = dist * 0.50
else:
    valor = dist * 0.35

print(f"O preço da passagem é: R$ {valor:.2f}")

# Aumento salário funcionário
salario = float(input("Informe seu salário: \n"))

if salario <= 1250:
    aumento = salario * 0.15
else:
    aumento = salario * 0.10
print(f"Seu aumento será de: R$ {aumento:.2f}")
