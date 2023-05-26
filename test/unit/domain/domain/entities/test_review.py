import pytest
from api.domain.entities.review import Review

# Review es parte de nuestro agregado que tiene la raiz en Product.
# Review es una entidad en tanto que tiene identidad propia y es mutable.
# sin embargo, las reglas de negocio de Review son las de sus Value Objects,
# excepto por el hecho de que Review es mutable.


@pytest.fixture
def review():
    return Review("1", 5.0, "Excelente")


def test_review_mutate_description(review):
    review.description = "Muy bueno"
    assert review.description == "Muy bueno"


def test_review_mutate_rating(review):
    review.rating = 4.0
    assert review.rating == 4.0


def test_get_user_id(review):
    assert review.get_user_id() == "1"


def test_get_rating(review):
    assert review.get_rating() == 5.0


def test_get_description(review):
    assert review.get_description() == "Excelente"
