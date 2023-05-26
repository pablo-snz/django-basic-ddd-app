from django.urls import path
from api.infrastructure.controller.create_review_controller import (
    CreateReviewController,
)
from api.infrastructure.controller.create_product_controller import (
    CreateProductController,
)
from api.infrastructure.controller.list_products_controller import (
    ListProductsController,
)


urlpatterns = [
    path("products/list", ListProductsController.as_view()),
    path("products/create", CreateProductController.as_view()),
    path("reviews/create", CreateReviewController.as_view()),
]
