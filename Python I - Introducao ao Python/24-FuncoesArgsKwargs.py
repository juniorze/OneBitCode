"""
*args: Utilizamos ele quando não temos a certeza de quantos
argumentos vamos ter dentro de uma função. Ao utilizá-lo, 
deixamos essa informação dinâmica e variável.
- Os argumentos são passados como uma tupla.

**kwargs: Além dos valores, podemos passar também as respectivas
chaves para cada argumento.
- Os argumentos são passados como um dicionário.
"""
def sum(*num):
    sum_total = 0
    
    for n in num:
        sum_total = sum_total + n

    print(f"Soma é: {sum_total}")
sum(7)
sum(8, 7)
sum(4, 5, 9)
sum(6, 8, 3, 1)

def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
print("######Curso######")
presentation(name="Python", category="Backend", level="Iniciante")


"""
Exemplo: Função para calcular a média de notas
Usa *args para aceitar um número variável de notas
"""
def calcular_media(*notas):
    if len(notas) == 0:
        return "Nenhuma nota fornecida"
    
    total = sum(notas)
    media = total / len(notas)
    
    print(f"Notas recebidas: {notas}")
    print(f"Média: {media:.2f}")
    
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Chamadas da função
print(calcular_media(7, 8, 9))
print(calcular_media(5, 6, 7, 8))
print(calcular_media(4, 5))
print(calcular_media())

"""
Exemplo: Função para criar um perfil de usuário
Usa **kwargs para aceitar informações variáveis do usuário
"""
def criar_perfil_usuario(**info):
    if not info:
        return "Nenhuma informação fornecida"
    
    perfil = "Perfil do Usuário:\n"
    for chave, valor in info.items():
        perfil += f"{chave.capitalize()}: {valor}\n"
    
    return perfil

# Chamadas da função
print(criar_perfil_usuario(nome="Alice", idade=30, profissao="Engenheira"))
print(criar_perfil_usuario(nome="Bob", cidade="São Paulo", hobby="Fotografia"))
print(criar_perfil_usuario())