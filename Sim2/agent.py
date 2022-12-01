import mesa
import math
from stack import StackAgent


class RobotAgent(mesa.Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.carrying = 0
        self.stackCount = 0
        self.tempClosest = 100
        self.point = 0,0
        self.movingToX = 0
        self.movingToY = 0
        self.new_pos = (0,0)
        self.foundBox = False
        self.gridmate = 1
        self.destroy = 0
        self.stacks = 0

    def pickUp(self):
        gridmate = self.model.grid.get_cell_list_contents([self.pos])
        print(len(gridmate), "GRRINDMATES" )
        if len(gridmate) > 1:
            self.model.grid.remove_agent(gridmate[0])

    def step(self):
        self.destroy = 0

        j = len(self.model.boxCoords)
        temp = 0

        print("PosX: ", self.pos[0])
        print("PosY: ", self.pos[1])
        print("J: ", j)
        if(j == 0 and (self.pos[0] == 0 and self.pos[1] == 0)):
            self.stay()
        else:
            if (self.carrying == 0):
                if(self.foundBox == False and j > 0):
                    for i in range(j):
                        print(self.model.boxCoords)
                        if((math.dist(self.pos, self.model.boxCoords[i])) < self.tempClosest):
                            #print("TEM")
                            #print(self.tempClosest)
                            self.tempClosest = math.dist(self.pos, self.model.boxCoords[i])

                            self.point = self.model.boxCoords[i]
                            temp = i
                            self.movingToX = self.point[0]
                            self.movingToY = self.point[1]
            
                    self.foundBox = True
                    print("Temp: ",temp)
                    print("X: ", self.movingToX)
                    print("Y: ", self.movingToY)
                    self.model.boxCoords.pop(temp)

            if (self.pos == (self.movingToX, self.movingToY)):
                print()
                self.pickUp()
                self.tempClosest = 100

            if(self.pos == (0,0) and self.foundBox == True):
                self.dropOff()
                self.foundBox =False
                print("dop")

    
            self.move()
        
        

    def move(self):
        #move until you find a box
        new_pos = 0
        if(self.carrying == 0):
            print(self.pos[0])
            print(self.pos[1])
            if(self.pos[0] != self.movingToX):
                
                if(self.pos[0] <= self.movingToX):
                    new_pos = (self.pos[0] + 1, self.pos[1])

                else:

                    new_pos = (self.pos[0] - 1, self.pos[1])

            if(self.pos[1] != self.movingToY):

                if(self.pos[1] <= self.movingToY):

                    new_pos = (self.pos[0], self.pos[1] + 1)

                else:

                    new_pos = (self.pos[0], self.pos[1] + -1)

            if(self.pos[0] == self.movingToX and self.pos[1] == self.movingToY):
                self.carrying = 1


        #carry the box back to the stack
        if(self.carrying == 1):

            if(self.pos[0] != 0):

                new_pos = (self.pos[0] - 1, self.pos[1])

            else:

                if(self.pos[1] > self.stacks):

                    new_pos = (self.pos[0], self.pos[1] - 1)

                elif(self.pos[1] < self.stacks):

                    new_pos = (self.pos[0], self.pos[1] + 1)

        self.model.grid.move_agent(self,new_pos)

    def dropOff(self):
        self.carrying = 0
        self.stacks += 1

    def stay(self):
        print("Staying")
