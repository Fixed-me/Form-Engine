# user_code.py
from Core.Form import Form
from Core.Field import Url, Bool

class RegisterForm(Form):
    email = Url()
    password = Bool(bool=True)

good_data = {
    "email": "https://stackoverflow.com/",
    "password": "True"
}

form = RegisterForm(good_data)

print(form.is_valid())
print(form.errors)