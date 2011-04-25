# -*- coding:utf-8 -*-
import math as mt
import sympy as sp
import matplotlib.pyplot as mpl
'''
A distância entre dois pontos no plano é
calculada pela fórmula da hipotenusa:
h = sqrt((x1-x2)**1+(y1-y2)**2)
'''
v1 = sp.Matrix([5,6])
v2 = sp.Matrix([2,3])
t = mt.sqrt((v1[0]-v2[0])**2+(v1[1]-v2[1])**2)

print "Distância v1 x v2: %s" % str(t)

'''
Um vetor tem direção, sentido e módulo.
O módulo (tamanho) é a sqrt(x**2+y**2)
'''

t = mt.sqrt(v1[0]**2+v1[1]**2)

print "O módulo do vetor v1 é: %s" % str(t)

print '''A soma de vetores é a soma de seus elementos: v1+v2:
%s''' % str(v1+v2)

print '''A multiplicação de um vetor por um escalar é a 
multiplicação do ecalar pelos elementos: 2*v1
%s ''' % str(2*v1)