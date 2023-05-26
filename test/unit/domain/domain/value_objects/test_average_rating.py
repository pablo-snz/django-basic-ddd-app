import pytest
from django_basic_ddd_app.api.domain.value_objects.average_rating import AverageRating

# Test VO AverageRating, business rules:
# AverageRating basic method: get -> returns the value
# the average should be between 0 and 5
# the average should be a float
# the average should be immutable
# the average should be comparable


def test_average_rating_should_be_between_0_and_5():
    with pytest.raises(ValueError):
        AverageRating(5.1)


def test_average_rating_should_be_a_float():
    with pytest.raises(TypeError):
        AverageRating("string")


def test_average_rating_should_be_immutable():
    average_rating = AverageRating(4.0)
    with pytest.raises(AttributeError):
        average_rating.value = 5.0


def test_average_rating_should_be_comparable():
    average_rating_1 = AverageRating(4.0)
    average_rating_2 = AverageRating(4.0)
    assert average_rating_1 == average_rating_2
    assert average_rating_1 <= average_rating_2
    assert average_rating_1 >= average_rating_2
    assert not average_rating_1 != average_rating_2
    assert average_rating_1 <= 4.0
    assert average_rating_2 >= 4.0
    assert average_rating_1 < 4.1
    assert average_rating_2 > 3.9


def test_average_rating_manage_nulls_and_returns():
    average_rating = AverageRating(None)
    assert average_rating.get() is None
