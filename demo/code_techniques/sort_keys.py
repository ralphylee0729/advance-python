"""sort keys"""

from typing import TypedDict, cast
from random import randint


class RandomDict(TypedDict):
    num: int
    name: str


def gen_name(size: int = 4) -> str:
    """gen name"""
    return "".join([chr(randint(65, 90)) for _ in range(size)])


random_dicts: list[RandomDict] = [
    {"num": randint(1, 1000), "name": gen_name()} for _ in range(10)
]

# random_dicts.sort(key=lambda x: x["num"])

# # it would be better to use a TypedDict instead of casting individual
# # expressions in lambda functions
# random_dicts.sort(key=lambda x: cast(int, x["num"]))


sorted_random_dicts = sorted(random_dicts, key=lambda x: x["name"])

print(random_dicts)
print(sorted_random_dicts)