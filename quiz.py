import random                           # random.choice

from iostream import Parser, cout, endl     # Parser is actually important


class Quiz:
    def __init__(
            self,
            file,
            on_false=None,
            on_true=None,
            has_humor=False,
            reversed=False
         ) -> None:
        self.on_false, self.on_true = on_false, on_true
        self.has_humor = has_humor

        self.parser = Parser(reversed=reversed)
        self.backend = Backend(self.parser)
        self.question_collection = list(
            self.parser.get_questions_from_file(file)
        )
        if not len(self.question_collection):
            raise Exception('File is empty')

    def is_accepted(self, inpt, answers):
        return self.backend.is_same(inpt, answers)

    def get_new_question(self):
        return random.choice(self.question_collection)


"""
    def run(self):
        while 1:
            question = self.get_new_question()
            self.ask_until_answered(question)

    def ask_until_answered(self, question):
        questions = list(question.questions)
        correct_ans = list(question.answers)
        while 1:
            ans = Output.ask(questions)

            match ans.strip(' \t'):
                case ':q' | ':quit' | ':exit':
                    return False
                case ':help!' | ':help' | ':h':
                    cout << correct_ans << endl * 3
                case ':n' | ':next' | ':skip' | ':skip 1':
                    cout << correct_ans << endl * 3
                    break
                case _:
                    if self.is_accepted(ans, correct_ans):
                        Output.congratulate(self.on_true, self.has_humor)
                        break
                    else:
                        Output.insult(self.on_false, self.has_humor)
        return True
"""


class Backend:
    def __init__(self, parser) -> None:
        self.parser = parser
        self.err_msg = ''

    def is_same(self, inpt, answers):  # mega TODO: Make this mess readable
        entered = list(Parser.parse(inpt, self.parser.w_sep))
        answers = list(answers)
        if len(entered) < len(answers):
            self.err_msg = '\
Not enough answers. \
Make sure you use \',\' to separate them'
            return False
        elif len(entered) > len(answers):
            self.err_msg = 'You entered too much words'
        for i, (e, ans) in enumerate(zip(entered, answers)):
            if e.strip(' ,\t\n') != ans:
                self.err_msg = f'\
The answer \'{e}\' on {i+1}. place is not \
accepted. For a hint enter :h'
                return False
        return True


"""
class Output:

    @staticmethod
    def complain(msg):
        pass

    @staticmethod  # TODO: merge
    def congratulate(src, enabled):
        cout << '\u2713' << endl * 2
        if enabled:
            cout << '"' << random.choice(src) << '"' << endl
        cout << endl * 2

    @staticmethod
    def insult(src, enabled):
        if enabled:
            cout << '"' << random.choice(src) << '"' << endl
        cout << endl * 2
"""
