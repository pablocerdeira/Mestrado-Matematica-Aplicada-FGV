# -*- coding:utf-8 -*-


def S(seq, i=0):
    if i == len(seq):
        return 0
    return S(seq, i+1) + seq[i]


def T(seq, i=0):
    if i == len(seq):
        return 1
    return T(seq, i+1) + 1

seq = range(101)

print seq

print "Tamanho da sequência: %s" % str(len(seq))

print S(seq)

print T(seq)

seq = range(100)

for n in range(100):
    seq = range(n)
    assert T(seq) == n + 1
