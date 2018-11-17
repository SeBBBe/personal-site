class PageElement:
    def __init__(self, tag, params="", content="", close=True, newline=True):
        self.inner = []
        self.tag = tag
        self.params = params
        self.content = content
        self.close = close
        self.newline = ""
        if newline:
            self.newline = "\n"

    def insert(self, elem):
        self.inner.append(elem)

    def generate(self, writer):
        if self.tag != "":
            writer.write("<" + self.tag + (" " + self.params if self.params != "" else "") + ">" + self.newline)
        if self.content != "":
            writer.write(self.content + self.newline)
        for elem in self.inner:
            elem.generate(writer)
        if self.tag != "" and self.close:
            writer.write("</" + self.tag + ">" + self.newline)