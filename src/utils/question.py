from typing import List, Self, Tuple


class Question:
    lhs: List[str];
    rhs: List[str];

    def __init__(self, lhs: List[str], rhs: List[str]) -> None:
        self.lhs = lhs;
        self.rhs = rhs;

    @classmethod
    def from_tuple(cls, src: Tuple[List[str], List[str]]) -> Self:
        lhs, rhs = src;
        return Question(lhs, rhs)
