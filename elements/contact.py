#!/usr/bin/env python
# -*- coding: utf-8 -*-

from elements.basic import *


class Links(Div):
    def __init__(self):
        super().__init__("links")
        icondistance = PageElement("", "", "    ", False, False)
        github = Hyperlink("http://www.github.com/sebbbe", True)
        github.insert(Image("img/github.png", "100px", "imgbutton"))
        linkedin = Hyperlink("http://www.linkedin.com/in/sebastianfabian", True)
        linkedin.insert(Image("img/linkedin.png", "100px", "imgbutton"))
        self.insert(Div("small_distance"))
        self.insert(Paragraph("Catch me at:"))
        self.insert(github)
        self.insert(icondistance)
        self.insert(linkedin)
        self.insert(Div("small_distance"))


class Contact(Div):
    def __init__(self):
        super().__init__("contact")
        self.insert(Div("small_distance"))
        self.insert(Image("img/contact.png", "100px"))
        self.insert(Div("small_distance"))