import tkinter as tk
from tkinter import messagebox
import excelData as ex
import os

from classes.docWriter import DocWriter 

def makeDocumentFromRoute(source, destination, alternatives = 1):
    src = source.get()
    dst = destination.get()
    alts = 1
    try:
        alts = int(alternatives)
    except ValueError:
        messagebox.showwarning("Warning", "Valid number of alternatives not specified, showing shortest route available.")
    writer = DocWriter(src + " to " + dst + " draft procedure data:")
    #route is found here:
    routes = ex.inventory[src].routesTo(ex.inventory[dst], alts)
    #change this to use a selected route from the options instead!
    for route in routes:
        for i in range(1,len(route)-2):
            route[i].setPosition(route)
        writer.buildDocument(route)
    filename = src +"_to_"+ dst + ".docx"
    writer.save(filename)
    os.system(f'start {filename}')

def src_filter(*args):
    query = src_entry.get().lower() 
    src_dropdown['menu'].delete(0, tk.END)
    for node in nodes:
        # if query in node.lower() and (ex.inventory[node].in_tank or select_from_all):
        if query in node.lower():
            src_dropdown['menu'].add_command(label=node, command=tk._setit(source, node))

def dst_filter(*args):
    query = dst_entry.get().lower() 
    dst_dropdown['menu'].delete(0, tk.END)
    for node in nodes:
        # if query in node.lower() and (ex.inventory[node].in_tank or select_from_all):
        if query in node.lower():
            dst_dropdown['menu'].add_command(label=node, command=tk._setit(destination, node))

def main():
    window = tk.Tk()
    window.title("Waste Transfer Route Generator")
    window.geometry("800x300")

    def toggle_boolean(*args):
        if select_from_all:
            nodes = ex.inventory.keys()
            for node in nodes:
                # dst_dropdown['menu'].delete(0, tk.END)
                dst_dropdown['menu'].add_command(label=node, command=tk._setit(destination, node))
        else:
            src_filter()
            dst_filter()

    items_to_tank = set()
    for item in ex.inventory.keys():
        if ex.inventory[item].in_tank:
            items_to_tank.add(item)
    
    global nodes 
    nodes = items_to_tank

    label0 = tk.Label(window, text="Select transfer origin:")
    label0.grid(row=0, column= 0, pady = 2)

    global source
    source = tk.StringVar(window)
    global src_dropdown
    src_dropdown = tk.OptionMenu(window, source, *nodes)
    src_dropdown.grid(row=0, column= 2, pady=2)
    global src_entry
    src_entry = tk.Entry(window)
    src_entry.grid(row=0, column= 1, pady=5, padx=4)

    label1 = tk.Label(window, text="Select transfer destination:")
    label1.grid(row=2, column= 0, pady = 2)

    global destination
    destination = tk.StringVar(window)
    global dst_dropdown
    dst_dropdown = tk.OptionMenu(window, destination, *nodes)
    dst_dropdown.grid(row=2, column= 2, pady=2)
    global dst_entry
    dst_entry = tk.Entry(window)
    dst_entry.grid(row=2, column= 1, pady=5, padx=4)

    global select_from_all
    select_from_all = tk.BooleanVar()
    select_from_all.set(False)

    checkbox = tk.Checkbutton(window, text="Show all", variable=select_from_all, command = toggle_boolean)
    checkbox.grid(row=0, column=4)

    label2 = tk.Label(window, text="Enter number of route alternatives needed:")
    label2.grid(row=4, column= 0, pady = 2, padx=7)

    global alternatives 
    alternatives = tk.Entry(window)
    alternatives.grid(row=4, column= 1, columnspan=2, pady=2, sticky="ew")

    src_entry.bind("<KeyRelease>", src_filter)
    dst_entry.bind("<KeyRelease>", dst_filter)

    printButton = tk.Button(window, text="Find Routes", command=lambda: makeDocumentFromRoute(source, destination, alternatives.get()))
    printButton.grid(row=5, column= 2, pady=20, sticky="ew")
    window.mainloop()

if __name__== '__main__':   
    main()

# TO DO: FIGURE OUT DVI, FIGURE OUT SPLITS NECESSARY??