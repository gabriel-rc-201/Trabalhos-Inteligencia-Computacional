
#!-*- conding: utf8 -*-
#coding: utf-8
"""
    Aluno: Gabriel Ribeiro Camelo
    Matricula: 401091
"""
import math
from random import randint, uniform

f = lambda x,y: abs(x*math.sin(y*math.pi/4) + y*math.sin(x*math.pi/4))

# Dados a serem observados
maiores_notas = [] # maiores notas de cada geração
maiores_individuos = [] # coordenadas dos individuos com as maiores notas
mutacoes = 0 # quantidade de mutações ao longo das gerações
GMut = [] # Gerações que ocorreram mutações
# Individuos
individuos = [] # lista de individuos
ind = '' # cromossomo

print("Valor par, please!!!")
quant_ind = int(input("Quantos individuos a vasculhar o território?: "))

for i in range(quant_ind):# salva os individuos no array individuo
    for j in range(20):
        ind += str(randint(0,1))
    individuos.append(ind)
    ind = ''

geracoes = int(input("Quantas gerações tu queres?: "))
taxa_mutacao = float(input("Definas a taxa de mutação: "))
# Iniciando algorítimo genético
for geracao in range(geracoes):
    # nota de cada individuo
    print("\n\n\tGERAÇÃO ", geracao)
    print("Notas:")

    coordenadas = []
    notas = []
    for i in range(quant_ind):
        x = 20/(2**10 - 1) * int(individuos[i][:10], 2)
        y = 20/(2**10 - 1) * int(individuos[i][10:], 2)
        nota = f(x,y)

        print("individuo {} nota: {}".format(i,nota))
        coordenadas.append((x,y))
        notas.append(nota)

    print("\nGeração: ", geracao)
    index_maior = notas.index(max(notas))
    print("Maior nota: {}\nIndividuo: {} ({}), coordenadas = {}".format(max(notas), index_maior,individuos[index_maior], coordenadas[index_maior]))
    maiores_individuos.append(coordenadas[index_maior])
    maiores_notas.append(max(notas))
    # Roleta

    # cada individuo vai ter o seu par seguido dele 0 e 1, primeiro par
    pares = [] # 2 e 3 segundo par 4 e 5 o seguinte, e assim por diante

    soma = sum(notas)

    for i in range(quant_ind):
        s = uniform(0, soma) # numero float aleatorio entre [0, soma]

        j = 0
        aux = notas[0]

        while aux < s:
            j += 1
            aux += notas[j]
        pares.append(individuos[i])
    # Operação de Crossover

    individuos.clear()
    for i in range(0,quant_ind,2):
        corte = randint(0,18) # 18 pois os indices variam no intervalo [0,19]
        filho1 = pares[i][:corte] + pares[i+1][corte:]
        filho2 = pares[i+1][:corte] + pares[i][corte:]

        individuos.append(filho1)
        individuos.append(filho2)

    pares = []
    # Mutação
    quant_mut_ger = 0 # quantidade de mutações que ocorreram na geração
    for i in range(quant_ind): # testa para cada individuo
        if uniform(0, 100) < taxa_mutacao: # probabilidade do individuo i de sofrer a mutação definida pelo usuario
            print("Ocorreu mutação no individuo", i)
            quant_mut_ger += 1
            mutacoes += 1

            if quant_mut_ger == 1:
                GMut.append(geracao)

            bit = randint(0,19) # bit que vai sofrer a mutação
            if individuos[i][bit] == '1':
                individuos[i] = individuos[i][:bit] + '0' + individuos[i][bit+1:]
            elif individuos[i][bit] == '0':
                individuos[i] = individuos[i][:bit] + '1' + individuos[i][bit+1:]

index_maior = maiores_notas.index(max(maiores_notas))

print("\n\nCom {} individuos".format(quant_ind))
print("Com {} gerções".format(geracoes))
print("Com taxe de mutação de {}%".format(taxa_mutacao))
print("A maior nota foi de {} na geração {} com as coordenadas {}\n\n".format(max(maiores_notas), index_maior, maiores_individuos[index_maior]))

if mutacoes != 0: # Se ocorrer alguma mutação ele informa:
    print("Ocoreram {} mutações".format(mutacoes)) # quantidade de mutações que ocorreram ao longo das gerações
    print("Em {} gerações".format(len(GMut)))
    r = 'n'
    r = input("Deseja saber em quais gerações ocorreram mutação? (S/n): ")
    if r == 'S' or r == 's':
        print("Nas gerações: {}".format(GMut)) # em quais gerações ocorreram mutação
