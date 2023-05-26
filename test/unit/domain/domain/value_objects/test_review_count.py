import pytest
from django_basic_ddd_app.api.domain.value_objects.review_count import ReviewCount

# Test VO ReviewCount, business rules:
# basic method: get -> returns the value
# should be integer
# should be >= 0
# should be immutable
# should be comparable


def test_review_count_should_be_integer():
    with pytest.raises(TypeError):
        ReviewCount(1.1)


def test_review_count_should_be_greater_or_equal_than_0():
    with pytest.raises(ValueError):
        ReviewCount(-1)


def test_review_count_should_be_immutable():
    review_count = ReviewCount(1)
    with pytest.raises(AttributeError):
        review_count.value = 2


def test_review_count_should_be_comparable():
    review_count_1 = ReviewCount(1)
    review_count_2 = ReviewCount(1)
    assert review_count_1 == review_count_2
    assert review_count_1 <= review_count_2
    assert review_count_1 >= review_count_2
    assert not review_count_1 != review_count_2
    assert review_count_1 <= 1
    assert review_count_2 >= 1
    assert review_count_1 < 2
    assert review_count_2 > 0


def test_review_count_get_should_return_value():
    review_count = ReviewCount(1)
    assert review_count.get() == 1
