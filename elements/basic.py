#!/usr/bin/env python
# -*- coding: utf-8 -*-

from elements import PageElement


class PageHead(PageElement):
    def __init__(self):
        super().__init__("head")

    def generate(self, writer):
        writer.writeline("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />")
        writer.writeline("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">")
        title = PageElement("title", "", "Sebastian Fabian")
        self.insert(title)
        super().generate(writer)


class Favicon:
    @staticmethod
    def generate(writer):
        writer.writeline("<link rel=\"apple-touch-icon\" sizes=\"180x180\" href=\"/apple-touch-icon.png\">")
        writer.writeline("<link rel=\"icon\" type=\"image/png\" sizes=\"32x32\" href=\"/favicon-32x32.png\">")
        writer.writeline("<link rel=\"icon\" type=\"image/png\" sizes=\"16x16\" href=\"/favicon-16x16.png\">")
        writer.writeline("<link rel=\"manifest\" href=\"/site.webmanifest\">")
        writer.writeline("<link rel=\"mask-icon\" href=\"/safari-pinned-tab.svg\" color=\"#5bbad5\">")
        writer.writeline("<meta name=\"msapplication-TileColor\" content=\"#da532c\">")
        writer.writeline("<meta name=\"theme-color\" content=\"#ffffff\">")


class Paragraph(PageElement):
    def __init__(self, text, param=""):
        super().__init__("p", param, text)


class Hyperlink(PageElement):
    def __init__(self, reference, tabbed=False):
        super().__init__("a", ("target=\"_blank\" " if tabbed else "") + "href=\"" + reference + "\"", "", True, False)


class Div(PageElement):
    def __init__(self, divclass="", imagesource=""):
        super().__init__("div", ("class=\"" + divclass + "\" " if divclass != "" else "") +
                         ("background=\"" + imagesource + "\"" if imagesource != "" else ""))


class Stylesheet(PageElement):
    def __init__(self, filename):
        super().__init__("link", "rel=\"stylesheet\" type=\"text/css\" href=\"" + filename + "\"", "", False)


class Image(PageElement):
    def __init__(self, url, height, divclass=""):
        super().__init__("img", ("class=\"" + divclass + "\" " if divclass != "" else "") + "src=\"" + url + "\"" + " style=\"height:" + height + ";\"", "", False, False)


class Glyphicon(PageElement):
    def __init__(self, icon):
        super().__init__("span", "class=\"glyphicon glyphicon-" + icon + "\"")
