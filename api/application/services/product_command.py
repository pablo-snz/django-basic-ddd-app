from api.domain.entities.product import Product
from api.domain.interfaces.repository import ProductRepository
from api.application.interfaces.uow import UnitOfWork


class ProductCommandService:
    def __init__(self, product_repository: ProductRepository, uow: UnitOfWork):
        self.product_repository = product_repository
        self.uow = uow

    def create(self, name: str, description: str) -> None:
        with self.uow:
            try:
                product = Product(name, description, 0)
                self.product_repository.save(product)
                self.uow.commit()
            except Exception as e:
                self.uow.rollback()
                raise e
