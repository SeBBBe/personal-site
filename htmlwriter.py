#!/usr/bin/env python
# -*- coding: utf-8 -*-

class HtmlWriter:
    def __init__(self, filename):
        self.file = open("output/" + filename, "w+")
        self.tagendings = []

    def writeline(self, line):
        self.write(line + "\n")

    def write(self, line):
        self.file.write(line.replace("å", ""))

    def pushtag(self, tag, params = ""):
        self.writeline("<" + tag + (" " + params if params != "" else "") + ">")
        self.tagendings.append("</" + tag + ">")

    def poptag(self, n = 1):
        for x in range(n):
            self.writeline(self.tagendings.pop())

    def close(self):
        while (self.tagendings):
            self.poptag()
        self.file.close()