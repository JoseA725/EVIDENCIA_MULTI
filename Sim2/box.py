import mesa

# object created to represent boxes
class BoxAgent(mesa.Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.destroy = 0

    def step(self):
        # if another agent makes contact destroy
        if(self.destroy > 0):
            self.model.grid.remove_agent(self)