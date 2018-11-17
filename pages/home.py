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
        subtitle = Paragraph("Software Engineer", "class=\"coversubtitle\"")
        textcoverdiv1 = Div("covertext")
        textcoverdiv1.insert(name)
        textcoverdiv1.insert(subtitle)
        coverdiv1.insert(Div("distance"))
        coverdiv1.insert(textcoverdiv1)
        body.insert(coverdiv1)

        coverdiv2 = Div("coverdiv2")
        about = Paragraph(
            "I am a software professional with an M.Sc in Engineering and an eye for details. During my studies I worked part-time in sales, which has given me an excellent hand with people, something I can put to great use in my current work driving product performance and scalability. My studies concluded in 2016 with my master thesis concerning route prediction at a major automotive manufacturer, which resulted in a patented algorithm.",
            "class=\"coverbread\"")
        about2 = Paragraph("This site was created as a hobby project. Although no expert in design by any means, I greatly enjoy building things. It is generated by Python code available from my GitHub.", "class=\"coverbread\"")
        textcoverdiv2 = Div("covertext")
        textcoverdiv2.insert(about)
        textcoverdiv2.insert(about2)
        coverdiv2.insert(Div("distance"))
        coverdiv2.insert(textcoverdiv2)
        body.insert(coverdiv2)

        coverdiv3 = Div("coverdiv3")
        construction = Paragraph("This site is a hobby project in progress! I will spend my weekends working on it :)", "class=\"coverbread\"")
        textcoverdiv3 = Div("covertext")
        textcoverdiv3.insert(construction)
        coverdiv3.insert(Div("distance"))
        coverdiv3.insert(textcoverdiv3)
        coverdiv3.insert(Div("coverdiv3img"))
        body.insert(coverdiv3)

        contact = Div("contact")
        iconDistance = PageElement("", "", "    ", False, False)
        github = Hyperlink("http://www.github.com/sebbbe")
        github.insert(Image("img/github.png", "64px"))
        linkedin = Hyperlink("http://www.linkedin.com/in/sebastianfabian")
        linkedin.insert(Image("img/linkedin.png", "64px"))
        contact.insert(Div("small_distance"))
        contact.insert(Paragraph("Catch me at:"))
        contact.insert(github)
        contact.insert(iconDistance)
        contact.insert(linkedin)
        contact.insert(iconDistance)
        contact.insert(Image("img/contact.png", "64px"))
        body.insert(contact)

        body.generate(self.page)

        self.page.close()
