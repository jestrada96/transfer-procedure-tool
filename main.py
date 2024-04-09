import tkinter as tk
from tkinter import messagebox
import nodefactory as nf
import os

from classes.docwriter import DocWriter 

def printRoute(source,destination, alternatives = 1):
    src = source.get()
    dst = destination.get()
    alts = 1
    try:
        alts = int(alternatives)
    except ValueError:
        messagebox.showwarning("Warning", "Valid number of alternatives not specified, showing shortest route available.")
    writer = DocWriter("Possible Routes from " + src + " to " + dst)
    routes = nf.getRoutes(src, dst)
    for route in routes:
        writer.addHeading("Route option: ")
        for node in route:
            if node.show:
                writer.addText(node.EIN())
    filename = src +"_to_"+ dst + ".docx"
    writer.save(filename)
    os.system(f'start {filename}')


def src_filter(*args):
    query = src_entry.get().lower() 
    src_dropdown['menu'].delete(0, tk.END)

    for node in nodes:
        if query in node.lower():
            src_dropdown['menu'].add_command(label=node, command=tk._setit(source, node))

def dst_filter(*args):
    query = dst_entry.get().lower() 
    dst_dropdown['menu'].delete(0, tk.END)
    
    for node in nodes:
        if query in node.lower():
            dst_dropdown['menu'].add_command(label=node, command=tk._setit(destination, node))

def main():
    root = tk.Tk()
    root.title("RouteFinderTest")
    root.geometry("500x290")
    
    global nodes
    nodes = nf.node_dict.keys()

    label0 = tk.Label(root, text="Select transfer origin:")
    label0.grid(row=0, column= 0, pady = 2)

    global source
    source = tk.StringVar(root)
    global src_dropdown
    src_dropdown = tk.OptionMenu(root, source, *nodes)
    src_dropdown.grid(row=0, column= 2, pady=2)
    global src_entry
    src_entry = tk.Entry(root)
    src_entry.grid(row=0, column= 1, pady=5, padx=4)

    label1 = tk.Label(root, text="Select transfer destination:")
    label1.grid(row=2, column= 0, pady = 2)

    global destination
    destination = tk.StringVar(root)
    global dst_dropdown
    dst_dropdown = tk.OptionMenu(root, destination, *nodes)
    dst_dropdown.grid(row=2, column= 2, pady=2)
    global dst_entry
    dst_entry = tk.Entry(root)
    dst_entry.grid(row=2, column= 1, pady=5, padx=4)

    label2 = tk.Label(root, text="Enter number of route alternatives needed:")
    label2.grid(row=4, column= 0, pady = 2, padx=7)

    global alternatives 
    alternatives = tk.Entry(root)
    alternatives.grid(row=4, column= 1, columnspan=2, pady=2, sticky="ew")

    src_entry.bind("<KeyRelease>", src_filter)
    dst_entry.bind("<KeyRelease>", dst_filter)

    printButton = tk.Button(root, text="Find Routes", command=lambda: printRoute(source, destination, alternatives.get()))
    printButton.grid(row=5, column= 2, pady=20, sticky="ew")
    root.mainloop()

if __name__== '__main__':
    main()