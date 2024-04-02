from docx import Document

class DocWriter():
    def __init__(self, name="MyDoc"):
        self.doc = Document()
        self.name = name

    def makeDoc(self):   
        self.doc.add_heading(self.name, 0)
        
    def addHeading(self, text):
        self.doc.add_heading(text, 1)

    def addText(self, text):
        if text:
            self.doc.add_paragraph(text)

    def save(self):
        self.doc.save('PrintedRoute.docx')