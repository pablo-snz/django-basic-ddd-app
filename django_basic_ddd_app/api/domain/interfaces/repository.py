from uuid import UUID
from abc import ABC, abstractmethod
from typing import List

from django_basic_ddd_app.api.domain.entities.product import Product


class ProductRepository(ABC):
    @abstractmethod
    def find_all(self, user_id: str | None) -> List[Product]:
        pass

    @abstractmethod
    def find_by_id(self, product_id: UUID, user_id: str | None) -> Product:
        pass

    @abstractmethod
    def save(self, product: Product) -> None:
        pass
