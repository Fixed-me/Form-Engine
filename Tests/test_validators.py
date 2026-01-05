from Core.validators import Required
from Core.errors import ValidationError

def test_required_fails_on_empty_string():
    v = Required()
    error = v("")
    assert isinstance(error, ValidationError)

def test_required_passes_on_value():
    v = Required()
    error = v("abc")
    assert error is None
