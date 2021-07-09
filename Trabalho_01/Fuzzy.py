#!-*- conding: utf8 -*-
#coding: utf-8

"""
    Aluno: Gabriel Ribeiro Camelo
    Matricula: 401091
"""

import numpy as np

def pressao_freio_baixo(pressao_pedal):#retorna o quao baixa eh a pressao no freio
    pressao_freio = (50-pressao_pedal)/50
    if pressao_freio > 0:
        return pressao_freio
    else:
        return 0

def pressao_freio_medio(pressao_pedal):#retorna o quao medio eh a pressao no freio
    if(pressao_pedal <= 50):
        pressao_freio = (pressao_pedal-30)/20
    elif (pressao_pedal > 50):
        pressao_freio = (70-pressao_pedal)/20
    
    if(pressao_freio < 0):
        return 0
    else:
        return pressao_freio

def pressao_freio_alta(pressao_pedal):#retorna o quao alta eh a pressao no freio
    pressao_freio = (pressao_pedal-50)/50
    if pressao_freio < 0:
        return 0
    else:
        return pressao_freio

def velocidade_baixa(vel):#retorna o quao baixa eh a velocidade da roda ou do carro
    intenc = 1 - vel/60
    
    if intenc < 0:
        return 0
    else:
        return intenc

def velocidade_media(vel):#retorna o quao media eh a velocidade da roda ou do carro
    if(vel <= 50):
        intenc = (vel - 20)/30
    elif (vel > 50):
        intenc = (80 - vel)/30

    if(intenc < 0):
        return 0
    else:
        return intenc

def velocidade_alta(vel):#retorna o quao alta eh a velocidade da roda ou do carro
    intenc = (vel - 40)/60

    if(intenc < 0):
        return 0
    else:
        return intenc

# Regra 01 == pressao_freio_medio, retorna o mesmo valor para aplicar freio

# Regra 02 == retorna o mim(pressao_freio_alta, carro.velocidade_alta, roda.velocidade_alta) para aplicar freio
def Regra02(pressao_pedal, vel_carro, vel_roda):
    pressao_freio = pressao_freio_alta(pressao_pedal)
    intenci_vel_roda = velocidade_alta(vel_roda)
    intenci_vel_carro = velocidade_alta(vel_carro)

    vet_aux = [pressao_freio, intenci_vel_carro, intenci_vel_roda]

    return min(vet_aux)

# Regra 03 == retorna o mim(pressao_freio_alta, carro.velocidade_alta, roda.velocidade_baixa) para liberar freio
def Regra03(pressao_pedal, vel_carro, vel_roda):
    pressao_freio = pressao_freio_alta(pressao_pedal)
    intenci_vel_roda = velocidade_baixa(vel_roda)
    intenci_vel_carro = velocidade_alta(vel_carro)

    vet_aux = [pressao_freio, intenci_vel_carro, intenci_vel_roda]

    return min(vet_aux)
# Regra 04 == pressao_freio_baixa, retorna o mesmo valor para liberar freio

#definindo matematicamente "apertar freio" e "liberar freio"

def myrange(start, end, step):#essa função vai gerar uma lista com os valores que se encontram no intervalo

    while start <= end:
        yield start
        start += step

libera_freio = lambda x: 1 - x/100
libera_freio_t = lambda y: 100*(1 - y)

aperta_freio = lambda x: x/100
aperta_freio_t = lambda y: y*100

multxy = lambda x,y: x*y# se for duas listas ele vai multiplicar o 1º da lista x com o 1º da lista y e assim por diante

def centroide(limite_lib, limite_apt):
    if limite_apt > limite_lib:
        #valores de x q estão para o limite inferior Pa(x)*x
        c1 = sum(myrange(0,libera_freio_t(limite_lib),1)) * limite_lib
        #valores de x q estão para o limite superior
        mapa01 = list(myrange(aperta_freio_t(limite_lib), aperta_freio_t(limite_apt), 1))
        mapa02 = list(map(aperta_freio, mapa01))#Pa(x) para o limite superior
        c2 = list(map(multxy, mapa01, mapa02))#Pa(x)*x

        c = c1 + sum(c2)
        # print(c)
        cd = sum(mapa02)
        # print(cd)
        return c/cd
    else:
        c1 = sum(myrange(0, aperta_freio_t(limite_apt), 1)) * limite_apt

        mapa01 = list(myrange(libera_freio_t(limite_apt), libera_freio_t(limite_lib), 1))
        mapa02 = list(map(libera_freio, mapa01))
        c2 = list(map(multxy, mapa01, mapa02))

        c = c1 + sum(c2)
        cd = sum(mapa02)

        return c/cd

def main():
    pressao_pedal = float(input("pressão do pedal: "))

    vel_roda = float(input("velocidade da roda: "))

    vel_carro = float(input("velocidade do carro: "))

    regra01 = pressao_freio_medio(pressao_pedal)
    regra02 = Regra02(pressao_pedal, vel_carro, vel_roda)
    regra03 = Regra03(pressao_pedal, vel_carro, vel_roda)
    regra04 = pressao_freio_baixo(pressao_pedal)

    #limite para liberar freio somo regra 3 com regra 4
    limite_lib_fr = regra03 + regra04
    #limite para aplicar o freio somo regra 1 e regra 2
    limite_apt_fr = regra01 + regra02

    # print("liberar o freio: ", limite_lib_fr)
    # print("apertar o freio: ", limite_apt_fr)

    c = centroide(limite_lib_fr, limite_apt_fr)

    print("\n", c)

main()

