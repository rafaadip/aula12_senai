# n = input("Digite um número: ")
# lista = {1,2,3,4,5}
# quantidade = list(map(lambda x: x ** 2, lista))
# print(quadrado)

# n = (10,20,30)
# lista = [1,2,3,6,2]
# quadrado2 = list(map(lambda numero:numero/12,lista))
# print(quadrado2)
# multiplicacao = lambda a,b: a*b
# print(multiplicacao(10,20))

# numeros = [22,200,20,1,30,31,7,11]
# pares = list(filter(lambda x : x % 2 == 0, numeros))
# print(pares)

### 1 - Crie uma função lambda que retorne o dobro de um número.
# dobro = lambda x : x * 2
# print(dobro(5))

### 2 - Crie uma função lambda que calcule a soma de dois números.
# soma = lambda x,y : x + y
# print(soma(10,20))

### 3 - Crie uma função lambda que verifique se um número é par.
# par = lambda x : x % 2 == 0
# print(par(4))

### 4 - Crie uma função lambda que converta uma string em maiúsculas.
# conversao = lambda s : s.upper()
# print(conversao("Olá Mundo"))

### 5 - Crie uma função lambda que calcule o produto de três números.

# from functools import reduce

# lista = [1,2,3,4,5,6,7]
# produto = reduce(lambda x,y : x * y, lista)
# print(produto)

frutas = {'uva','banana','maçã'}
if 'uva' in frutas:
    print("Tem uva")
else:
    print("Não tem uva")

f = {1,3,5}
g = frutas.union(f)
print(g)

numeros = set[(20,30,5,6,7)]
print(numeros)
conjunto1 = [2,6,4,7]
conjunto2 = [8,56,67,87]
for conjunto1 in conjunto2:
    print(conjunto2)
