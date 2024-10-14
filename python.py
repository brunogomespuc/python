#importando as bibliotecas
import math
from functools import reduce
import re
import numpy as np

## Lista dos comandos básicos mais utilizados no Python

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

## Comandos mais avançados em Python

# Compreensão de listas
quadrados = [x**2 for x in range(10)]
print(quadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Funções lambda
dobro = lambda x: x * 2
print(dobro(5))  # 10

# Funções map, filter e reduce

numeros = [1, 2, 3, 4, 5]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)  # [2, 4, 6, 8, 10]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]

soma = reduce(lambda x, y: x + y, numeros)
print(soma)  # 15

# Expressões regulares

texto = "O número de telefone é 123-456-7890"
padrao = re.compile(r'\d{3}-\d{3}-\d{4}')
resultado = padrao.search(texto)
print(resultado.group())  # 123-456-7890

# Tratamento de exceções
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero")

# Decoradores
def meu_decorador(func):
    def wrapper():
        print("Algo está acontecendo antes da função ser chamada.")
        func()
        print("Algo está acontecendo depois da função ser chamada.")
    return wrapper

@meu_decorador
def diz_oi():
    print("Oi!")

diz_oi()

# Geradores
def meu_gerador():
    for i in range(5):
        yield i

for valor in meu_gerador():
    print(valor)  # 0 1 2 3 4


## comandos básicos da bliblioteca numpy

# Criação de arrays
array = np.array([1, 2, 3, 4, 5])
print(array)  # [1 2 3 4 5]

# Criação de arrays com valores zeros
zeros = np.zeros(5)
print(zeros)  # [0. 0. 0. 0. 0.]

# Criação de arrays com valores uns
ones = np.ones(5)
print(ones)  # [1. 1. 1. 1. 1.]

# Criação de arrays com valores aleatórios
random = np.random.random(5)
print(random)  # [0.5488135  0.71518937 0.60276338 0.54488318 0.4236548 ]

# Operações aritméticas em arrays
soma = array + 5
print(soma)  # [ 6  7  8  9 10]

multiplicacao = array * 2
print(multiplicacao)  # [ 2  4  6  8 10]

# Funções estatísticas
media = np.mean(array)
print(media)  # 3.0

desvio_padrao = np.std(array)
print(desvio_padrao)  # 1.4142135623730951

# Indexação e fatiamento
print(array[0])  # 1
print(array[1:4])  # [2 3 4]

# Matrizes
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)
# [[1 2 3]
#  [4 5 6]]

# Produto de matrizes
produto = np.dot(matriz, matriz.T)
print(produto)
# [[14 32]
#  [32 77]]