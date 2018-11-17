import os
from htmlwriter import *
from elements import *
from pages import Post

class Blog:
    def __init__(self):
        self.filename = "blog.html"
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
        title = Paragraph("Table of Contents", "class=\"blogtitle\"")
        textdivinner.insert(title)

        self.generatePosts(textdivinner)

        textdiv.insert(textdivinner)
        blogdiv.insert(textdiv)
        body.insert(blogdiv)

        body.generate(self.page)

        self.page.close()

    def generatePosts(self, parent):
        files = os.listdir("content")
        files.sort()
        for filename in files:
            if (filename.split('.'))[-1] != "html":
                continue
            post = Post("content/" + filename)
            post.generate()
            link = Hyperlink(post.filename)
            link.insert(PageElement("", "", "<i>" + post.date + "</i> " + post.title))
            parent.insert(link)
            parent.insert(PageElement("br", "", "", False))
