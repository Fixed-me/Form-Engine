import re
from Core.errors import ValidationError

class URL:
    def __init__(self):
        self.pattern = re.compile("https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*")
    
    def __call__(self, value):
        if not self.pattern.match(value):
            return ValidationError(
                code="Url",
                message="Invalide Url"
            )
