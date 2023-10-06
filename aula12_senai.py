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

### METODO DIFFERENCE
# conjunto1={'value0','Value'}
# conjunto2={'value1','Value2'}
# print(conjunto1.difference(conjunto2))
# print(f'No conjunto 1 tem {conjunto2.difference(conjunto1)}, esses não tem no conjunto2')

# ### METODO UNIAO
# print('união')
# uniao = conjunto1.union(conjunto2)
# print(f'Os 2 conjuntos unidos: {uniao}\n')

# ### TRANSFORMANDO EM LISTA
# print('lista')
# lista = list(conjunto1)
# print(lista, '\n')

# ### TRANSFORMANDO LISTA EM CONJUNTO
# print('conjunto')
# lista4=[1,2,3,4,5,88]
# conjunto=set(lista4)
# print(conjunto)

### EXERCICIOS

### 1: **Transforme uma lista em um conjunto**
# # Criar uma lista
# lista = [1, 2, 3, 4, 5]
# # Transformar a lista em um conjunto
# conjunto1 = set(lista)
# # Imprimir o conjunto
# print('conjunto1:', conjunto1)


### 2: **Una estes 2 conjuntos:**
# zone = {1, 2, 3, 4}
# kwia = {3, 4, 5, 6}
# print('união')
# uniao = zone.union(kwia)
# print(uniao)

### 3: **Verifique a diferença entre os conjuntos:**
# g1 = {12,3569,1,5,7}
# g2 = {12,3569,2,5,8}
# print(g1.difference(g2))
# print(f'No conjunto 1 tem {g1.difference(g2)}, esses não tem no conjunto2')

### 4: Crie um conjunto chamado "frutas" com as seguintes frutas: maçã, banana, laranja, pêra e abacaxi. Em seguida, imprima o número de elementos no conjunto.
# frutas = {'maçã','banana','laranja','pêra','abacaxi'}
# tamanho= len(frutas)
# print(tamanho)

### 5: Crie dois conjuntos, "conjunto1" e "conjunto2",com alguns números inteiros. Imprima a união desses dois conjuntos
# conjunto1 = {1,2,3,4,5,6,7,8,9}
# conjunto2 = {11,22,33,44,55,66,77,88,99}
# uniao = conjunto1.union(conjunto2)
# print(uniao)

### 6: Dado o conjunto "cores" com cores diferentes, remova a cor "vermelho" do conjunto.
# cores = {'Azul','Vermelho','Preto','Rosa'}
# cores.remove('Vermelho')
# print(cores)

### 7: Crie um conjunto chamado "numeros" com os números de 1 a 10. Em seguida, crie um novo conjunto chamado "pares" contendo apenas os números pares do conjunto "numeros".
# numeros = {1,2,3,4,5,6,7,8,9,10}  
# pares = list(filter(lambda x: x % 2 == 0, numeros))
# print(pares)

### 8: Verifique se o conjunto "alunos_aprovados" contém todos os alunos do conjunto "todos_alunos". Os conjuntos devem ser definidos com nomes apropriados.
# alunos_aprovados = {'aluno2','aluno5','aluno3'}
# todos_alunos = {'aluno1','aluno2','aluno3','aluno4','aluno5','aluno6'}
# print(todos_alunos.difference(alunos_aprovados))






