from Core.errors import ValidationError

class NotInList:
    def __init__(self, list, Notinlist):
        self.list = list
        self.Notinlist = Notinlist

    def __call__(self, value):
        if value in self.list:
                return ValidationError(
                    code="List",
                    message="List in origin List",
                    meta={"List": self.list, "inList": self.Notinlist}
            )
        return None