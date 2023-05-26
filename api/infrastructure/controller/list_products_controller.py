from typing import List
from rest_framework.request import Request
from rest_framework.response import Response

from api.domain.entities.product import Product
from api.application.services.product_query import ProductQueryService
from api.infrastructure.controller.base_controller import BaseController


class ListProductsController(BaseController):
    def get(self, request: Request):
        product_query_service = ProductQueryService(self.repository, self.uow)
        auth, user = self.get_user_id(request)

        products: List[Product] = product_query_service.find_all(user)

        if len(products) == 0:
            return Response(status=404)

        return Response(
            [
                {
                    "product_id": product.get_id(),
                    "product_name": product.get_name(),
                    "product_description": product.get_description(),
                    "average_grade": product.get_average_rating(),
                    "num_reviews": product.get_num_reviews(),
                    "user_review": {
                        "user_id": product.get_review().get_user_id(),
                        "rating": product.get_review().get_rating(),
                        "description": product.get_review().get_description(),
                    }
                    if product.get_review() is not None
                    else None,
                }
                for product in products
            ]
        )
