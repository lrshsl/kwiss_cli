import random
from typing import List

from src.utils.iostream import cout, endl
from src.parser import Parser
from src.utils.question import Question


class Quiz:
    def __init__(self,
                 file: str,
                 reversed_=False
                 ) -> None:
        self.parser = Parser();
        self.backend = Backend(self.parser);
        self.question_collection = list((
            Question.from_tuple(line)
            for line in self.parser.get_pairs(file))
        );
        if not len(self.question_collection):
            raise Exception('File is empty');

    def run(self):
        while 1:
            question = self.get_new_question();
            if not self.ask_until_answered(question):
                return;

    def get_new_question(self):
        return random.choice(self.question_collection);

    def ask_until_answered(self, question):
        questions = list(question.lhs);
        correct_ans = list(question.rhs);
        while 1:
            ans = self.ask(questions);

            match ans.strip(' \t'):
                case ':q' | ':quit' | ':exit':
                    cout << endl << "--<[ Quitting ]>--" << endl;
                    return False;
                case ':help!' | ':help' | ':h':
                    cout << correct_ans << endl * 3;
                case ':n' | ':next' | ':skip' | ':skip 1':
                    cout << correct_ans << endl * 3;
                    break;
                case _:
                    if self.backend.is_accepted(ans, correct_ans):
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


