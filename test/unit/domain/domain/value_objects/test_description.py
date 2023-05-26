from api.domain.value_objects.description import Description
import pytest

# Test VO Description, business rules:
# Description basic method: get -> returns the value
# should be immutable
# should be comparable
# should be a string not empty


def test_description_should_be_a_string_not_empty():
    with pytest.raises(TypeError):
        Description(1)

    with pytest.raises(ValueError):
        Description("")


def test_description_should_be_immutable():
    description = Description("description")
    with pytest.raises(AttributeError):
        description.value = "description2"


def test_description_should_be_comparable():
    description_1 = Description("description")
    description_2 = Description("description")
    assert description_1 == description_2


def test_description_get():
    description = Description("description")
    assert description.get() == "description"
