# -*- coding:utf-8 -*-
from sympy import pprint
from sympy import Symbol
from sympy.matrices import *
import sys
sys.displayhook(pprint)

print '''
****************************************************************************
Exercício 01:
Asdrúbal acabou de receber um prêmio de 25 mil reais e deseja investir o 
dinheiro recebido. Ele deseja aplicar 6 mil reais em CDB, 3 mil reais em 
moeda estrangeira e 16 mil em ações. No entanto, no banco onde Asdrúbal 
pensa em investir só existe as seguintes opções de carteiras: 

opções de investimento Composição em cada quota
Carteira A 2 reais em CDB, 2 reais em moeda estrangeira, 2 reais em ações
Carteira B 1 real em CDB, nada em moeda estrangeira e 2 reais em ações
Carteira C 1 real em CDB, 1 real em moeda estrangeira e 3 reais em ações

(a) Mostre que as carteiras formam uma base do espaço das aplicações.

(b) Descreva a distribuição das aplicações desejada por Asdrúbal na base 
das carteiras.

(c) Quantas quotas de cada carteira Asdrúbal deve adquirir para compor a 
aplicação que deseja?

'''

print '''
Resposta Execício 01:
(a) Mostre que as carteiras formam uma base do espaço das aplicações.
'''

print '''
Montando matriz das carteiras (A):

Coluna 1: Carteira A
Coluna 2: Carteira B
Coluna 3: Carteira C
Coluna 4: Total das carteiras A, B e C

Linha 1: CDB
Linha 2: Moeda estrangeira
Linha 3: Ações
Linha 4: Montante desejado
'''

A = Matrix([[2,1,1,6000],[2,0,1,3000],[2,2,3,16000],[6,3,5,25000]])
print '''Matriz A:
%s
''' % str(A)

print '''
Operações 1:
L2 <- L2 - L1
L3 <- L3 - L1
L4 <- L4 - 3*L1
'''

A[1,:] = A[1,:] - A[0,:] 
A[2,:] = A[2,:] - A[0,:] 
A[3,:] = A[3,:] - 3 * A[0,:] 

print '''Matriz A após operações 1:
%s
''' % str(A)


print '''
Operações 2:
L2 <- L3
L3 <- L2
'''

A[1,:], A[2,:] = A[2,:], A[1,:]

print '''Matriz A após operações 2:
%s
''' % str(A)

print '''
Operações 3:
L1 <- L1 - L2
L3 <- L3 + L2
'''

A[0,:] = A[0,:] - A[1,:]
A[2,:] = A[2,:] + A[1,:]

print '''Matriz A após operações 3:
%s
''' % str(A)

print '''
Operações 4:
L1 <- L1 + 0.5 * L3
L2 <- L2 - L3
'''

A[0,:] = A[0,:] + 0.5 * A[2,:]
A[1,:] = A[1,:] - A[2,:]

print '''Matriz A após operações 4:
%s
''' % str(A)

print '''
Operações 5:
L1 <- L1 / 2
L3 <- L3 /2
'''

A[0,:] = A[0,:] / 2
A[2,:] = A[2,:] / 2

print '''Matriz A após operações 5:
%s
''' % str(A)

print '''
Portanto, em resposta ao questionamento (a):
As carteiras formam uma base no espaço, já que todas as 
variáveis são independentes.
Ela não formaria uma base no espaço se:
- uma das linhas resultasse zero em todos os lugares,
significando que haveria variáveis dependentes (x = y +1), ou
- se todas as variáveis em uma linha fossem zero e o resultado 
da equação fosse diferente de zero (não haveria cruzamento dos 
planos).
'''

print '''
Resposta ao exercício 01:
(b) Descreva a distribuição das aplicações desejada por Asdrúbal na base 
das carteiras.
Conferir com Moacyr ou Asla.
'''

print '''
****************************************************************************
2. É verdade que existe um polinômio de grau 3 que passa pelos pontos P1 = (0; 1), P2 = (1; 0), P3 =
(2; 1), P4 = (3; 2)? Como encontrá-lo? Mostre que este problema é equivalente a resolver um sistema
linear. Use um pacote computacional para resolver o sistema e para desenhar um gráfico com os pontos
Pi e este polinômio interpolador.
'''

print '''
Resposta Execício 02:
'''

print '''
Montando matriz dos ponto Pi (A) para o polinômio:
p(x) = axˆ3 + bxˆ2 + cx + d
a0ˆ3 + b0ˆ2 + c0 + d = 1
a1ˆ3 + b1ˆ2 + c1 + d = 0
a2ˆ3 + b2ˆ2 + c2 + d = 1
a3ˆ3 + b3ˆ2 + c3 + d = 2

Ou,

0 + 0 + 0 + d = 1
a + b + c + d = 0
8a + 4b + 2c + d = 1
27a + 9b + 3c + d = 2

'''

A = Matrix([[0,0,0,1,1],[1,1,1,1,0],[8,4,2,1,1],[27,9,3,1,2]])
print '''Matriz A:
%s
''' % str(A)

print '''
Concluimos que d = 1.
Substituimos d por 1 nas equações seguintes e remontamos a matriz.
'''

A = Matrix([[1,1,1,(0-1)],[8,4,2,(1-1)],[27,9,3,(2-1)]])
print '''Nova matriz A:
%s
''' % str(A)


print '''
Operações 1:
L2 <- L2 - 8 * L1
L3 <- L3 - 27 * L1
'''

A[1,:] = A[1,:] - 8 * A[0,:]
A[2,:] = A[2,:] - 27 * A[0,:]

print '''Matriz A após operações 1:
%s
''' % str(A)

print '''
Operações 2:
L2 <- L2 / -4
L1 <- L1 - L2
L3 <- L3 + 18 * L2
'''

A[1,:] = A[1,:] / -4
A[0,:] = A[0,:] - A[1,:]
A[2,:] = A[2,:] + 18 * A[1,:]

print '''Matriz A após operações 2:
%s
''' % str(A)


print '''
Operações 3:
L3 <- L3 / 3
L1 <- L1 + L3 * 1/2
L2 <- L2 - L3 * 3/2
'''

A[2,:] = A[2,:] / 3
A[0,:] = A[0,:] + A[2,:] * 1/2
A[1,:] = A[1,:] - A[2,:] * 3/2

print '''Matriz A após operações 3:
%s
''' % str(A)

print '''
Portanto, os valores de a, b, c e d no polinômio são:
p(x) = -1/3xˆ3 + 2xˆ2 + -8/3x + 1

ATENÇÃO: Este resultado está errado.
Conferir com Moacyr ou Asla.
'''


import numpy as np
import matplotlib.pyplot as plt

def p(x):
    return -1/3*x**3 + 2*x**2 + -8/3*x + 1

seq = np.arange(0,4,1)

for i in seq:
    print "x: %f, y: %f" % (seq[i],p(seq[i]))

#plt.plot(seq,p(seq))

#plt.show()

print '''
****************************************************************************
3. (Trefethen) Considere a matriz B de dimensões 4x4. Sobre ela são aplicadas as 
seguintes operações:
(a) Multiplicar a coluna 1 por 2
(b) Dividir a linha 1 por 3
(c) Adicionar a linha 3 à linha 1
(d) Trocar a coluna 1 com a coluna 4 de lugar
(e) Subtrair a linha 2 das demais linhas
(f) Substituir a coluna 4 pela coluna 3
(g) eliminar a coluna 1 (portanto o número de colunas é reduzido para 3)

i. Escreva o resultado como produto de 8 matrizes
ii. Escreva o resultado novamente como um produto A  B  C (mesmo B do enunciado) 
de três matrizes.
'''

print '''
Criando a matriz B 4x4:
'''

B = Matrix([[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]])
print '''Matriz B:
%s
''' % str(B)


print '''
a) Multiplicar a coluna 1 por 2
Criando a matriz E1:
'''

E1 = Matrix([[2,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
print '''Matriz E1:
%s
''' % str(E1)

print '''Matriz B*E1:
%s
''' % str(B*E1)


print '''
b) Dividir a linha 1 por 3
Criando a matriz E2:
'''

E2 = Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
E2[0,:] = E2[0,:] / 3
print '''Matriz E2:
%s
''' % str(E2)

print '''Matriz E2*B*E1:
%s
''' % str(E2*B*E1)


print '''
c) Adicionar a linha 3 à linha 1
Criando a matriz E3:
'''

E3 = Matrix([[1,0,0,0],[0,1,0,0],[1,0,1,0],[0,0,0,1]])
print '''Matriz E3:
%s
''' % str(E3)

print '''Matriz E3*E2*B*E1:
%s
''' % str(E3*E2*B*E1)


print '''
d) Trocar a coluna 1 com a coluna 4 de lugar
Criando a matriz E4:
'''

E4 = Matrix([[0,0,0,1],[0,1,0,0],[0,0,1,0],[1,0,0,0]])
print '''Matriz E4:
%s
''' % str(E4)

print '''Matriz E3*E2*B*E1*E4:
%s
''' % str(E3*E2*B*E1*E4)


print '''
e) Subtrair a linha 2 das demais linhas
Criando a matriz E5:
'''

E5 = Matrix([[1,-1,0,0],[0,1,0,0],[0,-1,1,0],[0,-1,0,1]])
print '''Matriz E5:
%s
''' % str(E5)

print '''Matriz E5*E3*E2*B*E1*E4:
%s
''' % str(E5*E3*E2*B*E1*E4)


print '''
f) Substituir a coluna 4 pela coluna 3
Criando a matriz E6:
'''

E6 = Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,1],[0,0,0,0]])
print '''Matriz E6:
%s
''' % str(E6)

print '''Matriz E5*E3*E2*B*E1*E4*E6:
%s
''' % str(E5*E3*E2*B*E1*E4*E6)


print '''
g) eliminar a coluna 1 (portanto o número de colunas é reduzido para 3)
Criando a matriz E7:
'''

E7 = Matrix([[0,0,0],[1,0,0],[0,1,0],[0,0,1]])
print '''Matriz E7:
%s
''' % str(E7)

print '''Matriz E5*E3*E2*B*E1*E4*E6*E7:
%s
''' % str(E5*E3*E2*B*E1*E4*E6*E7)

print '''
Portanto, quanto ao item i:
i. Escreva o resultado como produto de 8 matrizes
O resultado é:

Matriz E5*E3*E2*B*E1*E4*E6*E7

Sendo as matrizes:
'''
print '''E1:
%s
''' % str(E1)
print '''E2:
%s
''' % str(E2)
print '''E3:
%s
''' % str(E3)
print '''E4:
%s
''' % str(E4)
print '''E5:
%s
''' % str(E5)
print '''E6:
%s
''' % str(E6)
print '''E7:
%s
''' % str(E7)



print '''
ii. Escreva o resultado novamente como um produto A  B  C (mesmo 
B do enunciado) de três matrizes.

Para isso multiplicamos cada uma das matrizes de cada lado de B:
'''

print '''
Matriz A = E5*E3*E2 e
Matriz B = E1*E4*E6*E7
'''

print '''
Portanto,
Matriz A:
%s
e
Matriz B:
%s ''' % (str(E5*E3*E2),str(E1*E4*E6*E7))



print '''

****************************************************************************'''
A = Matrix([[1,0,1],[2,1,1],[3,1,2],[3,2,1]])
print '''
4. Seja 
A = 
%s ''' % str(A) 
print '''
(a) Use eliminação gaussiana para decompor A = L * U, onde L4x3 é triangular 
inferior e U3x3 é triangular superior
(b) Verique se o sistema A  x = b, onde b = [1; 2; 3; 1]T, tem solução.
'''

print '''
a) Encontrando a decomposição LU por Gauss
'''

print '''
Operações 1:
L2 <- L2 - 2 * L1
L3 <- L3 - 3 * L1
L4 <- L4 - 3 * L1
'''

E1 = Matrix([[1,0,0,0],[-2,1,0,0],[-3,0,1,0],[-3,0,0,1]])

print '''
Para isso multiplicaremos E1 por A, sendo E1:
%s 
''' % str(E1)

print '''
Matriz E1*A:
%s
''' % str(E1*A)


print '''
Operações 2:
L3 <- L3 - L2
L4 <- L4 - 2 * L2
'''

E2 = Matrix([[1,0,0,0],[0,1,0,0],[0,-1,1,0],[0,-2,0,1]])

print '''
Agora multiplicaremos E2 por E1*A, sendo E2:
%s 
''' % str(E2)

print '''
Matriz E2*E1*A:
%s
''' % str(E2*E1*A)


print '''
Portanto, a matriz L = E2*E1 e a matriz U = E2*E1*A
'''

print '''
Matriz L:
%s
''' % str(E2*E1)

print '''
Matriz U:
%s
''' % str(E2*E1*A)

print '''
Matriz LU:
%s
''' % str((E2*E1)*E2*E1*A)

print '''
Matriz A:
%s
''' % str(A)

print '''
ATENÇÃO: está errado.
Pedir ajuda a Moacyr ou Asla.
'''









