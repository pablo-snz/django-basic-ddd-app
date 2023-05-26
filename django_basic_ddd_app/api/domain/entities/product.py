from uuid import UUID, uuid4

from django_basic_ddd_app.api.domain.entities.review import Review
from django_basic_ddd_app.api.domain.value_objects.name import Name
from django_basic_ddd_app.api.domain.value_objects.average_rating import AverageRating
from django_basic_ddd_app.api.domain.value_objects.description import Description
from django_basic_ddd_app.api.domain.value_objects.review_count import ReviewCount


class Product:
    def __init__(
        self,
        name: str,
        description: str,
        num_reviews: int,
        average_rating: float | None = None,
        id: UUID | None = None,
    ):
        self._id: UUID = id if id is not None else uuid4()
        self._name: Name = Name(name)
        self._description: Description = Description(description)
        self._review_count: ReviewCount = ReviewCount(num_reviews)
        self._average_rating: AverageRating = AverageRating(average_rating)
        self._review: Review | None = None

    def add_review(
        self, user_id: str, rating: float, text: str, from_repository: bool = False
    ):
        old_rating = self._review.get_rating() if self._review else None
        self._review = Review(user_id, rating, text)

        if not from_repository:
            self._average_rating = AverageRating(
                self._calculate_rating(
                    self._average_rating.get(),
                    self._review_count.get(),
                    rating,
                    old_rating is not None,
                    old_rating,
                )
            )
            if not old_rating:
                self._review_count = ReviewCount(self._review_count.get() + 1)

    def _calculate_rating(
        self, average_rating, num_ratings, new_rating, rewrite, old_rating=None
    ):
        if num_ratings == 0:
            return new_rating
        total = average_rating * num_ratings
        updated_total = (
            total - old_rating + new_rating if rewrite else total + new_rating
        )
        return updated_total / (num_ratings + (0 if rewrite else 1))

    def get_review(self) -> Review:
        return self._review

    def get_average_rating(self) -> float | None:
        return self._average_rating.get()

    def get_name(self) -> str:
        return self._name.get()

    def get_id(self) -> UUID:
        return self._id

    def get_description(self) -> str:
        return self._description.get()

    def get_num_reviews(self) -> int:
        return self._review_count.get()
