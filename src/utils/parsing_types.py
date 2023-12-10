import enum
import sys


class ParsingErrorType(enum.IntEnum):
    GeneralError = enum.auto();


class ParsingError:
    type_: ParsingErrorType;
    msg: str;

    def __init__(self, type_, msg) -> None:
        self.type_ = type_
        self.msg = msg

    def print_stderr(self) -> None:
        print(f"--<[Error] {self.type_}: {self.msg}", file=sys.stderr)


