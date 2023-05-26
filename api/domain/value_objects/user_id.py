from dataclasses import dataclass


@dataclass(frozen=True)
class UserId:
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str):
            raise TypeError("UserId must be a integer")
        if len(self.value) == 0:
            raise ValueError("UserId must be not empty")

    def __eq__(self, other):
        return self.value == other.value

    def get(self):
        return self.value
