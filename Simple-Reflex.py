# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 08:15:21 2022

@author: SANTOSH
"""
## Simple reflex agent Vaccum Problem
## Chekcing if room is clean or not and cleaning 
## if count exceeds 10 , machine sleeps for sometime , then wakeup and continue the task again
import random
from random import randint 
from time import sleep
def main(roomID):
    global count
    count=0
    while(1):
        status=random.randint(0,1)
        if status==0:
            print("Room: ",roomID,"is clean , Moving to Room",anotherRoom(roomID))
            roomID=anotherRoom(roomID)
            sleep(5)
        elif status==1:
            print("Room:",roomID,"is Dirty, Sucking the dirt And Rechecking")
            sleep(5)
        count=count+1
        sleepCheck(count)
    
def anotherRoom(roomID):
    if roomID=='A' or roomID=='a':
        return 'B'
    else:
        return 'A'
def sleepCheck(count):
    if count>=5:
        print("going to sleep mode")
        sleep(20)
        print("\n\nWokeup and checking")
        main(roomID)

count=0
roomID=input("enter starting Room ID(A/B): ")
main(roomID)