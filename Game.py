import numpy as np
class Game:
    def __init__(self) -> None:
        self.background=np.array([
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
        ])
    def print_background(self)->None:
        for i in self.background:
            for j in i:  
                print("|",end="")  
                print(j,end="|")
            print("")
        print("")
    def changeO(self,x:int,y:int)->bool:
        if self.background[x][y]==" ":
            self.background[x][y]="O"
            return True
        else:
            return False
    def changeX(self,x:int,y:int)->bool:
        if self.background[x][y]==" ":
            self.background[x][y]="X"
            return True
        else:
            return False
    def play(self,x:int,y:int,m:str)->bool:
        played=False
        if m=="X":
            played=self.changeX(x,y)
        elif m=="O":
            played=self.changeO(x,y)
        return played
    def check_Win(self,m:str)->bool:
        possible1=self.background[0][0]+self.background[0][1]+self.background[0][2]
        possible2=self.background[1][0]+self.background[1][1]+self.background[1][2]
        possible3=self.background[2][0]+self.background[2][1]+self.background[2][2]
        possible4=self.background[0][0]+self.background[1][0]+self.background[2][0]
        possible5=self.background[0][1]+self.background[1][1]+self.background[2][1]
        possible6=self.background[0][2]+self.background[1][2]+self.background[2][2]
        possible7=self.background[0][0]+self.background[1][1]+self.background[2][2]
        possible8=self.background[0][2]+self.background[1][1]+self.background[2][0]
        mmm=m+m+m
        return mmm==possible1 or mmm==possible2 or mmm==possible3 or mmm==possible4 or mmm==possible5 or mmm==possible6 or mmm==possible7 or mmm==possible8
    def check_draw(self):
        count=0
        for x in np.nditer(self.background):
            if x=="X" or x=="O": count+=1
        return count==9
           