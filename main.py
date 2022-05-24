import random                           # random.choice

from iostream import IO, cout, endl     # IO is actually important


# -------------------------------------#-------------------------------------#
# Settings

SRC = 'en_irregular_verbs'  # File to read. See README.md     ##- SRC-Init -##
SWITCH_ORDER = False        # Switch word-definition to definition-word
SPEEDRUN = True             # Trigger for insultions & co


# -------------------------------------#-------------------------------------#
# Code

SRC = 'src/' + SRC + '.voci'
# Ik, plus on str isn't the best idea, but does that matter here?


INSULTIONS = (
    'Gotcha!',
    'R u sure..?',
    'Seriously??',
    'Rather give up!',
    'Will you ever lern it..?',
    'That was close\n..\n Or at least better than the last 6e+300 tries =P'
)

CONGRATULATIOINS = (
    'Um.. that was luck..',
    'Well, every blind squirrel sometimes finds a nut, right?',
    'Better than last time..',
    'Ahmm.., I knew that too.\n\n I did.',
    'You\'re sooo intelligent! [eyes rolling]',

    'Wow..'
)


class Quiz:
    def __init__(self, file) -> None:
        self.io = IO(reversed=SWITCH_ORDER)
        self.question_collection = list(
            self.io.get_questions_from_file(file)
        )
        if not len(self.question_collection):
            raise Exception('Empty file')

    def run(self):
        while 1:
            question = self.get_new_question()
            self.ask_until_answered(question)

    def get_new_question(self):
        return random.choice(self.question_collection)

    def ask_until_answered(self, question):
        questions = list(question.questions)
        correct_ans = list(question.answers)
        while 1:
            ans = self.ask(questions)
            cout << endl

            match ans.strip(' \t'):
                case ':q' | ':quit' | ':exit':
                    return False
                case ':help!' | ':help' | ':h':
                    cout << correct_ans << endl
                case ':n' | ':next' | ':skip' | ':skip 1':
                    cout << correct_ans << endl
                    break
                case _:
                    if self.is_accepted(ans, correct_ans):
                        self.congratulate()
                        break
                    else:
                        self.insult()
        return True

    def ask(self, questions):
        for q in questions:
            cout << '| ' << q << ' '
        cout << '|' << endl * 2 << '> '
        return input()

    def is_accepted(self, inpt, answers):
        """ Will get extended """  # TODO
        entered = list(self.io.parse(inpt))
        return self.is_same(entered, answers)

    def is_same(self, entered, answers):
        if len(entered) < len(answers):
            self.complain(
                'Not enough answers. Make sure you use \',\' to separate them'
            )
            return False
        elif len(entered) > len(answers):
            self.complain(
                'You entered too much words'
            )
        for i, (e, ans) in enumerate(zip(entered, answers)):
            if e.strip(' ,\t\n') != ans:
                self.complain(
                    f'The answer \'{e}\' on {i+1}. place is not \
accepted. For a hint enter :h'
                )  # TODO: replace place??
                return False
        return True

    @staticmethod
    def complain(msg):
        cout << 'X' << endl
        cout << 'Wrong answer: ' << msg << endl

    @staticmethod
    def congratulate():
        cout << '\u2713' << endl
        if not SPEEDRUN:
            cout << '"' << random.choice(CONGRATULATIOINS) << '"' << endl
        cout << endl * 2

    @staticmethod
    def insult():
        if not SPEEDRUN:
            cout << '"' << random.choice(INSULTIONS) << '"' << endl
        cout << endl * 2


if __name__ == '__main__':
    quiz = Quiz(SRC)
    quiz.run()
