# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 08:15:21 2022

@author: SANTOSH
"""
## Model + Goal based agent Vaccum Problem
#Array to store 2 previous states and 1 present state
##Goal condition: 3 consequetive clean states
import random
from random import randint 
from sys import exit
from time import sleep


def main(roomID):
    status=[1,1,1];#array to keep percent history ie past,present
    #assuming past state,past before past ,present state is dirty
    while(1):
        status[2]=random.randint(0,1)#current state
        if status[2]==0:
            goal(status,roomID)
            print("Room: ",roomID,"is clean , Moving to Room",anotherRoom(roomID))
            roomID=anotherRoom(roomID)
            sleep(1)
        elif status[2]==1:
            print("Room:",roomID,"is Dirty, Sucking the dirt And Rechecking")
            sleep(1)
        temp =status[1]
        status[1]=status[2]#previous states
        status[0]=temp #before previous

    
def anotherRoom(roomID):
    if roomID=='A' or roomID=='a':
        return 'B'
    else:
        return 'A'


def goal(status,roomID):
    if status[0]==0 and status[1]==0 and status[2]==0: #assuming 3 consequetive clean state to be goal state
        print("Room: ",roomID,"is clean")
        print("Goal achieved: 3 consequetive states were clean state")
        print("\nExiting the program")
        sleep(5)
        exit(0)

count=0
roomID=input("enter starting Room ID(A/B): ")
main(roomID)