from typing import List

from django_basic_ddd_app.api.domain.entities.product import Product
from django_basic_ddd_app.api.domain.interfaces.repository import ProductRepository
from django_basic_ddd_app.api.application.interfaces.uow import UnitOfWork


class ProductQueryService:
    def __init__(self, product_repository: ProductRepository, uow: UnitOfWork):
        self.product_repository = product_repository
        self.uow = uow

    def find_all(self, user_id: str | None) -> List[Product]:
        with self.uow:
            try:
                products: List[Product] = self.product_repository.find_all(user_id)
            except Exception as e:
                raise e

        return products
