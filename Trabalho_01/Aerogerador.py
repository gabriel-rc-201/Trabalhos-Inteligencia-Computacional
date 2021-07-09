
#!-*- conding: utf8 -*-
#coding: utf-8
"""
    Aluno: Gabriel Ribeiro Camelo
    Matricula: 401091
"""

import matplotlib.pyplot as plt
import re
import numpy as np

def mat_x(x, grau):# matriz de valores x
    kx = np.ones((len(x), grau+1))

    for i in range(len(x)):
        for j in range(1, grau+1):
            kx[i][j] = x[i]**j

    return kx

def mat_y(y):# matriz de valores y
    ky = np.ones((len(y), 1))

    for i in range(len(y)):
        ky[i][0] = y[i]

    return ky

subxy = lambda x,y: x-y
multxy = lambda x,y: x*y

def somaYy(y):
    #cria o somatorio de yy
    acumulador = 0
    y_media = np.sum(y)/len(y)
    for k in range(len(y)):
        acumulador += (y[k] - y_media)**2
    return acumulador

def main():
    arq = open("aerogerador.dat", "r") # abre o arquivo que contem os dados

    x = []
    y = []

    for line in arq:                  # separa x de y
        line = line.strip()           # quebra no \n
        line = re.sub('\s+',',',line) # trocando espaços vazios por virgula
        X,Y = line.split(",")         # quebra nas virgulas e retorna 2 valores

        x.append(float(X))
        y.append(float(Y))
    arq.close() # fecha o arquivo que contem os dados

    grau = int(input("Grau do polinomio: "))

    kx = mat_x(x, grau)
    ky = mat_y(y)

    Betah = (np.linalg.inv(np.transpose(kx)@kx))@np.transpose(kx)@ky

    yl = kx@Betah#y linha

    erro = ky - yl

    somaQe = sum(map(multxy, list(map(subxy, y,yl)), list(map(subxy, y,yl))))

    R2 = 1 - (somaQe/somaYy(y))
    R2aj = 1 - ((somaQe/(len(x) - (grau + 1)))/(somaYy(y)/(len(x) - 1)))

    print("R2: ", R2)

    print("R2 ajustado: ", R2aj)

    plt.plot(x,yl, color ='red')
    plt.scatter(x, y, marker = "*")
    plt.show()

main()
