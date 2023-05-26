from django_basic_ddd_app.api.domain.entities.product import Product
from django_basic_ddd_app.api.domain.interfaces.repository import ProductRepository
from django_basic_ddd_app.api.application.interfaces.uow import UnitOfWork
from uuid import UUID


class MockedRepository(ProductRepository):
    def __init__(self):
        self.products = []

    def find_all(self, user_id: str | None) -> list[Product]:
        return self.products

    def find_by_id(self, product_id: UUID, user_id: str | None) -> Product:
        for product in self.products:
            if product.get_id() == product_id:
                return product

    def save(self, product: Product) -> None:
        for i, product_ in enumerate(self.products):
            if product_.get_id() == product.get_id():
                self.products[i] = product
                return None

        self.products.append(product)


class MockedUnitOfWork(UnitOfWork):
    def __init__(self):
        self.committed = False
        self.rolled_back = False

    def __enter__(self):
        pass

    def __exit__(self, *args):
        pass

    def commit(self):
        self.committed = True

    def rollback(self):
        self.rolled_back = True
