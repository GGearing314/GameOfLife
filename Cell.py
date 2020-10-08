#Cell class for Life | G Gearing | 16/04/2020

class Cell():
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def kill(self):
        del self
    
    def getNeighbours(self):
        coords=list()
        for yCounter in range(3):
            for xCounter in range(3):
                coords.append((self.x-1+xCounter,self.y-1+yCounter))
        return coords
