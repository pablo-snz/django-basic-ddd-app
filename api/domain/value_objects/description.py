from dataclasses import dataclass


@dataclass(frozen=True)
class Description:
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str):
            raise TypeError("Description should be a string")
        if not self.value:
            raise ValueError("Description should not be empty")

    def __eq__(self, other):
        return self.value == other.value

    def get(self):
        return self.value
