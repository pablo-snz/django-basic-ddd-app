import pytest
from django_basic_ddd_app.api.domain.value_objects.rating import Rating

# Test VO Rating, business rules:
# basic method: get -> returns the value
# should be between 0 and 5
# should be a float
# should be immutable
# should be comparable


def test_rating_should_be_between_0_and_5():
    with pytest.raises(ValueError):
        Rating(5.1)


def test_rating_should_be_rounded_to_the_nearest_0_5():
    rating = Rating(4.1)
    assert rating.get() == 4.1


def test_rating_should_be_a_float():
    with pytest.raises(TypeError):
        Rating("string")


def test_rating_should_be_immutable():
    rating = Rating(4.0)
    with pytest.raises(AttributeError):
        rating.value = 5.0


def test_rating_should_be_comparable():
    rating_1 = Rating(4.0)
    rating_2 = Rating(4.0)
    assert rating_1 == rating_2
    assert rating_1 <= rating_2
    assert rating_1 >= rating_2
    assert not rating_1 != rating_2
    assert rating_1 <= 4.0
    assert rating_2 >= 4.0
    assert rating_1 < 4.1
    assert rating_2 > 3.9
