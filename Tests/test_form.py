from Core.form import Form
from Core.field import StringField
from Core.validators import Required

class TestForm(Form):
    def __init__(self, data):
        super().__init__(data)
        self.add_field("name", StringField(validators=[Required()]))
