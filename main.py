import numpy as np
import eel

eel.init("template")    # Accessing front from template folder

def PyIsEnd(case,whose):    # Function to show the end by javaScript
    eel.js_rslt(case,whose)

# Game class
class Tx3():
    # Main game array
    Array = np.array([[' ',' ',' ',],[' ',' ',' ',],[' ',' ',' ']])
    mode = None     # Game mode (1p or 2p)
    turn = 1    # player turn (1 or 2)
    
    # method to change turn
    def changeTurn(self):
        if(self.turn==1):
            self.turn = 2
        else:
            self.turn = 1

    # method to make a move,
    def writeToArray(self, x,y):
        if(self.turn == 1):
            player = "o"    # where player tells who move (o or t)
        else:
            player = "t"
        if (self.Array[x,y] == ' '):
            self.Array[x,y] = player
            self.changeTurn()
            self.isGameEnd()
            return True
        else:
            return False
    
    def reset(self):    # For reseting the game
        self.Array = np.array([[' ',' ',' ',],[' ',' ',' ',],[' ',' ',' ']])
        self.mode = None
        self.turn = 1
        tx3.showArray()

    # PC move in 1 player mode
    def AImove(self):
        a = self.Array
        if (not self.isGameEnd()):
            while True:
                if (a[1,1] == ' '):
                    self.writeToArray(1,1)
                    break
                elif (a[0,0] == a[0,1] != ' ' and a[0,2] == ' '):  #1st row
                    self.writeToArray(0,2)
                    break
                elif (a[0,0] == a[0,2] != ' ' and a[0,1] == ' '):
                    self.writeToArray(0,1)
                    break
                elif (a[0,2] == a[0,1] != ' ' and a[0,0] == ' '):
                    self.writeToArray(0,0)
                    break
                elif (a[1,1] == a[1,0] != ' ' and a[1,2] == ' '):  # 2nd row
                    self.writeToArray(1,2)
                    break
                elif (a[1,1] == a[1,2] != ' ' and a[1,0] == ' '):
                    self.writeToArray(1,0)
                    break
                elif (a[2,2] == a[2,1] != ' ' and a[2,0] == ' '):  # 3rd row
                    self.writeToArray(2,0)
                    break
                elif (a[2,2] == a[2,0] != ' ' and a[2,1] == ' '):
                    self.writeToArray(2,1)
                    break
                elif (a[2,1] == a[2,0] != ' ' and a[2,2] == ' '):
                    self.writeToArray(2,2)
                    break   #center
                elif (a[2,2] == a[1,2] != ' ' and a[0,2] == ' '):  # 3rd column
                    self.writeToArray(0,2)
                    break
                elif (a[0,2] == a[2,2] != ' ' and a[1,2] == ' '):
                    self.writeToArray(1,2)
                    break
                elif (a[0,2] == a[1,2] != ' ' and a[2,2] == ' '):  
                    self.writeToArray(2,2)
                    break
                elif (a[1,1] == a[2,1] != ' ' and a[0,1] == ' '):
                    self.writeToArray(0,1)
                    break
                elif (a[1,1] == a[0,1] != ' ' and a[2,1] == ' '):
                    self.writeToArray(2,1)
                    break
                elif (a[0,0] == a[1,0] != ' ' and a[2,0] == ' '):
                    self.writeToArray(2,0)
                    break
                elif (a[0,0] == a[2,0] != ' ' and a[1,0] == ' '):
                    self.writeToArray(1,0)
                    break
                elif (a[1,0] == a[2,0] != ' ' and a[0,0] == ' '):
                    self.writeToArray(0,0)
                    break   # All striaght
                elif (a[0,0] == a[1,1] != ' ' and a[2,2] == ' '):
                    self.writeToArray(2,2)
                    break
                elif (a[2,2] == a[1,1] != ' ' and a[0,0] == ' '):
                    self.writeToArray(0,0)
                    break
                elif (a[0,2] == a[1,1] != ' ' and a[2,0] == ' '):
                    self.writeToArray(2,0)
                    break
                elif (a[2,0] == a[1,1] != ' ' and a[0,2] == ' '):
                    self.writeToArray(0,2)
                    break
                else:
                    Column = np.random.choice([0,1,2])
                    Row = np.random.choice([0,1,2])
                    if self.writeToArray(Column,Row):
                        break
                    else:
                        continue

    def isDraw(self):   # method to check is match draw
        for x in range(3):
            for y in range(3):
                if self.Array[x,y] == ' ':
                    return False
        return True
    
    def isGameEnd(self):    # Method which checks is game end or not
        if self.Array[0,0] == self.Array[0,1] == self.Array[0,2] != ' ':
            PyIsEnd(1,self.Array[0,1])
            return True
        elif self.Array[1,0] == self.Array[1,1] == self.Array[1,2] != ' ':
            PyIsEnd(2,self.Array[1,1])
            return True
        elif self.Array[2,0] == self.Array[2,1] == self.Array[2,2] != ' ':
            PyIsEnd(3,self.Array[2,0])
            return True
        elif self.Array[0,0] == self.Array[1,0] == self.Array[2,0] != ' ':
            PyIsEnd(4,self.Array[0,0])
            return True
        elif self.Array[0,1] == self.Array[1,1] == self.Array[2,1] != ' ':
            PyIsEnd(5,self.Array[0,1])
            return True
        elif self.Array[0,2] == self.Array[1,2] == self.Array[2,2] != ' ':
            PyIsEnd(6,self.Array[0,2])
            return True
        elif self.Array[0,0] == self.Array[1,1] == self.Array[2,2] != ' ':
            PyIsEnd(7,self.Array[0,0])
            return True
        elif self.Array[0,2] == self.Array[1,1] == self.Array[2,0] != ' ':
            PyIsEnd(8,self.Array[0,2])
            return True
        elif self.isDraw():
            return True
        else:
            return False
        
    def showArray(self):    # method which returns a output array
        output = []
        for x in range(3):
            for y in range(3):
                if self.Array[x,y] == 'o':
                    output.append("use one")
                elif self.Array[x,y] == 't':
                    output.append("use two")
                else:
                    output.append("noo")
        eel.updateGrid(output)

tx3 = Tx3()

def PyAiMove():
    tx3.AImove()
    tx3.showArray()
    tx3.isGameEnd()

@eel.expose
def PyStartGame(gmode):
    tx3.turn = 1
    tx3.mode = int(gmode)

@eel.expose
def PyShow():
    tx3.showArray()

@eel.expose
def PyMove(x,y):
    if(not tx3.isGameEnd()):
        tx3.writeToArray(x,y)
        tx3.showArray()
        tx3.isGameEnd()
        if(tx3.mode==1 and not tx3.isGameEnd()):
            PyAiMove()
        
@eel.expose
def PyReset():
    tx3.reset()

eel.start("Tx3.html", size=('445','500'))