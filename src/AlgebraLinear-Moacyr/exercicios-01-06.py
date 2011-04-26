# -*- coding:utf-8 -*-
from sympy import pprint
from sympy import Symbol
from sympy.matrices import *
from random import *
import sys
sys.displayhook(pprint)

print '''
****************************************************************************
6. Estime a complexidade do algoritmo de solução de sistemas lineares do pacote computacional de sua
preferência: registre os tempos que o pacote levou para resolver sistemas aleatórios nxn, com n =
16; 32; 64; 128; 256; 512; 1024; 2048. Faça um gráfico do log do número de colunas contra o log dos tempos
registrados. O algoritmo do pacote tem complexidade inferior a O(nˆ3)?
'''

def random_ints(num, lower=-100, upper=100):
    return [randrange(lower,upper+1) for i in range(num)]

def geraMatriz(n):
    return Matrix(n, n, random_ints(n**2))

A = geraMatriz(5)
print A

A = geraMatriz(6)
print A

A = geraMatriz(7)
print A

