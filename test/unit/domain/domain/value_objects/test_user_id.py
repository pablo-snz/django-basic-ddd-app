import pytest
from django_basic_ddd_app.api.domain.value_objects.user_id import UserId

# Test VO Name, business rules:
# Name basic method: get -> returns the value
# should be immutable
# should be comparable
# should be a int


def test_user_id_should_be_a_string_not_empty():
    with pytest.raises(TypeError):
        UserId(1)

    with pytest.raises(ValueError):
        UserId("")


def test_user_id_should_be_immutable():
    user_id = UserId("1")
    with pytest.raises(AttributeError):
        user_id.value = "2"


def test_user_id_should_be_comparable():
    user_id_1 = UserId("1")
    user_id_2 = UserId("1")
    assert user_id_1 == user_id_2


def test_user_id_get():
    user_id = UserId("1")
    assert user_id.get() == "1"
