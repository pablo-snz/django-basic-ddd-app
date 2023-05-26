from dataclasses import dataclass
import numbers


@dataclass(frozen=True)
class Rating:
    value: float

    def __post_init__(self):
        if not isinstance(self.value, numbers.Number):
            raise TypeError("Rating value must be a float")

        object.__setattr__(self, "value", float(self.value))

        if self.value < 0 or self.value > 5:
            raise ValueError("Rating value must be between 0 and 5")

    def __eq__(self, other):
        if isinstance(other, Rating):
            return self.value == other.value
        return self.value == other

    def __lt__(self, other):
        if isinstance(other, Rating):
            return self.value < other.value
        return self.value < other

    def __gt__(self, other):
        if isinstance(other, Rating):
            return self.value > other.value
        return self.value > other

    def __le__(self, other):
        if isinstance(other, Rating):
            return self.value <= other.value
        return self.value <= other

    def __ge__(self, other):
        if isinstance(other, Rating):
            return self.value >= other.value
        return self.value >= other

    def get(self):
        return self.value
