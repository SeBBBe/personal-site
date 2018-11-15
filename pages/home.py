from htmlwriter import *
from elements import *

class Home:
    def __init__(self):
        self.page = HtmlWriter("index.html")

    def generate(self):
        self.page.writeline("<!doctype html>")
        self.page.pushtag("html")

        PageHead().generate(self.page)

        body = PageElement("body")
        p = Paragraph("Hello world!")
        body.insert(p)
        body.generate(self.page)

        self.page.close()
