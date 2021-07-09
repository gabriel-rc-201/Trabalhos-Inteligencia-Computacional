
#!-*- conding: utf8 -*-
#coding: utf-8
"""
    Aluno: Gabriel Ribeiro Camelo
    Matricula: 401091
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances as dist
from re import sub

arq = open("twomoons.dat")

Xtm = [] # X das duas luas
Ytm = [] # Y das duas luas
Ztm = [] # Z das duas luas

for line in arq:
    line = line.strip()
    line = sub('\s','_',line)
    x,y,z = line.split("_")
    Xtm.append(float(x))
    Ytm.append(float(y))
    Ztm.append(float(z))
arq.close()

dados = np.array([Xtm, Ytm, Ztm]).T
dados_permutados = np.random.permutation(dados).T

# Separo as duas luas para serem plotadas de cores diferentes
Xm1 = Xtm[:501] # X da primeira lua
Ym1 = Ytm[:501] # Y da primeira lua
Zm1 = Ztm[:501] # Z da primeira lua

Xm2 = Xtm[501:] # X da segunda lua
Ym2 = Ytm[501:] # Y da segunda lua
Zm2 = Ztm[501:] # Z da segunda lua

# transformando a minha base de dados de listas para arrays numpy
Xtm = dados_permutados[0]
Ytm = dados_permutados[1]
Ztm = dados_permutados[2]

Xm1 = np.array(Xm1)
Ym1 = np.array(Ym1)
Zm1 = np.array(Zm1)

Xm2 = np.array(Xm2)
Ym2 = np.array(Ym2)
Zm2 = np.array(Zm2)

# Encontrando os centros
TM = np.array([Xtm, Ytm]).T # Coordenadas Duas Luas
qc = int(input("quantidade de centros(minimo 2): ")) # Quantidade de Centros

t = KMeans(n_clusters = qc).fit(TM).cluster_centers_ # t = centros/clusters

# definindo a largura dos raios dos clusters
def secmin(numbers):
    m1, m2 = float('inf'), float('inf')
    for x in numbers:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

dists = list(map(secmin, dist(t,t))) # dist calcula a distancia entre cada cluster
                                     # visto q a menor distancia é a distancia
                                     # entre o ponto e ele mesmo, pega-se a segunda menor distancia
                                     # e armazena-as em uma lista
sigma = sum(dists)/len(dists) # sigma == raio de cada cluster

# Calcular a distancia de cada ponto a cada centro e pegar menor para cada ponto
v = dist(TM, t) # v == ||pontos - clusters||

# Funçã de ativação
f = lambda v: np.exp(-(v**2)/2*(sigma)**2) # gaussiana

# Saida da camada oculta
saida_oculta = f(v).T

# Pesos da camada de saida
Z = Ztm.reshape(1,1001)
W = (Z@saida_oculta.T) @ np.linalg.inv(saida_oculta@saida_oculta.T)

# O vetor da saida ocuta tem dimenssão 1001x1
# W tem dimenssão 1 x quantidade de centros
# O vetor de saida da rede tem dimenssão 1001x1

# Criação da superficie separadoras
intervalo_teste = 8 * np.random.random_sample((10000,2)) #cria uma matriz 10000x2 com numeros aleatórios entre 0 e 8
v_teste = dist(intervalo_teste, t)
saida_teste = f(v_teste).T

resp_test = (W@saida_teste).T
duvidas = []
for i in range(len(resp_test)):
    if (-0.04 <= resp_test[i]) and (resp_test[i] <= 0.04):
        duvidas.append(intervalo_teste[i])

duvidas = np.array(duvidas).T
print(np.shape(duvidas))
X = duvidas[0]
Y = duvidas[1]

# Plot dos gráficos
plt.scatter(X,Y,marker = "o", color = "black")
plt.scatter(Xm1, Ym1, marker = "*")
plt.scatter(Xm2, Ym2, marker = "*", color = "red")
plt.title("Com " +  str(qc) + " Nucleos")

plt.show()
