from elements import *


class NavBar:

    @staticmethod
    def generate(writer):
        div = Div("navbar")
        spacer = Div("col-md-2 col-sm-2 col-xs-6")
        home = NavButton("home", "index.html")
        blog = NavButton("blog", "blog.html")
        div.insert(spacer)
        div.insert(spacer)
        div.insert(spacer)
        div.insert(spacer)
        div.insert(home)
        div.insert(blog)
        div.generate(writer)


class NavButton(PageElement):
    def __init__(self, text, link):
        super().__init__("div", "class=\"col-md-2 col-sm-2 col-xs-6\"")
        link = PageElement("a", "href=\"" + link + "\" class=\"btn btn-sm animated-button thar-one\"", text)
        self.insert(link)