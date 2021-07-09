#!-*- conding: utf8 -*-
#coding: utf-8

"""
    Aluno: Gabriel Ribeiro Camelo
    Matricula: 401091
"""
import math # Matemática
import re   # expressões regulares
from numpy import mean

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
# 40 amostra para treino e 10 para teste

# Centroide Classe 1:
cc1 = [mean(a1[:40]), mean(a2[:40]), mean(a3[:40]), mean(a4[:40])]
# Centroide Classe 2
cc2 = [mean(a1[50:90]), mean(a2[50:90]), mean(a3[50:90]), mean(a4[50:90])]
# Centroide Classe 3
cc3 = [mean(a1[100:140]), mean(a2[100:140]), mean(a3[100:140]), mean(a4[100:140])]

# Pergunta ao usuario as caracteristicas da flor desconhecida
print("Caracteristica da flor desconhecida:")
carac1 = float(input("caracteristica 1: "))
carac2 = float(input("caracteristica 2: "))
carac3 = float(input("caracteristica 3: "))
carac4 = float(input("caracteristica 4: "))

# Calcula a distancia em relação ao centroide de cada classe
distancias = []

# distancia em relação a classe 1
d = dist(carac1, carac2, carac3, carac4, cc1[0], cc1[1], cc1[2], cc1[3])
distancias.append(d)

# distancia em relação a classe 2
d = dist(carac1, carac2, carac3, carac4, cc2[0], cc2[1], cc2[2], cc2[3])
distancias.append(d)

# distancia em relação a classe 3
d = dist(carac1, carac2, carac3, carac4, cc2[0], cc2[1], cc2[2], cc2[3])
distancias.append(d)

# Organiza do menor para o maior
maisProx = distancias.index(min(distancias)) + 1

print("A classe mais poxima é:", maisProx)
