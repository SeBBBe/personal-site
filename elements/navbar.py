from elements import *

class NavBar:
    def generate(self, writer):
        div = Div()
        #home = Hyperlink("index.html")
        #home.insert(PageElement("", "", "Home"))
        home = NavButton("home", "index.html")
        div.insert(home)
        div.generate(writer)

class NavButton(PageElement): #<div class="col-md-3 col-sm-3 col-xs-6"> <a href="#" class="btn btn-sm animated-button thar-one">Sign up</a> </div>
    def __init__(self, text, link): #<a href="#" class="btn btn-sm animated-button thar-one">Sign up</a>
        super().__init__("div", "class=\"col-md-3 col-sm-3 col-xs-6\"")
        link = PageElement("a", "href=\"" + link + "\" class=\"btn btn-sm animated-button thar-one\"", text)
        self.insert(link)