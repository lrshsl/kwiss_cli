import random
from typing import List

from src.utils.iostream import cout, endl
from src.parser import Parser
from src.utils.question import Question


class Quiz:
    def __init__(self,
                 file: str,
                 ) -> None:
        self.parser = Parser();
        self.backend = Backend(self.parser);
        self.question_collection = list((
            Question.from_tuple(line)
            for line in self.parser.get_pairs(file))
        );
        self.question_index: int = 0;
        if not len(self.question_collection):
            raise Exception('File is empty');


    def run(self, reverse: bool = False, randomize_order: bool = False):
        while 1:
            question = self.get_new_question(randomize_order);
            if not question or not self.ask_until_answered(question, reverse):
                return;


    def get_new_question(self, randomize_order: bool):
        if randomize_order:
            return random.choice(self.question_collection);

        if self.question_index > len(self.question_collection):
            return False;

        # Next question (in order)
        question: Question = self.question_collection[self.question_index];
        self.question_index += 1;
        return question;


    def ask_until_answered(self, question: Question, reverse: bool):
        words = list(question.lhs if not reverse else question.rhs);
        definition = list(question.rhs if not reverse else question.lhs);
        while 1:
            ans = self.ask(words);

            match ans.strip(' \t'):
                case ':q' | ':quit' | ':exit':
                    cout << endl << "--<[ Quitting ]>--" << endl;
                    return False;
                case ':help!' | ':help' | ':h':
                    cout << definition << endl * 3;
                case ':n' | ':next' | ':skip' | ':skip 1':
                    cout << definition << endl * 3;
                    break;
                case ':c' | ':clear':
                    cout << endl * 20;
                case _:
                    if self.backend.is_accepted(ans, definition):
                        Output.congratulate(None, False);
                        break;
                    else:
                        Output.insult(None, False);
        return True


    def ask(self, questions):
        for q in questions:
            cout << '| ' << q << ' ';
        cout << '|' << endl * 2 << '> ';
        return input();


class Backend:

    def __init__(self, parser: Parser) -> None:
        self.parser = parser;


    def is_accepted(self, inpt, answers: List[str]):
        """ Will get extended """  # TODO
        entered = self.parser.parse_answer(inpt);
        return self.is_same(entered, answers);


    def is_same(self, entered: List[str], answers: List[str]):

        if set(entered) == set(answers): return True;

        if len(entered) < len(answers):
            Output.complain(
                'Not enough answers. Make sure you use \',\' to separate them');
            return False;

        if len(entered) > len(answers):
            Output.complain('You entered too many words');
            return False;

        # Here, the sets are different although the length is the same
        for i, e in enumerate(entered):
            if e.strip(' ,\t\n') not in answers:
                Output.complain(
                    f'The answer \'{e}\' on {i+1}. place is not accepted. For a hint enter :h'
                )  # TODO: replace place??
                return False;

        raise Exception("this code should not be reached");



class Output:

    @staticmethod
    def complain(msg):
        cout << 'X' << endl * 2;
        cout << 'Wrong answer: ' << msg << endl;

    @staticmethod  # TODO: merge
    def congratulate(src, enabled):
        cout << '\u2713' << endl * 2;   # Unicode: Tick (✓)
        if enabled:
            cout << '"' << random.choice(src) << '"' << endl;
        cout << endl * 2;

    @staticmethod
    def insult(src, enabled):
        if enabled:
            cout << '"' << random.choice(src) << '"' << endl;
        cout << endl * 2;


