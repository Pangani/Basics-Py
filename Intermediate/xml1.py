import xml.sax

class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        self.current = name
        if self.current == "person":
            print("---person---")
            id = attrs["id"]
            print(f"ID: {id}")

    def endElement(self, name):
        if self.current == "name":
            print(f"Name: {self.name}")
        elif self.current == "age":
            print("Age: ", self.age)
        elif self.current == "weight":
            print("Weight: ", self.weight)
        elif self.current == "height":
            print("Height: ", self.height)
        self.current = ""

    def characters(self, content):
        if self.current == "name":
            self.name = content.strip()
        elif self.current == "age":
            self.age = int(content.strip())
        elif self.current == "weight":
            self.weight = float(content.strip())
        elif self.current == "height":
            self.height = float(content.strip())

handler = GroupHandler()

parser = xml.sax.make_parser()
parser.setContentHandler(handler)

parser.parse("group.xml")
    