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


print '''
---------------------------------------------------------------
Resposta exercício 1.1.1 (a) pág. 18
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


print '''
---------------------------------------------------------------
Exercício 1.1.2:
Conhecendo somente os produtos AB e AC, como podemos calcular:
a) A(B+C)
b) BtAt
c) CtAt
d) (ABA)C
'''

print '''
a) A(B+C)
Pelo princípio da distributividade:
A(B+C) = AB + AC
'''

print '''
b) BtAt
O produto de matrizes transpostas é igual à transposta do inverso de seus produtos:
BtAt = (AB)t
'''

print '''
c) CtAt
O produto de matrizes transpostas é igual à transposta do inverso de seus produtos:
CtAt = (AC)t
'''

print '''
d) (ABA)C
Pela associatividade:
(ABA)C = (AB)(AC)
'''

print '''
---------------------------------------------------------------
Exercício 1.1.3
Considere as seguintes matrizes:
'''

A = np.array([[-3,2,1],[1,2,-1]])
print '''Matriz A:
%s
''' % str(A)

B = np.array([[2,-1],[2,0],[0,3]])
print '''Matriz B:
%s
''' % str(B)

C = np.array([[-2,1,-1],[0,1,1],[-1,0,1]])
print '''Matriz C:
%s
''' % str(C)

D = np.array([[1,0,0],[0,1,0],[0,0,1]])
print '''Matriz D:
%s
''' % str(D)

E1 = np.array([[1],[0],[0]])
print '''Matriz E1:
%s
''' % str(E1)

E2 = np.array([[0],[1],[0]])
print '''Matriz E2:
%s
''' % str(E2)

E3 = np.array([[0],[0],[1]])
print '''Matriz E3:
%s
''' % str(E3)

print '''
Verifique que:
a) AB é diferente de BA
'''

print '''
A * B:
%s
'''% str(np.dot(A,B))

print '''
B * A:
%s
'''% str(np.dot(B,A))


print '''
---------------------------------------------------------------
Exercício 1.1.5
Encontre um valor de x tal que ABt = 0:
'''

A = np.array([1,4,-2])
print '''Matriz A:
%s
''' % str(A)

B = np.array([2,-3,5])
print '''Matriz B:
%s
''' % str(B)

print '''Matriz B transposta:
%s
''' % str(B.transpose())

print '''
A * B = 0
x*2 + 4*(-3) + (-2)*5 = 0
2x - 12 - 10 = 0
2x = 22
x = 11
'''

print '''
Testando resultado (x=11):
'''

A = np.array([11,4,-2])
print '''Matriz A:
%s
''' % str(A)

print '''
ABt = %s
''' % np.dot(A,B.transpose())


print '''
---------------------------------------------------------------
Exercício 1.1.6
Mostre que a matriz A = [[1,1/y],[y,2]] em que y é um número real não nulo
verifica a equação X^2 = 2X
'''
y = 1

A = np.array([[1,1/y],[y,2]])
print '''Matriz A:
%s
''' % str(A)

print '''
Xˆ2 = 2X
Xˆ2 - 2X = 0
X(X-2) = 0
X = 0 e 2
'''

print '''
---------------------------------------------------------------
Capítulo 1.2
---------------------------------------------------------------
Exemplo 1
'''

A = np.array([[1,1,1,1000],[2,1,4,2000],[2,3,5,2500]])
print '''Matriz A:
%s
''' % str(A)

print '''
Subtraíndo duas vezes a primeira linha da segunda linha de A: 
%s 
''' % str((2*A[0])-A[1])

A[1] = (2*A[0])-A[1]

print '''
Substituindo o valor da segunda linha de A pelo resultado e imprimindo A: 
%s 
''' % str(A)

A[2] = A[2]-2*A[0]

print '''
3L -> 3L - 2*1L: 
%s 
''' % str(A)

A[0] = A[0]-A[1]
A[2] = A[2]-A[1]

print '''
Para (1,2) = 0 => 1L -> 1L - 2L
Para (3,2) = 0 => 3L -> 3L - 2L: 
%s 
''' % str(A)

A[2] = A[2]/5

print '''
Para (3,3) = 1 => 3L -> 3L / 5:
%s 
''' % str(A)

A[0] = A[0]-3*A[2]
A[1] = A[1]+2*A[2]

print '''
Para (1,3) = 0 => 1L -> 1L - 3*3L:
Para (2,3) = 0 => 2L -> 2L + 2*3L:
%s 
''' % str(A)


print '''
---------------------------------------------------------------
Capítulo 1.2
---------------------------------------------------------------
Exercício 1.2.3 (pág. 63)

Resolva pelo métido Gauss-Jordan
a)
'''

A = np.array([[1,1,2,8],[-1,-2,3,1],[3,-7,4,10]])
print '''Matriz A:
%s
''' % str(A)

A[1] = A[1]+A[0]
A[2] = A[2]-3*A[0]

print '''
Para (1,2) = 0 => 2L -> 2L + 1L:
Para (1,3) = 0 => 3L -> 3L - 3*1L:
%s 
''' % str(A)

A[1] = A[1]*-1

print '''
Para (2,2) = 1 => 2L -> 2L * -1
%s 
''' % str(A)

A[0] = A[0]-A[1]
A[2] = A[2]+10*A[1]

print '''
Para (1,2) = 0 => 1L -> 1L - 2L
Para (3,2) = 0 => 3L -> 3L + 10*2L
%s 
''' % str(A)

A[2] = A[2]/-52

print '''
Para (3,3) = 1 => 3L -> 3L / -52
%s 
''' % str(A)

A[1] = A[1] + 5*A[2]
A[0] = A[0] - 7*A[2]

print '''
Para (2,3) = 0 => 2L -> 2L + 5*3L
Para (1,3) = 0 => 1L -> 1L - 7*3L
%s 
''' % str(A)


print '''
---------------------------------------------------------------
Capítulo 1.2
---------------------------------------------------------------
Exercício 1.2.3 (pág. 63)

Resolva pelo métido Gauss-Jordan
b)
'''

A = np.array([[2.,2.,2.,0.],[-2.,5.,2.,1.],[8.,1.,4.,-1.]])
print '''Matriz A:
%s
''' % str(A)

A[0] = A[0] / 2
A[1] = A[1] + A[0] *2
A[2] = A[2] - A[0] *8

print '''
Primeiro passo:
%s 
''' % str(A)

A[1] = A[1] / 7
A[0] = A[0] - A[1]
A[2] = A[2] + A[1] * 7

print '''
Segundo passo:
%s 
''' % str(A)

A[2] = A[2] / -4
A[0] = A[0] - A[2]

print '''
Terceiro passo:
%s 
''' % str(A)


print '''
---------------------------------------------------------------
Capítulo 1.2
---------------------------------------------------------------
Exercício 1.2.3 (pág. 64)

Resolva pelo métido Gauss-Jordan
c)
'''

A = np.array([[0.,-2.,3.,1.],[3.,6.,-3.,-2.],[6.,6.,3.,5.]])
print '''Matriz A:
%s
''' % str(A)

''' Trocando a 1L pela 2L '''
A = np.concatenate(([A[1]],[A[0]],[A[2]]),axis=0)

print '''
Trocando L1 com L2
%s 
''' % str(A)

''' Dividindo 1L por 3 '''
A[0] = A[0]/3

print '''
Dividindo 1L por 3
%s 
''' % str(A)

''' Subtraíndo 6*1L da 3L '''
A[2] = A[2] - 6 * A[0]

print '''
Subtraíndo 6*1L da 3L
%s 
''' % str(A)

''' 2L = 2L / -2 '''
A[1] = A[1] / -2

print '''
2L = 2L / -2
%s 
''' % str(A)

''' 1L = 1L - 2*2L '''
A[0] = A[0] - 2*A[1]
''' 3L = 3L + 6*2L '''
A[2] = A[2] + 6*A[1]

print '''
1L = 1L - 2*2L
%s 
''' % str(A)

print "Portanto, de acordo com  última linha, o sistema não tem solução"


print '''
---------------------------------------------------------------
Capítulo 1.2
---------------------------------------------------------------
Exercício 1.2.4 (pág. 64)

Os dois sistemas possuem a mesma matriz A. Resolva-os usando o método de Gauss-Jordan
'''

from sympy import pprint
import sys
sys.displayhook(pprint)
from sympy.matrices import *


A = Matrix([[1,-2,1,1,2],[2,-5,1,-2,-1],[3,-7,2,-1,2]])
print '''Matriz A:
%s
''' % str(A)

'''Zerando (2,1) e (3,1) '''
A[1,:] = A[1,:] - 2 * A[0,:] 
A[2,:] = A[2,:] - 3 * A[0,:] 


print '''
Zerando (2,1) e (3,1)
%s 
''' % str(A)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

''' Inverte L2 '''
A[1,:] = A[1,:] / -1 


print '''
Inverte L2
%s 
''' % str(A)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

'''Zerando (1,2) e (3,2) '''
A[0,:] = A[0,:] + 2 * A[1,:] 
A[2,:] = A[2,:] + A[1,:] 


print '''
Zerando (2,1) e (3,1)
%s 
''' % str(A)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
print '''
Repare a última linha da matriz A:
0x1 + 0x2 + 0x3 + 0x4 = 1

Nem aqui nem na China, né? 

O sistema não tem solução.
'''

print '''
---------------------------------------------------------------
Capítulo 1.2
---------------------------------------------------------------
Exercício 1.2.5 (pág. 64)

Seja A, 
'''

A = Matrix([[1,0,5],[1,1,1],[0,1,-4]])
print '''Matriz A:
%s
''' % str(A)

print '''
a) Encontre a solução geral do sistema (A + 4I3)X = 0
'''

I3 = eye(3)

B = A + 4 * I3

print '''
Resolvendo o parêntesis
B = A + 4 * I3:
B: 
%s ''' % str(B)

''' Vetor zero para que B*X = 0 '''
X = zeros((3,1))

print ''' 
Vetor zeros para que B*X = 0:
X:
%s ''' % str(X)

''' Join de B*X '''
B = B.row_join(X)

print ''' 
Join de B com X:
B:
%s ''' % str(B)

''' Troca L1 com L2 e L2 com L3 '''
B[0,:], B[1,:] = B[1,:], B[0,:]
B[1,:], B[2,:] = B[2,:], B[1,:]

print ''' 
Troca L1 com L2 e nova L2 com L3:
B:
%s ''' % str(B)

''' Zera (3,1) '''
B[2,:] = B[2,:] - 5 * B[0,:]

print ''' 
L3 -> L3 - 5 * L1:
B:
%s ''' % str(B)

''' Zera (1,2) e (3,2) '''
B[0,:] = B[0,:] - 5 * B[1,:]
B[2,:] = B[2,:] + 25 * B[1,:]

print ''' 
L1 -> L1 - 5 * L2
L3 -> L3 + 25 * L2
B:
%s ''' % str(B)

print '''
Portanto:
  x1 = -w
  x2 = 0
  x3 = w
  para todo w pertencente a R
'''

print '''
b) Encontre a solução geral do sistema (A - 2I3)X = 0
'''

I3 = eye(3)
B = A - 2 * I3
X = zeros((3,1))
B = B.row_join(X)

print '''
Matriz B:
%s ''' % str(B)

print ''' 
Troca L1 com L2 e L2 com L3 '''
B[0,:], B[1,:] = B[1,:], B[0,:]
B[1,:], B[2,:] = B[2,:], B[1,:]

print '''Matriz B:
%s ''' % str(B)

print ''' 
L3 <- L3 + L1 '''
B[2,:] = B[2,:] + B[0,:]

print '''Matriz B:
%s ''' % str(B)

print ''' 
L1 <- L1 + L2 
L3 <- L3 + L2'''
B[0,:] = B[0,:] + B[1,:]
B[2,:] = B[2,:] + B[1,:]

print '''Matriz B:
%s ''' % str(B)

print '''
Portanto:
    x1 = 5w
    x2 = 6w
    x3 = w
    para todo w pertencente a R
'''


print '''
---------------------------------------------------------------
Capítulo 1.2
---------------------------------------------------------------
Exercício 1.2.6 (pág. 64)

Seja A, 
'''

from sympy import Symbol
x = Symbol('x')

A = Matrix([[1,2,-3,4],[3,-1,5,2],[4,1,(x**2 - 14),x + 2]])
print '''Matriz A:
%s
''' % str(A)

print '''
a) Encontre os valores de x para quais o sistema não tem solução,
tem solução única e tem soluções infinitas.
'''

print '''
L2 <- L2 - 3 * L1
L3 <- L3 - 4 * L1
'''
A[1,:] = A[1,:] - 3 * A[0,:]
A[2,:] = A[2,:] - 4 * A[0,:]

print '''Matriz A:
%s ''' % str(A)

print '''
L2 <- L2 / -7
'''
A[1,:] = A[1,:] / -7

print '''Matriz A:
%s ''' % str(A)

print '''
L1 <- L1 - 2 * L2
L3 <- L3 + 7 * L2
'''
A[0,:] = A[0,:] - 2 * A[1,:]
A[2,:] = A[2,:] + 7 * A[1,:]

print '''Matriz A:
%s ''' % str(A)

print '''Portanto
    i. Se a 3L for totalmente zero, o sistema tem infinitas soluções.
    Se x**2 -16 = 0 e x -4 = 0, o sistema tem infinitas soluções.
    Assim, se x = 4 o sistema tem infinitas soluções.
    
    ii. Se x**2 - 16 = 0 e x -4 != 0, o sistema não tem solução.
    A 3L ficaria [0 0 0 N] sendo N != 0.
    Neste caso, para x = -4 o sistema não tem solução.
    
    iii. Se x**2 - 16 != 0, então o sistema tem solução única.
    A 3L ficaria [0 0 N1 N2] com N1 e N2 diferente de 0.
    Assim, para X != +-4 o sistema tem solução única.
'''


A = Matrix([[1,1,1,2],[2,3,2,5],[2,3,x**2 - 1,x + 1]])
print '''
-----------------------------------------------------------------
Matriz A:
%s
''' % str(A)

print '''
b) Encontre os valores de x para quais o sistema não tem solução,
tem solução única e tem soluções infinitas.
'''

print '''
L2 <- L2 - 2 * L1
L3 <- L3 - 2 * L1
'''
A[1,:] = A[1,:] - 2 * A[0,:]
A[2,:] = A[2,:] - 2 * A[0,:]

print '''Matriz A:
%s ''' % str(A)

print '''
L1 <- L1 - L2
L3 <- L3 - L2
'''
A[0,:] = A[0,:] - A[1,:]
A[2,:] = A[2,:] - A[1,:]

print '''Matriz A:
%s ''' % str(A)

print '''Portanto
    i. Para ter infinita soluções, a última linha seria de zeros.
    [0 0 0 0]
    Para isso, x**2 - 3 = 0 e x - 4 = 0
    Portanto, x tem que ser raix(3) e x = 4, o que é impossível.
    Logo, esse sistema não admite infinitas soluções.
    
    ii. Para não ter solução, o sistema precisa terminar com a 
    última linha [0 0 0 N] sendo N para todo N diferente de zero.
    Logo, para:
        x**2 - 3 = 0, ou x = raix(3) e
        x - 4 != 0, ou x != 4.
    Assim, para x = +-raix(3) o sistema não tem solução.
    
    iii. Para ter uma única solução o sistema precisa terminar com
    a última linha [0 0 N1 N2] sendo N1 diferente de zero e N2 qualquer.
    Logo, para:
        x**2 - 3 != 0, ou x != +-raiz(3)
    o sistema tem solução única.
'''


print '''
---------------------------------------------------------------
Capítulo 1.2
---------------------------------------------------------------
Exercício 1.2.7 (pág. 65)

Caso da indústria. 
'''

A = Matrix([[2,1,3],[1,3,5],[3,2,4]])
print '''Matriz A:
%s
''' % str(A)

B = Matrix([1900,2400,2900])
print '''Matriz B:
%s
''' % str(B)

print '''
Montando a matriz aumentada:
'''
A = A.row_join(B)

print '''Matriz A aumentada:
%s ''' % str(A)

print '''
L1 = L2 e L2 = L1
'''
A[0,:],A[1,:] = A[1,:],A[0,:]

print '''Matriz A:
%s ''' % str(A)

print '''
L2 <- L2 - 2 * L1
L3 <- L3 - 3 * L1
'''
A[1,:] = A[1,:] - 2 * A[0,:] 
A[2,:] = A[2,:] - 3 * A[0,:] 

print '''Matriz A:
%s ''' % str(A)

print '''
L2 <- L2 / -5
'''
A[1,:] = A[1,:] / -5 

print '''Matriz A:
%s ''' % str(A)

print '''
L1 <- L1 - 3 * L2
L3 <- L3 + 7 * L2
'''
A[0,:] = A[0,:] - 3 * A[1,:] 
A[2,:] = A[2,:] + 7 * A[1,:] 

print '''Matriz A:
%s ''' % str(A)

print '''
L3 <- L3 * -5/6
'''
A[2,:] = A[2,:] * -5/6 

print '''Matriz A:
%s ''' % str(A)


print '''
L1 <- L1 - L3 * 4/5
L2 <- L2 - L3 * 7/5
'''
A[0,:] = A[0,:] - A[2,:] * 4/5 
A[1,:] = A[1,:] - A[2,:] * 7/5 

print '''Matriz A:
%s ''' % str(A)

print '''Portanto, foram vendidos:
    500g de x
    300g de y e
    200g de z
'''


print '''
---------------------------------------------------------------
Capítulo 1.2
---------------------------------------------------------------
Exercício 1.2.8 (pág. 65)

Função polinomial 
'''

a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
d = Symbol('d')


A = Matrix([[a*0**3,b*0**2,c*0,d,10],[a*1**3,b*1**2,c*1,d,7],[a*3**3,b*3**2,c*3,d,-11],[a*4**3,b*4**2,c*4,d,-14]])
print '''Matriz A:
%s
''' % str(A)

print '''
Substitui d = 10
'''
A = Matrix([[a*0**3,b*0**2,c*0,(10-10)],[a*1**3,b*1**2,c*1,(7-10)],[a*3**3,b*3**2,c*3,(-11-10)],[a*4**3,b*4**2,c*4,(-14-10)]])

print '''Matriz A:
%s
''' % str(A)

print '''
Um linha de zeros. Portanto temos infinitas soluções
'''

print '''
Deleta a L1
'''

A.row_del(0)

print '''Matriz A:
%s
''' % str(A)

print '''
L2 <- L2 - 27 * L1
L3 <- L3 - 64 * L1
'''

A[1,:] = A[1,:] - 27 * A[0,:] 
A[2,:] = A[2,:] - 64 * A[0,:] 

print '''Matriz A:
%s
''' % str(A)


print '''
L2 <- L2 / - 18
'''

A[1,:] = A[1,:] / -18 

print '''Matriz A:
%s
''' % str(A)


print '''
L1 <- L1 - L2
L3 <- L3 + 48 * L2
'''

A[0,:] = A[0,:] - A[1,:] 
A[2,:] = A[2,:] + 48 * A[1,:] 

print '''Matriz A:
%s
''' % str(A)


print '''
L3 <- L3 / 4
'''

A[2,:] = A[2,:] / 4

print '''Matriz A:
%s
''' % str(A)

print '''
L1 <- L1 + L3 / 3
L2 <- L2 - 4 * L3 / 3
'''

A[0,:] = A[0,:] + A[2,:] / 3
A[1,:] = A[1,:] - 4 * A[2,:] / 3


print '''Matriz A:
%s
''' % str(A)

print '''Portanto,
    a = 1
    b = -6
    c = 2
    d = 10
    
    Ou seja,
    p(x) = xˆ3 - 6xˆ2 + 2x + 10
''' 
    

print '''
---------------------------------------------------------------
Capítulo 1.2
---------------------------------------------------------------
Exercício 1.2.9 (pág. 67)

Função polinomial 
xˆ2 + yˆ2 + ax + by + c = 0
'''

a = Symbol('a')
b = Symbol('b')
c = Symbol('c')


A = Matrix([[(-2)**2,7**2,a*(-2),b*7,c,0],[(-4)**2,5**2,a*(-4),b*5,c,0],[(4)**2,(-3)**2,a*(4),b*(-3),c,0]])
print '''Matriz A:
%s
''' % str(A)

print '''
Passando os valores numéricos para depois da igualdade
'''

A = Matrix([[a*(-2),b*7,c,(0-4-49)],[a*(-4),b*5,c,(0-16-25)],[a*(4),b*(-3),c,(0-16-9)]])
print '''Matriz A:
%s
''' % str(A)

print '''
1L <- 1L / -2
'''

A[0,:] = A[0,:] / -2 
print '''Matriz A:
%s
''' % str(A)


print '''
2L <- 2L + 4 * 1L
3L <- 3L - 4 * 1L
'''

A[1,:] = A[1,:] + 4 * A[0,:]
A[2,:] = A[2,:] - 4 * A[0,:]
 
print '''Matriz A:
%s
''' % str(A)


print '''
2L <- 2L / -9
'''

A[1,:] = A[1,:] / -9
 
print '''Matriz A:
%s
''' % str(A)


print '''
1L <- 1L + 7 * 2L / 2
3L <- 3L - 11 * 1L
'''

A[0,:] = A[0,:] + 7 * A[1,:] / 2
A[2,:] = A[2,:] - 11 * A[1,:]
 
print '''Matriz A:
%s
''' % str(A)


print '''
3L <- 3L * 9 / 16
'''

A[2,:] = A[2,:] * 9 /16
 
print '''Matriz A:
%s
''' % str(A)


print '''
1L <- 1L + 3L / 9
2L <- 2L - 3L / 9
'''

A[0,:] = A[0,:] + A[2,:] / 9
A[1,:] = A[1,:] - A[2,:] / 9
 
print '''Matriz A:
%s
''' % str(A)


print '''Portanto,
    a = -2
    b = -4
    c = -29
    
    E a equação do círculo é:
    xˆ2 + yˆ2 - 2x - 4y - 29 = 0
'''

