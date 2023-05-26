import pytest

from test.unit.application.services import MockedRepository, MockedUnitOfWork
from api.application.services.review_command import (
    ReviewCommandService,
)
from api.domain.entities.product import Product


@pytest.fixture
def mocked_repository():
    return MockedRepository()


@pytest.fixture
def mocked_uow():
    return MockedUnitOfWork()


def test_create_review(mocked_repository, mocked_uow):
    test_product = Product("name", "description", 3, 4.0)
    mocked_repository.products = [test_product]

    review_command_service = ReviewCommandService(mocked_repository, mocked_uow)
    review_command_service.create(test_product.get_id(), "1", 5.0, "text")

    assert test_product.get_average_rating() == 4.25
    assert len(mocked_repository.products) == 1
    assert mocked_repository.products[0].get_review().get_user_id() == "1"
    assert mocked_repository.products[0].get_review().get_rating() == 5.0
    assert mocked_repository.products[0].get_review().get_description() == "text"
    assert mocked_uow.committed is True
    assert mocked_uow.rolled_back is False


def test_create_review_with_invalid_product_id(mocked_repository, mocked_uow):
    test_product = Product("name", "description", 0)
    mocked_repository.products = [test_product]

    review_command_service = ReviewCommandService(mocked_repository, mocked_uow)
    with pytest.raises(Exception):
        review_command_service.create("invalid_product_id", "1", 5.0, "text")

    assert len(mocked_repository.products) == 1
    assert mocked_repository.products[0].get_review() is None
    assert mocked_uow.committed is False
    assert mocked_uow.rolled_back is True
