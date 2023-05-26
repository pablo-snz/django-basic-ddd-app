import pytest

from test.unit.application.services import MockedRepository, MockedUnitOfWork
from django_basic_ddd_app.api.application.services.product_query import (
    ProductQueryService,
)
from django_basic_ddd_app.api.domain.entities.product import Product


@pytest.fixture
def mocked_repository():
    return MockedRepository()


@pytest.fixture
def mocked_uow():
    return MockedUnitOfWork()


def test_find_all_products(mocked_repository, mocked_uow):
    mocked_repository.products = [
        Product("name", "description", 0),
        Product("name", "description", 0),
        Product("name", "description", 0),
    ]

    product_query_service = ProductQueryService(mocked_repository, mocked_uow)
    products = product_query_service.find_all("user_id")

    assert len(products) == 3
    assert mocked_uow.committed is False
    assert mocked_uow.rolled_back is False


def test_find_all_products_with_error(mocked_repository, mocked_uow):
    mocked_repository.find_all = lambda user_id: 1 / 0

    product_query_service = ProductQueryService(mocked_repository, mocked_uow)

    with pytest.raises(ZeroDivisionError):
        product_query_service.find_all("user_id")

    assert mocked_uow.committed is False
    assert mocked_uow.rolled_back is False
