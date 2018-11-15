from elements import *

class NavBar:
    def generate(self, writer):
        div = Div()
        home = Hyperlink("index.html")
        home.insert(PageElement("", "", "Home"))
        div.insert(home)
        div.generate(writer)