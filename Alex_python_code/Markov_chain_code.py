# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 15:43:09 2017

@author: Alexa
"""

###This is some code for Markov chains

import numpy as np
import matplotlib.pyplot as plt

Smatrix=np.matrix([[0.5,0.2,0.3], [0.2,0.5,0.3],[0.3,0.3,0.4]])
#print(Smatrix)

M=len(Smatrix[:,1])
#Emp_trans_mat=np.zeros([M,M])
#Timeaty=np.zeros(M)
#count_mat=np.zeros([M,M])
#A=np.matrix([[1,2,2], [1,4,1],[2,1,3]])

def update(A,x,y):   ##Updating it from last Observation
 Count_mat=np.matrix(A)
# Time=np.sum(Count_mat, axis=1)
 #Time[x,0]=Time[x,0]+1
 Count_mat[x,y]=Count_mat[x,y]+1
 #Emp_trans_mat=(Count_mat[:,y])*(1/(Time[x,0]))
 return Count_mat



def Simulate(Initial,Iterations,Stochasticmatrix):
    State=Initial
    History=[Initial]
    Emp_trans_mat=np.matrix(np.identity(M))
    C=np.matrix(np.ones(shape=(M,M)))
    Time=np.sum(C, axis=1)
    for i in range(Iterations):
        d=np.ndarray.tolist(Stochasticmatrix[State,:])
        New=np.random.multinomial(1,d[0],1)
        Prevstate=State
        State=np.argmax(New)
        C=update(C,Prevstate,State)
        History.append(State)
    Time=np.sum(C, axis=1)
    for i in range(M):
         Emp_trans_mat[i,:]=(C[i,:])*(1/(Time[i,0]))
    return Emp_trans_mat,C, History,Time

        
[E1,Count1,H1,T1]=Simulate(1, 5000, Smatrix)

S2=sp.linalg.logm(Smatrix,0.10)

print(S2)

#[E2,Count2,H2,T2]=Simulate(1, 10000, S2)










