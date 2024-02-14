import sys
from typing import List
from src.quiz import Quiz


def main():
    # Arguments
    args: List[str] = sys.argv;

    # Input file
    assert len(args) >= 2, "pls provide a filename";
    filename: str = args[1];

    # Reverse
    reverse: bool = False;
    if len(args) == 3:
        if args[2] in ("-rev", "--reverse-word-definition"):
            print("Word-definition inverted");
            reverse = True;
        else:
            print(f"Argument at place 2 ({args[2]}) unknown");
            sys.exit(1);

    # Randomize order
    randomize_order: bool = False;
    if len(args) == 4:
        if args[3] in ("-rand", "--randomize-order"):
            print("Order of words randomized");
            randomize_order = True;
        else:
            print(f"Argument at place 3 ({args[3]}) unknown");
            sys.exit(1);

    Quiz(filename).run(reverse, randomize_order);


if __name__ == "__main__":
    main();
