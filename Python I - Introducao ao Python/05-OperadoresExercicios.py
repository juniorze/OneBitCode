
"""
Antecessor e Sucessor de um número
Escreva um programa em Python que leia um número e represente o número antecessor 
e sucessor desse número que foi lido, utilizando operadores de atribuição
"""
number = int(input("Digite um número\n"))

print(f"Antecessor do número: {number -1} | Sucessor do número: {number +1}")

"""
Média de 4 notas
Escreva um programa em Python que leia quatro números e calcule a média entre esses números
"""
note1 = float(input("Digite a nota 1\n"))
note2 = float(input("Digite a nota 2\n"))
note3 = float(input("Digite a nota 3\n"))
note4 = float(input("Digite a nota 4\n"))

average = (note1 + note2 + note3 + note4) /4

print(f"Médias das notas é: {average:.2f}")