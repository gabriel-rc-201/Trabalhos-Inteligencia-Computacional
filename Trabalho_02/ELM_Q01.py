
#!-*- conding: utf8 -*-
#coding: utf-8

"""
    Aluno: Gabriel Ribeiro Camelo
    Matricula: 401091
"""

import matplotlib.pyplot as pplt # gráficos
import math                      # Matemática
import re                        # expressões regulares
import numpy as np               # matrizes
from statistics import pstdev    # Desvio padrão
from scipy import stats          # Contem o zscore
#Funções para o calculo do R2
subxy = lambda x,y: x-y
multxy = lambda x,y: x*y

def somaYy(y):
    #cria o somatorio de yy
    acumulador = 0
    y_media = np.sum(y)/len(y)
    for k in range(len(y)):
        acumulador += (y[k] - y_media)**2

    return acumulador

# Coleta de dados
arq = open("aerogerador.dat", "r") # abre o arquivo que contem os dados

x = [] # Dados
y = [] # Resultados

for line in arq:                  # separa x de y
    line = line.strip()           # quebra no \n
    line = re.sub('\s+',',',line) # trocando espaços vazios por virgula
    X,Y = line.split(",")         # quebra nas virgulas e retorna 2 valores

    x.append(float(X))
    y.append(float(Y))
arq.close() # fecha o arquivo que contem os dados

# Normalização Zscore
xn = stats.zscore(x)
#adicionando o peso que pondera o bias
xb = []
for i in range(2250):
    xb.append(-1)

X = np.matrix([xb, xn]) # Matriz de dados com o bias

# Matriz de pesos aleatórios
def matPesos (qtdNeuronios, qtdAtributos):
    # retorna uma matriz de numeros aleatórios de uma distribuição narmal
    w = np.random.randn(qtdNeuronios, qtdAtributos+1)
    return w

Neuronios = int(input("Quantidade de Neuronios: "))
W = matPesos(Neuronios, 1)

# Função de Ativação
phi = lambda u: (1 - math.exp(u))/(1 + math.exp(u)) #Logistica

# Ativação dos Neuronios
U = np.array(W@X)

Z = list(map(phi, [valor for linha in U for valor in linha]))
Z = np.array(Z)
Z = Z.reshape(Neuronios, 2250)

# Matriz de pesos dos neuronios da camada de saida
M = (y@Z.T) @ np.linalg.inv(Z@Z.T)

# Ativação dos neuronios de saida
D = M@Z

# Calculo do R2

somaQe = sum(map(multxy, list(map(subxy, y, D)), list(map(subxy, y, D))))

R2 = 1 - (somaQe/somaYy(y))

#Resultados
print("R2: ", R2)

#gráfico
pplt.plot(x, D, color ='red')
pplt.scatter(x, y, marker = "*")
pplt.show()
