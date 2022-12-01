from model import *
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
import mesa


def agent_portrayal(agent):
    portrayal = {"Filled": "true"}
    if agent.unique_id < 5:
        portrayal["Shape"] = "circle"
        portrayal["Color"] = "green"
        portrayal["Layer"] = 0
        portrayal["r"] = 0.5
    elif agent.unique_id >= 5 and agent.unique_id < 25:
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "red"
        portrayal["Layer"] = "1"
        portrayal["w"] = 0.2
        portrayal["h"] = 0.2
        portrayal["xAlign"] = 0.5
        portrayal["yAlign"] = 0.5
    else:
        portrayal["Shape"] = "rect"
        portrayal["Color"] = "blue"
        portrayal["Layer"] = "1"
        portrayal["w"] = 0.2
        portrayal["h"] = 0.2
        portrayal["xAlign"] = 0.5
        portrayal["yAlign"] = 0.5
    return portrayal

grid = mesa.visualization.CanvasGrid(agent_portrayal, 10, 10, 500, 500)
server = mesa.visualization.ModularServer(
    BoxModel, [grid], "Box Model", {"N": 5, "width": 10, "height": 10, "K": 20}
)
server = ModularServer(BoxModel,
                       [grid],
                       "Box Model",
                       {"N":5, "width":10, "height":10, "K": 20})
server.port = 8520 # The default
server.launch()