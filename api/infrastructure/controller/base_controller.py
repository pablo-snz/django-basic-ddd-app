from rest_framework.request import Request
from rest_framework.views import APIView
from typing import Tuple, Optional

from api.infrastructure.django_repository import DjangoProductRepository
from api.infrastructure.django_uow import DjangoUoW
import jwt


class BaseController(APIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # inject dependencies
        self.repository = DjangoProductRepository()
        self.uow = DjangoUoW()

    def get_user_id(self, request: Request) -> Tuple[bool, Optional[str]]:
        auth = False
        user = None
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if auth_header is not None:
            _, token = auth_header.split()
            try:
                # hardcoded secret key - Esto esta fatal. pero por falta de tiempo se queda asi.
                user = jwt.decode(token, "secret", algorithms=["HS256"]).get(
                    "user_id", None
                )
                user = str(user)
                auth = True
            except Exception:
                pass
        return auth, user
