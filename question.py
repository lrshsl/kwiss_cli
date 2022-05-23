from typing import Sequence, Iterable


class Question:
    def __init__(self, src: Sequence[Iterable[str]]) -> None:
        self.questions, self.answers = src
