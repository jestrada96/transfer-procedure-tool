globals().clear()
from openpyxl import load_workbook

from classes.valve2 import Valve2
from classes.valve3 import Valve3

wb = load_workbook(filename = 'Valves.xlsx')
ws = wb['Connections']
valve_column=ws["B3:B200"]
destinations=ws["C3:E200"]

node_dict = {}

for row in valve_column:
    for cell in row:
        if cell.value: 
            node_dict[cell.value] = Valve3(cell.value)

for node, destination_row in zip(node_dict.values(), destinations):
    for destination_cell in destination_row:
        if destination_cell.value in node_dict:
            # if destination_cell.value:
                node.connect(node_dict[destination_cell.value])

# for con in node_dict["APVP-WT-V-611"].connections:
#      print(con.EIN())
     
                