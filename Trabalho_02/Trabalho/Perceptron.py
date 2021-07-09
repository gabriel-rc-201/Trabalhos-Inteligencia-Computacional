
#!-*- conding: utf8 -*-
#coding: utf-8

"""
ativação do perceptron == produto escalar entre
                          o vetor de entrada e o
                          vetor de pesos

Erro entre a saída desejada (d) e a saída gerada pela rede (y):
e = d-y

w(t+1) = w(t) + ne(t)x(t)
n -> passo de aprendizado 0 < n << 1

função de ativação: função degrao sai 0 ou 1
                    y = 1 se u >= 0
                    y = 0 se u < 0

    Aluno: Gabriel Ribeiro Camelo
    Matricula: 401091
"""
import math             # Matemática
import re               # Expressões regulares
import numpy as np      # Matrizes
import random           # aleatório
from scipy import stats # Contem o zscore

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

# Bias
xbtr = []
for i in range(40):
    xbtr.append(-1)

xbtt = []
for i in range(10):
    xbtt.append(-1)

# Atributos
# Treino
# Atributos correspondente a classe 1 treino

at1tr = [xbtr, a1[:40], a2[:40], a3[:40], a4[:40]]
# Atributos correspondente a classe 2 treino
at2tr = [xbtr, a1[50:90], a2[50:90], a3[50:90], a4[50:90]]
# Atributos correspondente a classe 3 treino
at3tr = [xbtr, a1[100:140], a2[100:140], a3[100:140], a4[100:140]]

# Teste
# Atributo classe 1 teste
a1tt = [xbtt, a1[40:50], a2[40:50], a3[40:50], a4[40:50]]
# Atributo classe 2 teste
a2tt = [xbtt, a1[90:100], a2[90:100], a3[90:100], a4[90:100]]
# Atributo classe 3 teste
a3tt = [xbtt, a1[140:150], a2[140:150], a3[140:150], a4[140:150]]

# Classes
# Treino
# Classe 1 treino
c1tr = [c1[:40], c2[:40], c3[:40]]
# Classe 2 treino
c2tr = [c1[50:90],c2[50:90], c3[50:90]]
# Classe 3 treino
c3tr = [c1[100:140],c2[100:140], c3[100:140]]

# Teste
# Classe 1 teste
c1tt = [c1[40:50], c2[40:50], c3[40:50]]
# Classe 2 teste
c2tt = [c1[90:100], c2[90:100], c3[90:100]]
# Classe 3 teste
c3tt = [c1[140:150], c2[140:150], c3[140:150]]

# Matrizes Respostas D
D1 = np.matrix(c1tr) # Matriz Resposta 1 correspondente a classe 1 (3x40)
D2 = np.matrix(c2tr) # Matriz Resposta 2 correspondente a classe 2 (3x40)
D3 = np.matrix(c3tr) # Matriz Resposta 3 correspondente a classe 3 (3x40)

"""
3 classes 3 neuronios de saida
4 atributos

dimenssões de W: 4 linhas (uma para cada atributo) 3 colunas (1 para cada neuronio)
Matriz X:
    vão ser 3 matriz x 1 para cada classe
    dimenssões: 4 linhas (uma para cada atributo) 40 colunas (1 para cada neuronio)
"""

W = np.zeros((5,3))                # Matriz de pesso começa distribuição aleatória normal 5x3
X1 = stats.zscore(np.array(at1tr)) # Matriz entrada X1 correspondente aos atributos de classe 1 5x40 Normalizado
X2 = stats.zscore(np.array(at2tr)) # Matriz entrada X2 correspondente aos atributos de classe 2 5x40 Normalizado
X3 = stats.zscore(np.array(at3tr)) # Matriz entrada X3 correspondente aos atributos de classe 3 5x40 Normalizado

# Função de ativação
ativacao = lambda u: 1 if u >= 0 else 0 #retorna 1 se u >= 0 ou 0 caso contrario

for i in range(79): # 79 epocas
    U1 = np.array(X1.T@W)
    Y1 = list(map(ativacao, [valor for linha in U1 for valor in linha]))
    Y1 = np.array(Y1)
    Y1 = Y1.reshape(40, 3) # Resposta gerada pela rede Y1 40x3

    U2 = np.array(X2.T@W)
    Y2 = list(map(ativacao, [valor for linha in U2 for valor in linha]))
    Y2 = np.array(Y2)
    Y2 = Y2.reshape(40, 3) # Resposta gerada pela rede Y2 40x3

    U3 = np.array(X3.T@W)
    Y3 = list(map(ativacao, [valor for linha in U3 for valor in linha]))
    Y3 = np.array(Y3)
    Y3 = Y3.reshape(40, 3) # Resposta gerada pela rede Y3 40x3

    # Erros:
    E1 = D1 - Y1.T # Matriz de Erro corresponde a classe 1 3x40
    E2 = D2 - Y2.T # Matriz de Erro corresponde a classe 2 3x40
    E3 = D3 - Y3.T # Matriz de Erro corresponde a classe 3 3x40

    # Correção do W: w(t+1) = w(t) + ne(t)x(t)
    W = W + 0.05*(E1@X1.T + E2@X2.T + E3@X3.T).T

# Teste pós treino

X1 = stats.zscore(np.matrix(a1tt)) # Matriz entrada X1 correspondente aos atributos de classe 1 5x10 Normalizado
X2 = stats.zscore(np.matrix(a2tt)) # Matriz entrada X2 correspondente aos atributos de classe 2 5x10 Normalizado
X3 = stats.zscore(np.matrix(a3tt)) # Matriz entrada X3 correspondente aos atributos de classe 3 5x10 Normalizado

U1 = np.array(X1.T@W)
Y1 = list(map(ativacao, [valor for linha in U1 for valor in linha]))
Y1 = np.array(Y1)
Y1 = Y1.reshape(10, 3) # Resposta gerada pela rede Y1 10x3

U2 = np.array(X2.T@W)
Y2 = list(map(ativacao, [valor for linha in U2 for valor in linha]))
Y2 = np.array(Y2)
Y2 = Y2.reshape(10, 3) # Resposta gerada pela rede Y2 10x3

U3 = np.array(X3.T@W)
Y3 = list(map(ativacao, [valor for linha in U3 for valor in linha]))
Y3 = np.array(Y3)
Y3 = Y3.reshape(10, 3) # Resposta gerada pela rede Y3 10x3

print(Y1)
print(Y2)
print(Y3)
