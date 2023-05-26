import pytest
from api.domain.value_objects.name import Name


# Test VO Name, business rules:
# Name basic method: get -> returns the value
# should be immutable
# should be comparable
# should be a string not empty


def test_name_should_be_a_string_not_empty():
    with pytest.raises(TypeError):
        Name(1)

    with pytest.raises(ValueError):
        Name("")


def test_name_should_be_immutable():
    name = Name("name")
    with pytest.raises(AttributeError):
        name.value = "name2"


def test_name_should_be_comparable():
    name_1 = Name("name")
    name_2 = Name("name")
    assert name_1 == name_2


def test_name_get():
    description = Name("name")
    assert description.get() == "name"
