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
        head.insert(Stylesheet("main.css"))
        head.insert(Stylesheet("buttons.css"))
        head.insert(Favicon())
        head.generate(self.page)

        navbar = NavBar()
        navbar.generate(self.page)

        body = PageElement("body")
        coverdiv1 = Div("coverdiv1")
        name = Paragraph("Sebastian Fabian", "class=\"coverhugetext\"")
        subtitle = Paragraph("Professional Software Engineer (M.Sc)", "class=\"coversubtitle\"")
        textcoverdiv1 = Div("covertext")
        textcoverdiv1.insert(name)
        textcoverdiv1.insert(subtitle)
        coverdiv1.insert(Div("distance"))
        coverdiv1.insert(textcoverdiv1)
        body.insert(coverdiv1)

        coverdiv2 = Div("coverdiv2")
        about = Paragraph("Software professional with an M.Sc in Engineering and an eye for details. I never let go of the whole picture, but enjoy making the smallest pieces fit intricately together. During my studies I worked part-time in sales, which has given me an excellent hand with people and improved communication and cooperation skills, which shows in my work driving product testability in my current position. My studies concluded in 2016 with my master thesis concerning route prediction, which resulted in a patented algorithm.", "class=\"coverbread\"")
        textcoverdiv2 = Div("covertext")
        textcoverdiv2.insert(about)
        coverdiv2.insert(Div("distance"))
        coverdiv2.insert(textcoverdiv2)
        body.insert(coverdiv2)

        coverdiv3 = Div("coverdiv3")
        construction = Paragraph("This site is a hobby project in progress! I'll spend my weekends working on it :)", "class=\"coverbread\"")
        textcoverdiv3 = Div("covertext")
        textcoverdiv3.insert(construction)
        coverdiv3.insert(Div("distance"))
        coverdiv3.insert(textcoverdiv3)
        coverdiv3.insert(Div("coverdiv3img"))
        body.insert(coverdiv3)

        body.generate(self.page)

        self.page.close()
