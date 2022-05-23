import random

from iostream import IO, cout, endl     # IO is actually important


SRC = 'src/' + 'en_irregular_verbs' + '.voci'
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
        self.io = IO()
        self.question_collection = list(self.io.get_questions_from_file(file))
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
                case ':help!' | ':help':
                    cout << correct_ans << endl
                case ':n' | ':next' | ':skip' | ':skip 1':
                    cout << correct_ans << endl
                    break
                case _:
                    if self.is_accepted(ans, correct_ans):
                        self.congratulate()
                        break
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
        for e in entered:
            if e.strip(' ,\t\n') not in answers:
                self.complain(
                    f'The answer \'{e}\' is not accepted'
                )
                return False
        return True

    @staticmethod
    def complain(msg):
        cout << 'Wrong answer: ' << msg << endl

    def congratulate(self):
        cout << '\u2713' << endl << '"'
        cout << random.choice(CONGRATULATIOINS)
        cout << '"' << endl * 3


if __name__ == '__main__':
    quiz = Quiz(SRC)
    quiz.run()
