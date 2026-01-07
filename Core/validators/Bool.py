from Core.errors import ValidationError

class Bool:

    def __init__(self, bool):
        self.bool = bool

    def __call__(self, value):
        
        if value is not self.bool:
            return ValidationError(
                code="Bool",
                message="Bool is in some ways not Correct",
                meta=self.bool

            )
