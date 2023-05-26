from django_basic_ddd_app.api.application.interfaces.uow import UnitOfWork
from django.db import transaction


class DjangoUoW(UnitOfWork):
    def __init__(self):
        self._transaction = None

    def __enter__(self):
        self._transaction = transaction.atomic()
        self._transaction.__enter__()

    def __exit__(self, *args):
        self._transaction.__exit__(*args)

    def commit(self):
        self._transaction.__exit__(None, None, None)

    def rollback(self):
        self._transaction.__exit__(Exception, None, None)
