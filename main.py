from classes.node import Node
from classes.valve2 import Valve2
from classes.valve3 import Valve3

# fix connections list max count and back connections checker later, 
# for now focus on functionality and assume connections will be accurate and logical

# Make connects_to part of Nodes not Valves, will require refactor to have Nodes use connections?
# How do you want to implement creating a node?
# Make it similar to a double valve for a nozzle? give it "1 way" for pumps and tkr and blanks??

# dummy = Valve2("---")
valve806 = Valve3("APVP-WTL-V-806")
valve609 = Valve3("APVP-WTL-V-609")
valve803 = Valve3("APVP-WTL-V-803")
valve802 = Valve3("APVP-WTL-V-802")
valve804 = Valve3("APVP-WTL-V-804")
valve805 = Valve3("APVP-WTL-V-805")
valve801 = Valve3("APVP-WTL-V-801")
valve610 = Valve3("APVP-WTL-V-808")
valve603 = Valve3("APVP-WTL-V-603")
valve601 = Valve3("APVP-WTL-V-601")
valve602 = Valve3("APVP-WTL-V-602")
valve606 = Valve3("APVP-WTL-V-606")
valve607 = Valve3("APVP-WTL-V-607")
valve608 = Valve3("APVP-WTL-V-608")
valve611 = Valve3("APVP-WTL-V-611")
valve612 = Valve3("APVP-WTL-V-612")
valve613 = Valve3("APVP-WTL-V-613")
valve614 = Valve3("APVP-WTL-V-614")
valve615 = Valve3("APVP-WTL-V-615")
valve616 = Valve3("APVP-WTL-V-616")
valve617 = Valve3("APVP-WTL-V-617")
valve618 = Valve3("APVP-WTL-V-618")
valve619 = Valve3("APVP-WTL-V-619")
valve620 = Valve3("APVP-WTL-V-620") 
jumperP = Valve2("jummperP")
split_01 = Valve3("split")


valve806.connect(valve609)
valve609.connect()
valve803.connect(valve802, valve802)
split_01.connect(valve803, valve804)
valve802.connect(valve801,valve805)
valve804.connect()
valve805.connect()
valve801.connect(valve802)
valve610.connect()
valve603.connect(valve619, valve601,valve613)
valve601.connect(valve611, valve602)
valve602.connect(valve601, valve612, valve614)
valve606.connect(valve608)
valve607.connect(valve608)
valve611.connect(valve606)
valve612.connect()
valve613.connect()
valve614.connect()
valve615.connect(valve607)
valve616.connect()
valve617.connect()
valve618.connect()
valve619.connect(valve609, valve803,)
valve620.connect(valve804, valve606) 

for route in valve614.routes_to(valve615):
    print([node.ein for node in route]) 

