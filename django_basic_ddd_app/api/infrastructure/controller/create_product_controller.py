from rest_framework.request import Request
from rest_framework.response import Response

from django_basic_ddd_app.api.application.services.product_command import ProductCommandService
from django_basic_ddd_app.api.infrastructure.controller.base_controller import BaseController


class CreateProductController(BaseController):
    def post(self, request: Request):
        product_command_service = ProductCommandService(self.repository, self.uow)
        auth, user = self.get_user_id(request)

        if auth is False or user is None:
            return Response(status=401)

        name = request.data.get("name")
        description = request.data.get("description")

        product_command_service.create(name, description)

        return Response({"status: 200"})
