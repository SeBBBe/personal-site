#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from elements.basic import *


class Experiences(Div):
    def __init__(self):
        super().__init__("experiences")
        self.insert(Div("small_distance"))
        titlediv = Div("covertext")
        titlediv.insert(Paragraph("Experience", "class=\"coverhugetext\""))
        self.insert(titlediv)
        self.insert(Div("half_small_distance"))
        with open('content/experience.json') as f:
            data = json.load(f)
        for experiencedata in data["experience"]:
            experience = Experience(experiencedata)
            self.insert(experience)
            self.insert(Div("small_distance"))


class Experience(Div):
    def __init__(self, json):
        super().__init__("experience")
        side = Div("experience_side")
        side.insert(Paragraph(json["title"], "class=\"experience_title\""))
        side.insert(Paragraph(json["company"], "class=\"experience_company\""))
        side.insert(Paragraph(json["time"], "class=\"experience_time\""))
        main = Div("experience_main")
        main.insert(Paragraph(json["description"]))

        self.insert(side)
        self.insert(main)