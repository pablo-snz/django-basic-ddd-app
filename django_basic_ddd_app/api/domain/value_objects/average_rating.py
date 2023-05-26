from dataclasses import dataclass


@dataclass(frozen=True)
class AverageRating:
    value: float | None

    def __post_init__(self):
        if self.value is None:
            return
        if not isinstance(self.value, float):
            raise TypeError("AverageRating value must be a float")
        if self.value is not None:
            if self.value < 0 or self.value > 5:
                raise ValueError("AverageRating value must be between 0 and 5")

    def __eq__(self, other):
        if isinstance(other, AverageRating):
            return self.value == other.value
        return self.value == other

    def __le__(self, other):
        if isinstance(other, AverageRating):
            return self.value <= other.value
        return self.value <= other

    def __ge__(self, other):
        if isinstance(other, AverageRating):
            return self.value >= other.value
        return self.value >= other

    def __lt__(self, other):
        if isinstance(other, AverageRating):
            return self.value < other.value
        return self.value < other

    def __gt__(self, other):
        if isinstance(other, AverageRating):
            return self.value > other.value
        return self.value > other

    def get(self):
        return self.value
