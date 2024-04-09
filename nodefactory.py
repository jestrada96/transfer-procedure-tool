globals().clear()
from openpyxl import load_workbook
from classes.valve import Valve
from classes.valve2 import Valve2
from classes.valve3 import Valve3
from classes.split import Split
from classes.nozzle import Nozzle
from classes.pump import Pump
from classes.dropleg import Dropleg
from classes.node import Node

wb = load_workbook(filename = 'Valves.xlsx')
ws = wb['Connections']
node_column=ws["B3:B200"]
class_column=ws["C3:C200"]
destinations=ws["D3:F200"]

classes = {
        "2-Way-Valve": Valve2,
        "3-Way-Valve": Valve3,
        "Split Point": Split,
        "Nozzle": Nozzle,
        "Pump": Pump,
        "": Valve,
        "Dropleg": Dropleg,
        None: Valve 
}

node_dict = {}

#Initialize Dictionary
for cell in node_column:
        if cell[0].value: 
            node_dict[cell[0].value] = None

#Populate directory with a node of class bassed on class column
for key, class_row in zip(node_dict.keys(), class_column):
    for class_cell in class_row:
        # if class_cell.value in classes.keys(): 
        node_dict[key] = classes[class_cell.value](key)

for node, destination_row in zip(node_dict.values(), destinations):
    # node.setPit();
    for destination_cell in destination_row:
        if destination_cell.value in node_dict:
            if destination_cell.value:
                node.connect(node_dict[destination_cell.value])

# for value in node_dict.values():
#     print ("\n")
#     print("connections in ", value.EIN())
#     print(type(value))
#     for connection in value.connections:
#         print(connection.EIN(), end=" ")

def getRoutes(a, b):
    src = node_dict[a]
    dst = node_dict[b]
    return src.routesTo(dst)

     
                