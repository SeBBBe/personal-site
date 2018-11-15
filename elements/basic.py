from elements import PageElement

class PageHead:
    def generate(self, writer):
        head = PageElement("head")
        title = PageElement("title", "", "Sebastian Fabian")
        head.insert(title)
        head.generate(writer)

class Paragraph:
    def __init__(self, text):
        self.elem = PageElement("p", "", text)
    def generate(self, writer):
        self.elem.generate(writer)