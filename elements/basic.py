from elements import PageElement

class PageHead(PageElement):
    def __init__(self):
        super().__init__("head")
    def generate(self, writer):
        title = PageElement("title", "", "Sebastian Fabian")
        self.insert(title)
        super().generate(writer)

class Paragraph(PageElement):
    def __init__(self, text):
        super().__init__("p", "", text)

class Hyperlink(PageElement):
    def __init__(self, reference):
        super().__init__("a", "href=\"" + reference + "\"", "")