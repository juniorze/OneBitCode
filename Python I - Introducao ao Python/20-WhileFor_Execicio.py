## Contagem Regressiva
# Faça um programa para escrever a contagem regressiva do lançamento de um foguete. 
# O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”.

#### MINHA SOLUÇÃO ####
# Lançamento Contagem regressiva
import time
import winsound
frequency = 4000
duration = 1500

cont = 11
while (cont != 0):
        cont = cont - 1
        print(cont)
        time.sleep (1)
winsound.Beep(frequency, duration) 


# Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário
#### MINHA SOLUÇÃO ####
# Tabuada
indice = int(input("Informe qual tabuada você quer conferir: \n"))
a = int(input("Informe onde deseja iniciar: \n"))
b = int(input("Informe onde deseja terminar: \n"))
b +=1

print(f"\nTabuada do {indice}:")

for i in range(a, b):
    resultado = indice * i
    print(f"{indice} x {i} = {resultado}")

#### SOLUÇÃO CURSO Instrutor ####
# Lançamento Contagem regressiva
import winsound
x = 10
while x >= 0:
    print(x)
    x = x - 1
winsound.Beep(2500, 500)

# Tabuada
number = int(input("Tabuada de: "))
begin = int(input("De: "))
end = int(input("Até: "))
x = begin
while x <= end:
    print(f"{number} x {x} = {number * x}")
    x = x + 1
