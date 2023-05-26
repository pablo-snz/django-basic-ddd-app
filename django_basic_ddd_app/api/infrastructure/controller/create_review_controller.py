from uuid import UUID
from rest_framework.request import Request
from rest_framework.response import Response

from django_basic_ddd_app.api.domain.exceptions.entity_not_exist_exception import EntityNotExistException
from django_basic_ddd_app.api.application.services.review_command import ReviewCommandService
from django_basic_ddd_app.api.infrastructure.controller.base_controller import BaseController


class CreateReviewController(BaseController):
    def post(self, request: Request):
        review_command_service = ReviewCommandService(self.repository, self.uow)
        auth, user = self.get_user_id(request)

        if auth is False or user is None:
            return Response(status=401)

        product_id = UUID(request.data.get("product_id"))
        rating = request.data.get("grade")
        description = request.data.get("review")

        try:
            review_command_service.create(product_id, user, float(rating), description)
        except EntityNotExistException:
            return Response(status=404)

        return Response({"status": 200})
