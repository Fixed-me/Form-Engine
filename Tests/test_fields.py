from Core.field import StringField
from Core.validators import Required, MinLength

def test_field_collects_multiple_errors():
    field = StringField(validators=[
        Required(),
        MinLength(3),
    ])

    errors = field.validate("")

    assert len(errors) == 2
