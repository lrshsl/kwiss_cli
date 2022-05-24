import codecs                           # unicode encoding (Umlauts)

from question import Question


class ostream:
    def __init__(self) -> None:
        pass

    def __lshift__(self, other):
        val = str(other)
        print(val, end='')
        return self


cout = ostream()
endl = '\n'


class IO:
    def __init__(self, reversed=False) -> None:
        tokens = {
            'word-definition separator': u':',
            'word separator': u','
        }
        self.wd_sep, self.w_sep = tokens.values()
        self.reversed = reversed

    def get_questions_from_file(self, file):
        lines = codecs.open(file, 'r', encoding='utf-8').readlines()
        parsed_lines = self.parse_lines(lines)
        for parsed_line in parsed_lines:
            yield parsed_line

    def parse_lines(self, lines):
        for line_nb, line in enumerate(lines):
            parsed_line = self.parse_line(line, line_nb)
            if parsed_line is not None:
                yield Question(parsed_line)

    def parse_line(self, line, line_nb):
        if not self.is_parsable_line(line, line_nb):
            return
        left, right = line.split(self.wd_sep)
        if self.reversed:
            left, right = right, left
        return (self.parse(left), self.parse(right))

    def is_parsable_line(self, line, line_nb):
        def is_any_alpha(s): return any(c for c in s if c.isalpha())
        if not is_any_alpha(line):
            return 0
        if line.count(self.wd_sep) != 1:
            raise Exception(
                f"""
\tUnable to parse line {line_nb}:
\tWrong count of separators in \'{line}\'
Found {line.count(self.wd_sep)}, expected 1"""
            )
        return 1

    def parse(self, side):  # TODO: readable
        """ Used to parse left hand side or right hand side of a voci item """
        def stripped(arr): return (x.strip(' \t\n\r') for x in arr)
        return stripped(side.split(self.w_sep))
