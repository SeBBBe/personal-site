from elements import PageElement

class PageHead(PageElement):
    def __init__(self):
        super().__init__("head")
    def generate(self, writer):
        title = PageElement("title", "", "Sebastian Fabian")
        self.insert(title)
        super().generate(writer)

class Paragraph(PageElement):
    def __init__(self, text, param=""):
        super().__init__("p", param, text)

class Hyperlink(PageElement):
    def __init__(self, reference):
        super().__init__("a", "href=\"" + reference + "\"", "")

class Div(PageElement):
    def __init__(self, divclass=""):
        super().__init__("div", ("class=\"" + divclass + "\"" if divclass != "" else ""))

class Stylesheet(PageElement):
    def __init__(self, filename):
        super().__init__("link", "rel=\"stylesheet\" type=\"text/css\" href=\"" + filename + "\"", "", False)