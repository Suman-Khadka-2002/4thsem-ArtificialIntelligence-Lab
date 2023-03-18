# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 18:41:09 2022

@author: bpn_a
"""

import numpy as np 
from random import randint

#inputs 
X=np.array([[1,1,1],[1,-1,1],[-1,1,1],[-1,-1,1]])
#output
Y_ad=np.array([[1],[-1],[-1],[-1]])

print('input as X1, X2, b:')
print (X)
print("\n")
print('output as Y: ')
print (Y_ad)
print("\n")
weights_ad=np.zeros((3))
# weights_o=np.zeros((3))
print("Initial Weights: ")
print(weights_ad)
print("\n")

# update weight for and gate /logic
def update_weight_ad(X,Y,weights):
    for i in range(4):
         
        weights=weights+X[i]*Y[i]
        #print weights
        slope =(-weights[0]/weights[1])
        # c=int(-weights[2]/weights[0])
        if slope<0 and weights[0]>0:
            weights_main=weights
        
    return weights_main

weights_ad=update_weight_ad(X,Y_ad,weights_ad)

rand_int=int(input('Enter the test case no you want to try : '))
print("As for now, Added Weights : W1, W2 and B")
print(weights_ad)
print("\n")
print("As for now, value of X1, X2, b:")
print( X[rand_int])
print("\n")
def check_learning(X,weights,rand_int):
    Yin=0
    for i in range(3):
        Yin+=X[rand_int,i]*weights[i]
    if Yin<0:
        Yin=-1
    elif Yin == 0:
        exit
    else:
        Yin=1
    return Yin

Yin=check_learning(X,weights_ad,rand_int)

print ('Y= ', Yin)