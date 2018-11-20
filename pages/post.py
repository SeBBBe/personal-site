from htmlwriter import *
from elements import *


class Post:
    def __init__(self, source):
        self.source = source
        with open(source) as f:
            self.title = f.readline().rstrip('\n')
            self.date = f.readline().rstrip('\n')
            self.description = f.readline().rstrip('\n')
            self.imagesource = f.readline().rstrip('\n')
        self.filename = self.title.replace(" ", "-").replace("/", "-").replace("\n", "")
        self.filename = (self.filename[:75] + '..') if len(self.filename) > 75 else self.filename
        self.filename += ".html"
        self.page = HtmlWriter(self.filename)
        self.prev = PostMeta()
        self.next = PostMeta()
        self.sig_div = Table(1, 2, "collapsetable")
        self.sig_div.insertat(0, 0, Image("img/profile.jpg", "32px", "sigimg"))
        self.sig_div.insertat(0, 1, Paragraph("<i>Sebastian Fabian | " + self.date + "</i>", "class=\"sigtext\""))

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
        body.insert(PageElement("style", "", "div.coverimg { background-image: url(\"" + self.imagesource + "\");}"))
        coverimg = Div("coverimg", self.imagesource)
        title = Paragraph("", "class=\"coversubtitle\"")
        title.insert(PageElement("span", "class=\"whitebkg\"", self.title))
        textcoverdiv1 = Div("covertext")
        textcoverdiv1.insert(title)
        coverimg.insert(Div("distance"))
        coverimg.insert(textcoverdiv1)

        body.insert(coverimg)

        #blogdiv = Div("blogdiv")
        #blogdiv.insert(Div("blogtitledistance"))
        textdiv = Div("blogtext")
        textdivinner = Div("blogtextinner")
        self.parsemarkdown(textdivinner)
        textdiv.insert(textdivinner)

        navdiv = Div("navdiv")

        if self.prev.title != "":
            prev = Hyperlink(self.prev.link)
            prev.content = self.prev.title + " <<"
            navdiv.insert(prev)
            navdiv.insert(PageElement("", "", "&nbsp"))

        toc = Hyperlink("blog.html")
        toc.content = "Table of Contents"
        navdiv.insert(toc)

        if self.next.title != "":
            next = Hyperlink(self.next.link)
            next.content = ">> " + self.next.title
            navdiv.insert(PageElement("", "", "&nbsp"))
            navdiv.insert(next)

        textdiv.insert(navdiv)

        #blogdiv.insert(textdiv)
        #blogdiv.insert(Div("distance"))
        body.insert(textdiv)

        body.insert(Links())
        body.insert(Contact())

        body.generate(self.page)

        self.page.close()

    def parsemarkdown(self, parent):
        with open(self.source) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        i = 0
        for line in content:
            if line == "":
                pass
            if i == 0:
                title = Paragraph(line, "class=\"blogtitle\"")
                parent.insert(title)
            elif i == 1:
                parent.insert(self.sig_div)
                parent.insert(Paragraph(""))
                if self.prev.title != "":
                    p = Paragraph("")
                    prev = Hyperlink(self.prev.link)
                    prev.content = "Previous post: " + self.prev.title
                    p.insert(prev)
                    parent.insert(p)
                if self.next.title != "":
                    p = Paragraph("")
                    next = Hyperlink(self.next.link)
                    next.content = "Next post: " + self.next.title
                    p.insert(next)
                    parent.insert(p)
                parent.insert(Div("half_small_distance"))
            elif i <= 3:
                pass
            else:
                p = PageElement("", "", line)
                parent.insert(p)
            i += 1


class PostMeta:
    def __init__(self):
        self.title = ""
        self.link = ""
