import random
from iostream import cout, endl, IO

# TODO: variation in complains


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
        while not self.exit_requested:
            correct_ans = list(question.answers)
            ans = self.ask(question)
            self.is_accepted(ans, correct_ans):
            self.react_on_command(ans)
        cout << 'True!'  # TODO: Variation

    def ask(self, question):
        for q in question.questions:
            cout << q << ' '
        cout << endl
        return input()

    def is_accepted(self, inpt, answers):
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

    def react_on_command(self, src):
        match src.strip(' \t'):
        case ':q' | ':quit' | ':exit':
            self.exit_requested = True
        case ':n' | ':next' | ':skip' | ':skip 1':
            return 


if __name__ == '__main__':
    src = 'rc/lat_undecima.voci'
    quiz = Quiz(src)
    quiz.run()
