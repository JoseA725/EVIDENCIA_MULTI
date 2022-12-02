import mesa
from agent import RobotAgent
from box import BoxAgent
from stack import StackAgent
import time


class BoxModel(mesa.Model):

    def __init__(self, N, width, height, K):
        self.boxCoords = []
        self.num_agents = N
        self.num_box = K
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.SimultaneousActivation(self)
        self.tiempo = time.time()

        #setup agents on grid
        for i in range(self.num_agents):
            a = RobotAgent(i, self)
            self.schedule.add(a)
            self.grid.place_agent(a, (0,i))

        # setup stacks
        for i in range(height):
            s = StackAgent(i + N + K, self)
            self.schedule.add(s)
            z = (0, i)
            self.grid.place_agent(s, (z))

        #setup boxes
        for i in range(self.num_box):

            b = BoxAgent(i + N, self)
            self.schedule.add(b)
            z = self.grid.find_empty()
            self.boxCoords.append(z)
            self.grid.place_agent(b, (z))

    # Calls the steps functions in the agents
    def step(self):
        self.schedule.step()
        tiempoFinal = time.time()
        print(tiempoFinal - self.tiempo)
