# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 09:35:55 2017

@author: Alexa
"""

###This code is to define the likelihood function for Markov chain

import numpy as py
import math as m
import scipy as sp

vlog=np.vectorize(m.log)

def LogLikelihood(P,C):  #P your stochastic matrix, C a count matrix from data
 P1=np.matrix(P)
 X1=np.matrix(X)
 L=1
 LOGP=vlog(P1)   ### Take the log of the maximum function 
 M=len(X)
 LIKE=(-1/M)*(C*LOG(P))
 return LIKE


 
 