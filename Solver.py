from sympy import *
import numpy as np
rows,cols=map(int,input().split())
A,p,k,tvf,fgh=[],[],[],[],[]
blank_list=[]
for i in range(cols):
   blank_list.append(0)
with open('matrix.txt') as f:
    pfg = f.read().strip().split('\n')
A = []
for pf in pfg[0:rows]:
    e = pf.split()
    elements=e[0:cols]
    int_elements = []
    for element in elements:
        int_elements.append(int(element))
    A.append(int_elements)
print("MARTRIX=",A)
E=Matrix(A)
R=E.rref()
print("RREF",R[0])
null_space=E.nullspace()
n_space=np.array(null_space)
fgh=n_space.tolist()
for i in range(len(A[0])):
    if i not in R[1]:
        p.append(i+1)
for i in range(len(p)):
   k=[]
   for j in range(len(fgh[i])):
      k.append(fgh[i][j][0])
   tvf.append(k)
for i in range(len(p)):
    print("x{}".format(p[i]),"*",tvf[i],"+ ",end='')
print(blank_list,end="")