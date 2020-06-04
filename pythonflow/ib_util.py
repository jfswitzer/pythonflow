import hashlib
import builtins
import random as rand
import operator
from .core import opmethod, SAVED_VALUES

def autogen_problem():
    #arithmetic for now
    n = rand.randint(0,1000)
    m = rand.randint(0,1000)
    op = rand.randint(0,3)
    if (m == 0) & (op == 3):
        m = 1
    if (op == 0):
        val = n + m
        op = operator.add
    elif (op == 1):
        val = n - m
        op = operator.sub
    elif (op == 2):
        val = n * m
        op = operator.mul
    else:
        val = n / m
        op = operator.truediv
    target = op
    args = (n, m)
    m = hashlib.sha256()
    m.update(str(target).encode('utf-8'))
    m.update(str(args).encode('utf-8'))
    h = m.digest()
    print("Autogen - target "+ str(target)+"args "+str(args)+" h looks like: "+str(h))
    SAVED_VALUES[h] = val
    
    
        
