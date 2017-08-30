# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 11:19:22 2017

@author: Alexa
"""

import numpy as np
import scipy as sp
import math 
import matplotlib.pyplot

M=2  #argsize of myfunction.

def my(x):
    y=(math.exp(-(x[0]**2)-(x[1]**4)))-x[0]*x[1]-x[1]**2-x[0]**2
    return y

#The next function will calculate an approxiamte gradient, the function
#is "Hardwired" into it



def approxgrad(epsilon, alpha,x):
    y=(1/epsilon)*(my(x+epsilon*alpha)-my(x))
    return y
    
###Now to actually find the minimum of a function 


def funcmin(Initial,alpha,epsilon,trainrate,Iterations):
    place=Initial
    for i in range(Iterations):
     place=place-trainrate*approxgrad(epsilon,alpha,place) 
    return place, my(place)


def coolingfunc(x) :
    y=1/(x+1)
    return y

def funcmax(Initial,lowtrain,uptrain,lowalpha,upalpha,lowepsilon,upepsilon, Iterations):
    place=Initial
    for i in range(Iterations):
     alpha=np.random.uniform(lowalpha,upalpha,M)
     epsilon=np.random.uniform(lowepsilon,upepsilon,1)
     trainrate=np.random.uniform(lowtrain,uptrain,1)
     place=place+trainrate*coolingfunc(0)*approxgrad(epsilon,alpha,place)
     #print(place)
    return place, my(place)

    
    
    
    






