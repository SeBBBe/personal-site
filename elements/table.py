from elements import PageElement


class Table(PageElement):
    def __init__(self, rows, cols):
        super().__init__("table")
        self.rows = rows
        self.cols = cols
        self.elems = {}

    def insertat(self, row, col, elem):
        key = str(row) + ":" + str(col)
        self.elems[key] = elem

    def generate(self, writer):
        for row in range(self.rows):
            tr = PageElement("tr")
            for col in range(self.cols):
                td = PageElement("td")
                key = str(row) + ":" + str(col)
                if key in self.elems:
                    td.insert(self.elems[key])
                tr.insert(td)
            super().insert(tr)
        super().generate(writer)