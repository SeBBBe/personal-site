import os
from htmlwriter import *
from elements import *
from pages import *


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
        textdivinner.insert(Div("half_small_distance"))

        self.generateposts(textdivinner)

        textdiv.insert(textdivinner)
        blogdiv.insert(textdiv)
        blogdiv.insert(Div("distance"))
        body.insert(blogdiv)

        body.insert(Links())
        body.insert(Contact())

        body.generate(self.page)

        self.page.close()

    @staticmethod
    def generateposts(parent):
        files = os.listdir("content")
        files.sort()
        posts = []
        for filename in files:
            if (filename.split('.'))[-1] != "html":
                continue
            post = Post("content/" + filename)
            postdiv = Div("post")
            title = Paragraph("", "class=\"posttitle\"")
            link = Hyperlink(post.filename)
            link.insert(PageElement("", "", post.title))
            title.insert(link)
            postdiv.insert(title)
            descdiv = Div("")
            imgdiv = Div("imgdiv")
            imgdiv.insert(Image(post.imagesource, "128px"))
            descdiv.insert(imgdiv)
            descdiv.insert(Paragraph(post.description, "class=\"postdescription\""))
            postdiv.insert(descdiv)
            sig_div = Table(1, 2, "collapsetable")
            sig_div.insertat(0, 0, Image("img/profile.jpg", "32px", "sigimg"))
            sig_div.insertat(0, 1, Paragraph("<i>Sebastian Fabian | " + post.date + "</i>", "class=\"sigtext\""))
            postdiv.insert(sig_div)
            parent.insert(postdiv)
            parent.insert(Div("small_distance"))
            posts.append(post)
        i = 0
        while i < len(posts):
            post = posts[i]
            if i > 0:
                post.prev.title = posts[i-1].title
                post.prev.link = posts[i-1].filename
            if i < (len(posts) - 1):
                post.next.title = posts[i+1].title
                post.next.link = posts[i+1].filename
            i += 1
        for post in posts:
            post.generate()
