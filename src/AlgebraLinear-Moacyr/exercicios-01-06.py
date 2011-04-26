# -*- coding:utf-8 -*-
from sympy import pprint
from sympy import Symbol
from sympy.matrices import *
from random import *
import sys
sys.displayhook(pprint)
import time
import numpy as np
import matplotlib.pyplot as plt


print '''
****************************************************************************
6. Estime a complexidade do algoritmo de solução de sistemas lineares do pacote computacional de sua
preferência: registre os tempos que o pacote levou para resolver sistemas aleatórios nxn, com n =
16; 32; 64; 128; 256; 512; 1024; 2048. Faça um gráfico do log do número de colunas contra o log dos tempos
registrados. O algoritmo do pacote tem complexidade inferior a O(nˆ3)?
'''

def random_ints(num, lower=-100, upper=100):
    return [randrange(lower,upper+1) for i in range(num)]

def geraMatriz(n, l=-100, u=100):
    return Matrix(n, n, random_ints(n**2, l, u))

tempoGeracao = {}
tempoDeterminante = {}
for n in range(4,12):
    
    ''' Contagem de tempo para criação das matrizes '''
    t0 = time.time()
    A = geraMatriz(2**n,-100,100)
    tt = time.time() - t0
    tempoGeracao[2**n] = tt
    print "Tempo de geração das matrizes:"
    print tempoGeracao 

    ''' Contagem de tempo para cálculo do determinante '''
    t0 = time.time()
    detA = A.det()
    tt = time.time() - t0
    tempoDeterminante[2**n] = tt
    print "Tempo de cálculo dos determinantes:"
    print tempoDeterminante 
    
plt.plot(tempoGeracao.keys(),tempoGeracao.values())
plt.plot(tempoDeterminante.keys(),tempoDeterminante.values(), "r")
plt.yscale('log')

plt.show()
