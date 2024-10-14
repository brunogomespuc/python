#importando uma biblioteca
import math

# Lista dos comandos mais utilizados no Python

# Imprime uma mensagem na tela
print("Olá, mundo!")

# Declaração de variáveis
x = 10
y = 5.5
nome = "Python"

# Estruturas de controle de fluxo
if x > y:
    print("x é maior que y")
else:
    print("x não é maior que y")

# Laço de repetição for
for i in range(5):
    print(i)

# Laço de repetição while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Definição de funções
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Mundo"))

# Listas
lista = [1, 2, 3, 4, 5]
print(lista)

# Dicionários
dicionario = {"nome": "Python", "idade": 30}
print(dicionario)

# Manipulação de arquivos
with open("arquivo.txt", "w") as arquivo:
    arquivo.write("Escrevendo no arquivo")

# Importação de módulos
print(math.sqrt(16))