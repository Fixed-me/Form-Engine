
# Form Engine

**Work in Progress**  
This Form Engine is currently under active development.  
APIs, validation behavior, and internal structures may change.

---

## Overview

The Form Engine is a modular Python framework for defining, validating, and processing forms.  
It is built around **Fields**, **Validators**, and a central **Form** class that ties everything together.

The goal is to make forms **declarative**, **extensible**, and **easy to test**.

---

## Core Concepts

### Form

A `Form` is a class composed of multiple Fields.

```python
from Engine import Form, String, Integer

class UserForm(Form):
    name = String(minLength=3)
    password = Integer(validators=[Min(8)])
````

* Each form automatically collects all defined fields
* Validation is performed field by field
* Errors are returned in a structured format

---

### Fields

Fields represent individual input values, including type handling, conversion, and validation.

Currently available Fields:

* `Bool`
* `Date`
* `Float`
* `Integer`
* `List`
* `String`

Example:

```python
name = String()
age = Integer()
```

---

### Validators

Validators ensure that values meet specific rules.
They can be used **explicitly** or via **built-in (standard) validators**.

#### Explicit Validators

```python
from Engine import String
from Engine.Validators import MinLength

name = String(validators=[MinLength(3)])
```

#### Standard Validators (Shortcuts)

Many validators are available directly as keyword arguments on a Field:

```python
name = String(minLength=3)
email = String(email=True)
```

Internally, these arguments are automatically converted into validator instances.

---

## Available Validators

### General

* `Equals`
* `NotEquals`
* `InList`
* `NotInList`
* `Choices`
* `Pattern`
* `Regex`

### String

* `MinLength`
* `MaxLength`
* `Lowercase`
* `Uppercase`
* `Email`
* `Url`

### Integer / Number

* `Min`
* `Max`

### Bool

* `Bool`

### Date / Datetime

* `BeforeDatetime`
* `AfterDatetime`
* `DateFormat`

---

## Validation Errors

Each validator returns a `ValidationError` object on failure.

Structure:

```python
ValidationError(
    code="validator_name",
    message="A default readable error message",
    meta={
        "name": expected_value
    }
)
```

Properties:

* **code**
  Machine-readable error code (e.g. for frontends or translations)

* **message**
  Human-readable default error message

* **meta**
  Additional context (e.g. expected values or limits)

---

## Example: More Complex Form

```python
from Engine import Form, String, Integer

class RegisterForm(Form):
    username = String(
        minLength=3,
        maxLength=20,
        lowercase=True
    )

    password = Integer(
        validators=[Min(8)]
    )
```

---

## Architecture (Short Overview)

* `Form`
  Coordinates fields and validation

* `Field`
  Holds type, value, validators, and standard options

* `Validator`
  Isolated validation rules, independently testable

* `ValidationError`
  Unified error representation

---

## Current Status

Basic field types implemented,

Modular validator system,

Built-in validators per field,

Documentation in progress,

Tests in progress

API not yet stable

---

## Planned Features (Ideas)

* Cross-field validation (e.g. `password == password_repeat`)
* Multilingual error messages
* Custom error messages per validator
* JSON / dict export of validation errors
* Optional strict parsing mode
* Async validation
* Schema export (e.g. for frontend usage)

---

## Contributing

Pull requests, ideas, and feedback are welcome.
Since the project is still evolving, please coordinate before making large changes.

---

## License

This project is licensed under the MIT License.

