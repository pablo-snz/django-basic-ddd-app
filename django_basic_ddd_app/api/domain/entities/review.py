from django_basic_ddd_app.api.domain.value_objects.user_id import UserId
from django_basic_ddd_app.api.domain.value_objects.rating import Rating
from django_basic_ddd_app.api.domain.value_objects.description import Description


class Review:
    def __init__(self, user_id, rating, description):
        self._user_id = UserId(user_id)
        self._rating = Rating(rating)
        self._description = Description(description)

    def set_description(self, description):
        self._description = Description(description)

    def set_rating(self, rating):
        self._rating = Rating(rating)

    def get_user_id(self):
        return self._user_id.get()

    def get_rating(self):
        return self._rating.get()

    def get_description(self):
        return self._description.get()
