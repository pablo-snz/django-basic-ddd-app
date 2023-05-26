import pytest

from test.unit.application.services import MockedRepository, MockedUnitOfWork
from django_basic_ddd_app.api.application.services.product_command import (
    ProductCommandService,
)


@pytest.fixture
def mocked_repository():
    return MockedRepository()


@pytest.fixture
def mocked_uow():
    return MockedUnitOfWork()


def test_create_product(mocked_repository, mocked_uow):
    product_command_service = ProductCommandService(mocked_repository, mocked_uow)
    product_command_service.create("name", "description")

    assert len(mocked_repository.products) == 1
    assert mocked_repository.products[0].get_name() == "name"
    assert mocked_repository.products[0].get_description() == "description"
    assert mocked_uow.committed is True
    assert mocked_uow.rolled_back is False


def test_create_product_with_error(mocked_repository, mocked_uow):
    product_command_service = ProductCommandService(mocked_repository, mocked_uow)
    mocked_repository.save = lambda product: 1 / 0

    with pytest.raises(ZeroDivisionError):
        product_command_service.create("name", "description")

    assert len(mocked_repository.products) == 0
    assert mocked_uow.committed is False
    assert mocked_uow.rolled_back is True
