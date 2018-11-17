from elements import PageElement
from elements import basic


class Experiences(basic.Div):
    def __init__(self, text, link):
        super().__init__("div", "class=\"col-md-2 col-sm-2 col-xs-6\"")
        link = PageElement("a", "href=\"" + link + "\" class=\"btn btn-sm animated-button thar-one\"", text)
        self.insert(link)
