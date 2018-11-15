class PageElement:
    def __init__(self, tag, params="", content="", close=True):
        self.inner = []
        self.tag = tag
        self.params = params
        self.content = content
        self.close = close

    def insert(self, elem):
        self.inner.append(elem)

    def generate(self, writer):
        if self.tag != "":
            writer.writeline("<" + self.tag + (" " + self.params if self.params != "" else "") + ">")
        if self.content != "":
            writer.writeline(self.content)
        for elem in self.inner:
            elem.generate(writer)
        if self.tag != "" and self.close:
            writer.writeline("</" + self.tag + ">")