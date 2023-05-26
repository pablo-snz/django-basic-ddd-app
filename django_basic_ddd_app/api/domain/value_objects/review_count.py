from dataclasses import dataclass


@dataclass(frozen=True)
class ReviewCount:
    value: int

    def __post_init__(self):
        if not isinstance(self.value, int):
            raise TypeError("ReviewCount should be integer")
        if self.value < 0:
            raise ValueError("ReviewCount should be greater or equal than 0")

    def __eq__(self, other):
        if isinstance(other, ReviewCount):
            return self.value == other.value
        return self.value == other

    def __le__(self, other):
        if isinstance(other, ReviewCount):
            return self.value <= other.value
        return self.value <= other

    def __ge__(self, other):
        if isinstance(other, ReviewCount):
            return self.value >= other.value
        return self.value >= other

    def __ne__(self, other):
        if isinstance(other, ReviewCount):
            return self.value != other.value
        return self.value != other

    def __lt__(self, other):
        if isinstance(other, ReviewCount):
            return self.value < other.value
        return self.value < other

    def __gt__(self, other):
        if isinstance(other, ReviewCount):
            return self.value > other.value
        return self.value > other

    def get(self):
        return self.value
