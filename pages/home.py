from htmlwriter import *

class Page_Home:
    def __init__(self):
        self.page = HtmlWriter("index.html")

    def generate(self):
        self.page.writeline("<!doctype html>")
        self.page.pushtag("html")
        self.page.pushtag("head")
        self.page.pushtag("title")
        self.page.writeline("Sebastian Fabian")
        self.page.poptag(2)
        self.page.pushtag("body")
        self.page.pushtag("p")
        self.page.writeline("Hello world!")
        self.page.close()