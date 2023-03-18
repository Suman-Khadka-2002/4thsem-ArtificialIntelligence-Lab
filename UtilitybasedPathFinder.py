# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 16:30:14 2022

@author: SANTOSH
"""
'''
->Assuming a graph with vertices A,B,C,G With G as goal node ,A is starting node
->has 2 path to reach G fro A , A-B-G and A-C-G.
->Utility based agent has task to find the route with minimum cost.'''
def alp(num): # to give letter to the node
    if num==0:
        return 'A'
    elif num==1:
        return 'B'
    elif num==2:
        return 'C'
    elif num==3:
        return 'G'
    
def costcheck(cost): # to print 'not defined to' values that 
                     # isnt given i.e A-G and B-C
   if cost==0:
       return 'Not defined'
   else:
       return cost 

def totcost(i,j,k):
    print("\nCost for ",alp(i),"-",alp(j),"-",alp(k))
    print(alp(i),"-",alp(j),"=",costs[i][j])
    print(alp(j),"-",alp(k),"=",costs[j][k])
    print("Total Cost= ",costs[i][j]+costs[j][k])
    return costs[i][j]+costs[j][k]
    
   
costs=[[0,10,8,0],
       [10,0,0,4],
       [8,0,0,8],
       [0,4,8,0]] # Adjacency matrix of graph
print("The costs of the path: \n")
for i in range(0,4):
    for j in range(0,4):
        if i>=j: #skipping the values below and including diagonal of matrix 
            pass
        else:
            # printing cost
            print(alp(i)," to ",alp(j)," = ",costcheck(costs[i][j])) 
print("\nFinding cost of undefined path (B to C) : ")
print("B-G-C : ",costs[1][3]+costs[3][2])
print("B-A-C : ",costs[1][0]+costs[0][2])

## Checking for the shortest route
print("\nFinding cost for A to G")
print("Finding and comparing the cost of route A-B-G and A-C-G ")
a=totcost(0,1,3)
b=totcost(0, 2, 3)
if min(a,b)==a:
    print("\nPath A-B-G has minimum cost: ", a," .So Utility agent will pick this path")
else:
    print("\nPath A-C-G has minimum cost: ", b," .So Utility agent will pick this path")