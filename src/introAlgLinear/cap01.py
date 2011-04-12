# -*- coding:utf-8 -*-
''' Importamos o NumPy para operações com matrizes '''
import numpy as np
''' Importamos o sys para tratamento de erros '''
import sys

print '''
Exercícios do Livro Introdução à Álgebra Linear
Pág. 18
'''

A = np.array([[2,0],[6,7]])

print '''Matriz A:
%s
''' % str(A)

B = np.array([[0,4],[2,-8]])

print '''Matriz B: 
%s
''' % str(B)

C = np.array([[-6,9,-7],[7,-3,-2]])

print '''Matriz C: 
%s
''' % str(C)

D = np.array([[-6,4,0],[1,1,4],[-6,0,6]])

print '''Matriz D: 
%s
''' % str(D)

E = np.array([[6,9,-9],[-1,0,-4],[-6,0,-1]])

print '''Matriz E: 
%s
''' % str(E)

print '''ATENÇÃO:
O NumPy não faz multiplicação direta de matrizes com o *
Quando é utilizado * ele funciona como escalar multiplicando
cada elemento de uma matriz pelo elemento da outra (elementwise).
Neste caso, e apenas neste caso, pode-se dizer que o resultado
é comutativo.
*****************************************************************
Exemplos (incorretos de acordo com o exercício):
'''
print '''A*B:
%s
''' % str(A*B)

print '''B*A:
%s
''' % str(B*A)


print '''Resposta exercício 1.1.1 (a) pág. 18
np.dot(A,B) - np.dot(B,A):
%s
''' % str(np.dot(A,B) - np.dot(B,A))


'''
Fazendo um error handler para pegar o erro do exercício (b)
'''
try:
    x = 2*C - D
except:
    x = "Erro: ", sys.exc_info()[0]


print '''Resposta exercício 1.1.1 (b) pág. 18
2C - D:
%s
''' % str(x)


print '''Resposta exercício 1.1.1 (c) pág. 18
(2Dt - 3Et)t:
%s
''' % str((2*D.transpose() - 3*E.transpose()).transpose())


print '''Pelo teorema da transposição da transposição:
(2Dt - 3Et)t = (2*Dt)t - (3Et)t = 2(Dt)t - 3(Dt)t = 2D - 3D
%s
''' % str(2*D - 3*E)


print '''Resposta exercício 1.1.1 (d) pág. 18
D^2 - DE:
%s
''' % str(np.dot(D,D) - np.dot(D,E))


print '''Pelo teorema da distributividade:
D^2 - DE = DD - DE = D(D - E)
%s
''' % str(np.dot(D,(D-E)))








