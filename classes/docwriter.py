from docx import Document
from classes.node import Node
from docx.shared import Pt
from docx.shared import RGBColor

class DocWriter():
    def __init__(self, name="MyDoc"):
        self.name = name
        self.doc = Document()
        run = self.doc.add_heading("", 1).add_run()
        font = run.font
        font.name = "Times New Roman"
        font.size = Pt(11)
        font.color.rgb = RGBColor(0x42,0x42,0x42)
        run.add_text(self.name)
        
    def makeSection(self, name, instruction = None):
        paragraph = self.doc.add_paragraph()
        paragraph.paragraph_format.space_after = Pt(1)
        paragraph.paragraph_format.space_before = Pt(1)
        section_name = paragraph.add_run(name)
        section_name.font.bold = True
        section_name.font.name = "Times New Roman"
        section_name.font.size = Pt(11)
        prompt = paragraph.add_run(instruction)
        prompt.font.name = "Times New Roman"
        prompt.font.size = Pt(11)
        return paragraph

    def save(self, filename= "PrintedRoute.docx"):
        self.doc.save(filename)

    def buildDocument(self, route):
        route_list = self.makeSection("Route List: ", "Valves in route (reference only):")
        for node in route:
            if node.show:
                route_list.add_run("\n")
                route_list.add_run(node.EIN())
        heaters = self.makeSection("Section 5.5.3 heaters: " ,"Replace existing data with the following:")
        pits = self.makeSection("Steps 5.17.9: ","Replace existing data with the following:")
        Checklist1 = self.makeSection("Checklist 1: ","Replace list with:")
        Checklist3 = self.makeSection("Checklist3:","")
        Checklist4 = self.makeSection("Checklist4:","")
        Checklist5 = self.makeSection("Checklist5:","")
        Checklist6 = self.makeSection("Checklist6:","")
        Checklist7 = self.makeSection("Checklist7:","")
