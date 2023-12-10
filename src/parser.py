import os
import numpy as np
from typing import List, Optional, Tuple, assert_type

from src.utils.parsing_types import ParsingError, ParsingErrorType

def nonempty(lines: List[str]):
    for line in lines:
        if len(line.strip()) > 1:
            yield line;

class Parser:

    def __init__(self) -> None: pass;


    # Parse Answer
    def parse_answer(self, answer: str) -> List[str]:
        words = [w.strip()
                 for w in answer.split(",")];
        return words

    # Parse File
    def get_pairs(self, filename) -> List[Tuple[List[str], List[str]]]:
        print(f"--<[Log] Reading file {filename}>--");

        # Parse file
        err = self.parse_file(filename);
        if err is not None:
            err.print_stderr();

        print(f"--<[Log] File read >--")
        return self.pairs


    def parse_file(self, filename: str) -> Optional[ParsingError]:
        # Read file
        lines = self.read_file_lines(filename);
        if isinstance(lines, ParsingError):
            return lines;

        # Split lhs and rhs
        lines_split = [line.split(':') for line in nonempty(lines)];

        self.pairs = [([word.strip() for word in lhs.split(",")],
                       [word.strip() for word in rhs.split(",")])
                      for lhs, rhs in lines_split];



    @staticmethod
    def read_file_lines(filename) -> List[str] | ParsingError:

        # Check if file exists
        if not os.path.exists(filename):
            return ParsingError(ParsingErrorType,
                                "File {} does not exists".format(filename));

        # Read the content
        with open(filename, 'r') as f:
            lines: List[str] = f.read().splitlines()

        return lines
