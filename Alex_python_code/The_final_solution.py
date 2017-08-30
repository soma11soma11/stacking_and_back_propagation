# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 10:34:58 2017

@author: Alexa
"""
import numpy as np
import math as m
import scipy as sp
### Finding the nearest stochastic squareroot/intensity matrix

Smatrix=np.matrix([[0.5,0.2,0.3], [0.2,0.5,0.3],[0.3,0.3,0.4]]) 
print("Our stochastic matrix")
print(Smatrix)

M=len(Smatrix[:,1])
#Emp_trans_mat=np.zeros([M,M])
#Timeaty=np.zeros(M)
#count_mat=np.zeros([M,M])
#A=np.matrix([[1,2,2], [1,4,1],[2,1,3]])

vlog=np.vectorize(m.log)



######################

def my(P,C,N):  #P your stochastic matrix, C a count matrix from data
 P1=np.matrix(P)
 C1=np.matrix(C)
 L=1
 LOGP=vlog(P1)   ### Take the log of the maximum function 
# M=
 LIKE=(-1/N)*(C*LOGP)
 return LIKE
########################


#######################
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

DL=5000    #Number of data points you want to simulate
[E1,Count1,H1,T1]=Simulate(1, DL, Smatrix)
S2=sp.linalg.sqrtm(Smatrix,0.10)
print(S2)
########################





########################


def approxgrad(epsilon, alpha,x,C):  ##alpha needs to be a matrix
    y=(1/epsilon[0])*(my(x+epsilon*alpha,C,DL)-my(x,C,DL))
    Y=np.matrix(y)
    return y


def funcmin(Initial,lowtrain,uptrain,lowalpha,upalpha,lowepsilon,upepsilon, Iterations):
    place=Initial
    for i in range(Iterations):
     alpha=np.random.uniform(lowalpha,upalpha,(M,M))
     epsilon=np.random.uniform(lowepsilon,upepsilon,1)
     trainrate=np.random.uniform(lowtrain,uptrain,1)
     place=(1-trainrate[0])*place+trainrate[0]*approxgrad(epsilon,alpha,place,Count1)
    return place
########################





######################





