import sys
from src.quiz import Quiz


def main():
    filename = sys.argv[1]
    Quiz(filename).run()


if __name__ == "__main__":
    main()
