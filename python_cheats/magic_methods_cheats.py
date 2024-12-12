class MyObject(Object):

    def __dir__(self):
        return "All attributes' name"

    def __getattr__(self, attribute):
        return "Attribute's value"

