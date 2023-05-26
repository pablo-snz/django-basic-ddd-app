import pytest
from uuid import UUID
from django_basic_ddd_app.api.domain.entities.product import Product

# Product es la raiz de nuestro agregado. Tiene bastante lógica de negocio que queremos testear correctamente.
# Bussines logic para testear:
# - Agregar un review
# - Calcular el rating promedio
# - Obtener el review de un usuario


@pytest.fixture
def product():
    return Product("product", "description", 0)


def test_add_review(product):
    assert product.get_review() is None
    product.add_review("1", 4.0, "text")
    assert product.get_review().get_user_id() == "1"
    assert product.get_review().get_rating() == 4.0
    assert product.get_review().get_description() == "text"


def test_calculate_rating():
    product = Product("product", "description", 1, 4.0)
    product.add_review("2", 5.0, "text")
    assert product._average_rating.get() == 4.5


def test_calculate_single_rating():
    product = Product("product", "description", 0)
    product.add_review("2", 5.0, "text")
    assert product._average_rating.get() == 5.0


def test_get_name(product):
    assert product.get_name() == "product"


def test_get_id(product):
    assert isinstance(product.get_id(), UUID)


def test_get_user_review_not_exists(product):
    assert product.get_review() is None


def test_get_average_rating_no_reviews(product):
    assert product.get_average_rating() is None


def test_get_num_reviews():
    product = Product("product", "description", 1, 4.0)
    product.add_review("2", 5.0, "text")
    assert product.get_num_reviews() == 2


def test_update_review(product):
    product.add_review("1", 4.0, "text")
    assert product.get_review().get_user_id() == "1"
    assert product.get_review().get_rating() == 4.0

    assert product.get_average_rating() == 4.0

    product.add_review("1", 5.0, "updated text")
    assert product.get_review().get_user_id() == "1"
    assert product.get_review().get_rating() == 5.0
    assert product.get_review().get_description() == "updated text"

    assert product.get_average_rating() == 5.0
    assert product.get_num_reviews() == 1
