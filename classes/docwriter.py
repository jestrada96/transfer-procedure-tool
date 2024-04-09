from docx import Document

class DocWriter():
    def __init__(self, name="MyDoc"):
        self.name = name
        self.doc = Document()
        self.doc.add_heading(self.name, 0)
        
    def addHeading(self, text, lvl = 1):
        print(text)
        self.doc.add_heading(text, lvl)

    def addText(self, text):
        print(text)
        if text:
            self.doc.add_paragraph(text)

    def save(self, filename= "PrintedRoute.docx"):
        self.doc.save(filename)