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

###### RESPOSTA DO INSTRUTOR ######
## Cálculo da Distância
distance = float(input("Digite a distância a percorrer: "))
if distance <= 200:
    ticket = 0.5 * distance
else:
    ticket = 0.35 * distance
print(f"Preço da passagem: R$ {ticket:.2f}")

## Aumento Salário Funcionário
salary = float(input("Digite seu salário: "))
perc_increase = 0.15
if salary > 1250:
     perc_increase = 0.10
incresase = salary * perc_increase
print(f"Seu aumento será de: R$ {incresase:.2f}")
