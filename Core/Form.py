# form.py
from Core.Field import Field

class FormMeta(type):
    def __new__(cls, name, bases, attrs):
        fields = {}

        for key, value in list(attrs.items()):
            if isinstance(value, Field):
                value.name = key
                fields[key] = value
                del attrs[key]

        attrs["_fields"] = fields
        return super().__new__(cls, name, bases, attrs)


class Form(metaclass=FormMeta):
    def __init__(self, data):
        self.data = data
    
    def is_valid(self):
        self._errors = {}
        self.cleaned_data = {}

        for name, field in self._fields.items():
            raw = self.data.get(name)
            value, errs = field.clean(raw)

            if errs:
                self._errors[name] = errs
            else:
                self.cleaned_data[name] = value

        return not self._errors


    @property
    def errors(self):
        return {
            field: [e.to_dict() for e in errs]
            for field, errs in self._errors.items()
        }
