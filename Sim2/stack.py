import mesa


class StackAgent(mesa.Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.size = 1

    def step(self):
        #print("in")
        if(self.size < 6):
            gridmate = self.model.grid.get_cell_list_contents([self.pos])
            print(len(gridmate), "GRRINDMATES")
            if len(gridmate) > 1:
                self.size += 1


    def move(self):
        print()