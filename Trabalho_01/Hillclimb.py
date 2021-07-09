#!-*- conding: utf8 -*-
#coding: utf-8
"""
    Aluno: Gabriel Ribeiro Camelo
    Matricula: 401091
"""
from random import randint
import math

#valores iniciais de x e y
xi = randint(0,20)
yi = randint(0,20)

#função problema
f = lambda x,y: abs(x*math.sin(y*math.pi/4) + y*math.sin(x*math.pi/4))

def vizinhos(x, y):
    vizinho = []#pontos vizinhos ao meu ponto atual

    v1 = (x+0.01, y)
    vizinho.append(v1)

    v2 = (x-0.01, y)
    vizinho.append(v2)
    
    v3 = (x, y+0.01)
    vizinho.append(v3)
    
    v4 = (x, y-0.01)
    vizinho.append(v4)
    
    v5 = (x+0.01, y+0.01)
    vizinho.append(v5)
    
    v6 = (x-0.01, y-0.01)
    vizinho.append(v6)
    
    v7 = (x+0.01, y-0.01)
    vizinho.append(v7)
    
    v8 = (x-0.01, y+0.01)
    vizinho.append(v8)
     
    v9 = (x, y)
    vizinho.append(v9)

    return vizinho
    
def f_vizinho(vizinho):#retorna o indice do maior valor de f do vizinho
    y_vizinho = []#valor de f de cada vizinho
    for i in range(9):
        y_vizinho.append(f(vizinho[i][0],vizinho[i][1]))
    
    return y_vizinho

topo = f(xi, yi)

print("comecou em: ", topo)
print("com x = ", xi)
print("e y = ", yi)
z = 0

while(z < 10000):
    v = vizinhos(xi,yi)

    fv = f_vizinho(v)
    max_fv = max(fv)
    index_mv = fv.index(max_fv)

    #print("index do maior vizinho: ", index_mv)

    if fv[index_mv] > f(xi, yi):
        xi = v[index_mv][0]
        yi = v[index_mv][1]
        topo = f(xi, yi)
    
    z = z + 1
print("terminou em: ", topo)
print("com x = ", xi)
print("e y = ", yi)

# depois de rodar o código algumas vezes
# o maior valor de f encontrado foi 36.08965117434065