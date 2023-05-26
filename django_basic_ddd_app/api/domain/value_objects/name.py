from dataclasses import dataclass


@dataclass(frozen=True)
class Name:
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str):
            raise TypeError("Name should be a string")
        if not self.value:
            raise ValueError("Name should not be empty")

    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return self.value

    def get(self):
        return self.value
