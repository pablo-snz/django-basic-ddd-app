from uuid import UUID
from api.domain.interfaces.repository import ProductRepository
from api.domain.exceptions.entity_not_exist_exception import (
    EntityNotExistException,
)
from api.application.interfaces.uow import UnitOfWork


class ReviewCommandService:
    def __init__(self, product_repository: ProductRepository, uow: UnitOfWork):
        self.product_repository = product_repository
        self.uow = uow

    def create(
        self, product_id: UUID, user_id: str | None, rating: float, description: str
    ):
        with self.uow:
            try:
                product = self.product_repository.find_by_id(product_id, user_id)
                if product is None:
                    raise EntityNotExistException("Product does not exist")
                product.add_review(user_id, rating, description)
                self.product_repository.save(product)
                self.uow.commit()
            except Exception as e:
                self.uow.rollback()
                raise e
