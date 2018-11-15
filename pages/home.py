from htmlwriter import *
from elements import *

class Home:
    def __init__(self):
        self.filename = "index.html"
        self.page = HtmlWriter(self.filename)

    def generate(self):
        self.page.writeline("<!doctype html>")
        self.page.pushtag("html")

        head = PageHead()
        head.insert(Stylesheet("buttons.css"))
        head.generate(self.page)

        navbar = NavBar()
        navbar.generate(self.page)

        body = PageElement("body")
        p = Paragraph("Hello world!")
        body.insert(p)
        body.generate(self.page)

        self.page.close()
