import mesa
from agent import RobotAgent

class BoxAgent(mesa.Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.destroy = 0

    def step(self):
        #print("in")
        if(self.destroy > 0):
            print("FOUND BOX")
            self.model.grid.remove_agent(self)

    def move(self):
        print()
