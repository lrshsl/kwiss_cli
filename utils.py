from typing import Sequence, Iterable


class Question:
    def __init__(self, src: Sequence[Iterable[str]]) -> None:
        self.questions, self.answers = src

    def __iter__(self):
        yield self.questions
        yield self.answers


class Str:
    @staticmethod
    def arr_to_str(s):
        return ', '.join(s)


class Color:
    RED = (1, 0, 0)
    GREEN = (0, 1, 0)
    WHITE = (1, 1, 1)
