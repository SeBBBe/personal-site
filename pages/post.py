from htmlwriter import *
from elements import *


class Post:
    def __init__(self, source):
        self.source = source
        with open(source) as f:
            self.title = f.readline()
            self.date = f.readline()
        self.filename = self.title.replace(" ", "-").replace("/", "-").replace("\n", "")
        self.filename = (self.filename[:75] + '..') if len(self.filename) > 75 else self.filename
        self.filename += ".html"
        self.page = HtmlWriter(self.filename)

    def generate(self):
        self.page.writeline("<!doctype html>")
        self.page.pushtag("html")

        head = PageHead()
        head.insert(Stylesheet("main.css"))
        head.insert(Stylesheet("buttons.css"))
        head.insert(Stylesheet("blog.css"))
        head.generate(self.page)

        navbar = NavBar()
        navbar.generate(self.page)

        body = PageElement("body")
        blogdiv = Div("blogdiv")
        blogdiv.insert(Div("blogtitledistance"))
        textdiv = Div("blogtext")
        textdivinner = Div("blogtextinner")
        self.parsemarkdown(textdivinner)
        textdiv.insert(textdivinner)
        blogdiv.insert(textdiv)
        body.insert(blogdiv)

        body.generate(self.page)

        self.page.close()

    def parsemarkdown(self, parent):
        with open(self.source) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        i = 0
        for line in content:
            if line == "":
                continue
            if i == 0:
                title = Paragraph(line, "class=\"blogtitle\"")
                parent.insert(title)
            elif i == 1:
                published = Paragraph("Published: " + line + "<br>Author: Sebastian Fabian", "class=\"blogdate\"")
                parent.insert(published)
            else:
                p = PageElement("", "", line)
                parent.insert(p)
            i += 1
