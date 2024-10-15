'''
Exercício 2
Exercicio A - Substituindo caractere repetido
Escreva um programa Python para obter uma string de uma string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere
Ex:
fifa 23 → **fi#a 23**
restart→ resta#t

## Exercicio B - Substituindo os dois primeiros caracteres
Obter uma única string de duas strings fornecidas, separadas por um espaço e troque os dois primeiros caracteres de cada string.
Ex:
abc xyz → **xyc abz**
'''
### Minha Resposta
### Resposta 1
print ("---------------------------------")
palavra1='O rato roeu a roupa do rei de Roma'
palavra2='Tres pratos de trigo para tres tigres tristes'
caractere1 = palavra1[:1].lower()
caractere2 = palavra2[:1].lower()
print(palavra1.replace(caractere1, "$"))
print(palavra2.replace(caractere2, "$"))
print ("---------------------------------")
print ("---------------------------------")
### Solucao do instrutor
name = 'Fifa 23'
character = name[0].lower()
new = name.replace(character, '#')
new = character +  new[1:]
print(new)
print ("---------------------------------")
### Minha Resposta
### Resposta 2
palavra3 = input("Digite duas palavras: ")
divide1, divide2 = palavra3.split(' ')
caso1 = divide1[:2]
caso2 = divide2[:2]
resultado = palavra3.replace(caso1, "##", 1).replace(caso2, caso1, 1).replace("##", caso2, 1)
print(resultado)
print ("---------------------------------")
print ("---------------------------------")
### Solucao do instrutor
st1 = 'abc'
st2 = 'xyz'
new_st1 = st2[:2] + st1[2:]
new_st2 = st1[:2] + st2[2:]
print(f"{new_st1} {new_st2}")