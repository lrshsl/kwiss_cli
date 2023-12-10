

class OStream:
    def __init__(self) -> None:
        pass

    def __lshift__(self, other):
        val = str(other)
        print(val, end='')
        return self


cout = OStream()
endl = '\n'
