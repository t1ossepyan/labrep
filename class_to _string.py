class StringCollector:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("ВВедите че нибудь: ")

    def output(self):
        print(self.text.upper())

object = StringCollector()

object.getString()
object.output()