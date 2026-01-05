from Core.errors import ValidationError

class MaxLength:
    def __init__(self, length):
        self.length = length
    
    def __call__(self, value):
        if len(value) > self.length:
            return ValidationError(
                code="max_length",
                message="Too long",
                meta={"max": self.length}
            )
        return None