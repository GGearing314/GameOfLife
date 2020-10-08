#Conway's Game Of Life | G Gearing | 16/04/2020

import numpy as np
from time import sleep

tick=0
tickInterval=1

#World Generation:
numCol=10 #Max x values
numRow=10 #Max y values
world=np.zeros((numCol,numRow))

world[5][5]=1
world[5][4]=1
world[5][3]=1
world[4][5]=1

#Functions and procedures:
def getNeighbours(x,y):
    coords=list()
    for yCounter in range(3):
        for xCounter in range(3):
            coords.append((x-1+xCounter,y-1+yCounter))
    return coords

def countNeighbours(x,y): #Function takes Cell object and counts how many live cells surround it 
    coords=getNeighbours(x,y)
    cellCount=(-1)

    for c in coords:
        if (c[0]<0) or (c[1]<0) or (c[0]==numCol) or (c[1]==numRow):
            continue
        if world[c[0]][c[1]]==1:
            cellCount+=1
    return cellCount

def canReproduce(x,y): #Checks to see if a dead cell can become live and if so...makes it so
    if (countNeighbours(x,y)+1)==3:
        return True
    
#Main Loop:
while True:
    print("Generation"+str(tick))
    #------>
    #TODO graphical representation here ------
    print(world)
    #------>
    sleep(tickInterval)
    changes=list() #List of change tuples with structure (x,y,state)
    for y in range(numRow):
        for x in range(numCol):
            if world[x][y]==1:
                cellCount=countNeighbours(x,y)
                if cellCount<2 or cellCount>3:  #Deals with the rules for killing off cells 
                    changes.append((x,y,0)) #Issues a change to kill that cell
            else:
                if canReproduce(x,y):
                    changes.append((x,y,1)) #Issues a chnage to create a cell
    #Updates the actual world after it has all been checked through:   
    if len(changes)==0:
        break
    for change in changes:
        world[change[0]][change[1]]=change[2]
    tick+=1
print("World has ground to a stop")
