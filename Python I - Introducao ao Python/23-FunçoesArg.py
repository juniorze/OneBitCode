"""
3 -> 3 * 2 * 1
5 -> 5 * 4 * 3 * 2 * 1
"""
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num-1))

number = int(input("Digite o número para fatorial\n"))
print(f"O fatorial de {number} é: {factorial(number)}")

"""
3 -> 3 + 2 + 1
5 -> 5 + 4 + 3 + 2 + 1
"""

def total_sum(num):
    if num == 1:
        return 1
    else:
        return (num + total_sum(num - 1))

num = int(input("Digite um número para soma \n"))
print(f"A soma total do {num} é: {total_sum(num)}")


"""
Exemplo 1: Sequência de Fibonacci
A sequência de Fibonacci é definida como:
F(n) = F(n-1) + F(n-2), onde F(0) = 0 e F(1) = 1
Ex: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Digite o número de termos da sequência de Fibonacci: "))
print(f"O {num}º termo da sequência de Fibonacci é: {fibonacci(num-1)}")

# Imprimindo a sequência
print("Sequência de Fibonacci:")
for i in range(num):
    print(fibonacci(i), end=" ")
print()  # Para pular uma linha no final

"""
Exemplo 2: Potência de um número
Calcula x elevado a n usando recursão
Ex: 2^4 = 2 * 2^3 = 2 * 2 * 2^2 = 2 * 2 * 2 * 2^1 = 2 * 2 * 2 * 2 * 2^0 = 16
"""

def potencia(x, n):
    if n == 0:
        return 1
    else:
        return x * potencia(x, n-1)

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = potencia(base, expoente)
print(f"{base} elevado a {expoente} é: {resultado}")