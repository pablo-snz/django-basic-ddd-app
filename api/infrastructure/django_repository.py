from api.domain.interfaces.repository import ProductRepository
from api.infrastructure.models import ProductModel, ReviewModel
from api.domain.entities.product import Product
from uuid import UUID


class DjangoProductRepository(ProductRepository):
    def model_to_entity(self, model, user_id):
        product = Product(
            model.name,
            model.description,
            model.num_reviews,
            model.average_rating,
            id=model.id,
        )
        review = ReviewModel.objects.filter(product=model, user_id=user_id).first()
        if review is not None:
            product.add_review(
                review.user_id, review.rating, review.description, from_repository=True
            )
        return product

    def entity_to_model(self, entity, model=None):
        if model is None:
            try:
                model = ProductModel.objects.get(id=entity.get_id())
            except ProductModel.DoesNotExist:
                model = ProductModel()
        model.name = entity.get_name()
        model.description = entity.get_description()
        model.num_reviews = entity.get_num_reviews()
        model.average_rating = entity.get_average_rating()
        return model

    def find_all(self, user_id: str = None):
        return [self.model_to_entity(p, user_id) for p in ProductModel.objects.all()]

    def find_by_id(self, product_id: UUID, user_id: str):
        try:
            product_model = ProductModel.objects.get(id=product_id)
            return self.model_to_entity(product_model, user_id)
        except ProductModel.DoesNotExist:
            return None

    def save(self, product: Product):
        product_model = self.entity_to_model(product)
        product_model.save()
        if product.get_review() is not None:
            review = product.get_review()
            review_model, _ = ReviewModel.objects.update_or_create(
                product=product_model,
                user_id=review.get_user_id(),
                defaults={
                    "rating": review.get_rating(),
                    "description": review.get_description(),
                },
            )
