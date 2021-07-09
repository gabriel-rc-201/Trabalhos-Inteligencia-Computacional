
#!-*- conding: utf8 -*-
#coding: utf-8

"""
    Aluno: Gabriel Ribeiro Camelo
    Matricula: 401091
"""
import math # Matemática
import re   # expressões regulares

# Funções acessórias
#calcula a distancia entre os pontos
dist = lambda x1, y1, z1, w1 , x2, y2, z2, w2: math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2 + (w2-w1)**2)

# coleta de dados dos arquivos
arq = open("iris_log.dat")

a1 = []
a2 = []
a3 = []
a4 = []

c1 = []
c2 = []
c3 = []

for line in arq:
    line = line.strip()
    line = re.sub('\s+', '_', line)
    A1, A2, A3, A4, C1, C2, C3 = line.split("_")
    a1.append(float(A1))
    a2.append(float(A2))
    a3.append(float(A3))
    a4.append(float(A4))
    c1.append(float(C1))
    c2.append(float(C2))
    c3.append(float(C3))

arq.close()

# Organização dos dados
# atributos
atributos = []
atributos.append(a1)
atributos.append(a2)
atributos.append(a3)
atributos.append(a4)

# Classes
classes = []
classes.append(c1)
classes.append(c2)
classes.append(c3)

# Pergunta ao usuario as caracteristicas da flor desconhecida
print("Caracteristica da flor desconhecida:")
carac1 = float(input("caracteristica 1: "))
carac2 = float(input("caracteristica 2: "))
carac3 = float(input("caracteristica 3: "))
carac4 = float(input("caracteristica 4: "))

# Pergunta K, quantidade de vizinhos proximo
K = int(input("insira o valor de K(quantidade de vizinhos proximo): "))

qtd = 0
while True:
    # print(K)
    # acumula as distancias para cada elemento
    distancias = []
    for j in range(150):
        # print("atributos[0][",j,"] =",  atributos[0][j])
        # print("atributos[1][",j,"] =",  atributos[1][j])
        # print("atributos[2][",j,"] =",  atributos[2][j])
        # print("atributos[3][",j,"] =",  atributos[3][j])
        d = dist(carac1, carac2, carac3, carac4, atributos[0][j], atributos[1][j], atributos[2][j], atributos[3][j])

        distancias.append(d)

    # Organiza do menor para o maior
    drank = sorted(distancias)

    ir = [] # indice dos K mais ranqueados
    for i in range(K):
        ir.append(distancias.index(drank[i])) # o indice no caso corresponde a coluna
    # Conta quantos elementos de cada classe tem próximo ao elemento desconhecido
    acl1 = 0 # acumulador classe 1
    acl2 = 0 # acumulador classe 2
    acl3 = 0 # acumulador classe 3
    for i in ir: # coluna
        for j in range(3): # linha
            if classes[j][i] == 1:
                if j == 0:
                    acl1 += 1
                elif j == 1:
                    acl2 += 1
                elif j == 2:
                    acl3 += 1

    # Verifica se ocorreu empate entre as classes
    qtd = [acl1, acl2, acl3]
    equals = 0
    print(qtd)
    maior = max(qtd)
    for i in qtd:
        if i == maior:
            equals += 1 # se não ocorrer empate equals == 1
    if equals == 1:
        classeDesconhecida = qtd.index(maior) + 1
        print("Aparentemente essa flor pertence a classe: ", classeDesconhecida)
        print("com um probabilidade de:", acl1/K, "para a classe 1")
        print("com um probabilidade de:", acl2/K, "para a classe 2")
        print("com um probabilidade de:", acl3/K, "para a classe 3")
        break
    else:
        print("deu empate\nvamos tentar com menos vizinhos")
        K -= 1
    if K < 1:
        print("Não há registro dessa planta!!!")
        break
