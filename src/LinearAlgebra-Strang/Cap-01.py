# -*- coding:utf-8 -*-
import math as mt
import sympy as sp
import matplotlib.pyplot as mpl

A = sp.Matrix([[1,2],[4,5]])
print A

print '''
Considere as equações:
2x - y = 1
x + y = 5.
'''

print '''
Row form:
'''
A = sp.Matrix([[2,1],[-1,1]])
b = sp.Matrix([[1],[5]])
x1,y1 = sp.Symbol('x'),sp.Symbol("y")
x = sp.Matrix([[x1],[y1]])

print '''
Ax = b:
%s * %s = %s
''' % (str(A), str(x), str(b))

print '''
B) Column form:
'''
x1 * A[:,0] + y1 * A[:,1]
print '''
%s
''' % str(x1 * A[:,0] + y1 * A[:,1])

print '''
Testando operações com matrizes:
'''
x1,y1 = 2,-1

print '''
Res: 
%s''' % str(x1*A[:,0])
