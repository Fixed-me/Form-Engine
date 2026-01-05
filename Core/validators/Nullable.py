from Core.errors import ValidationError

class Nullable:
    def __init__(self, nullable):
        self.nullable = nullable
    
    def __call__(self, value):
        if value == 0:
            return ValidationError (
                code="nullable",
                message="not nullable",
                meta={"nullable": self.nullable}
            )
        return None