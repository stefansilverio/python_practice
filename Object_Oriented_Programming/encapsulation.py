#  objects group variables and methods in a single unit - the object
#  client = code outside the class that uses the object
#  encapsulation - hiding a class's internal data to prevent client from access
#  use naming conventions to distinguish private variables and methods
#  might want to change implementation of code later or afraid that client will
#  break client code by changing state


class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        #  clients can use this
        pass

    def _unsafe_method(self):
        #  clients shouldn't use this
        pass
