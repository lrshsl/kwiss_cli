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
