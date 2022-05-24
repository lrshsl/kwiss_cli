import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.clock import Clock

from quiz import Quiz
from utils import Str, Color


class LearnScreen(GridLayout):
    hint = StringProperty()
    question = StringProperty()

    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)


class QuizApp(App):

    def __init__(self, engine: Quiz):
        super().__init__()
        self.backend = Backend(self, engine)

    def build(self):
        screen = LearnScreen()
        screen.question = self.get_new_formatted_question()
        return screen

    def get_new_formatted_question(self):
        self.backend.generate_new_question()
        return self.backend.get_formatted_question()

    def process(self):
        if self.root is None:
            return
        ans = self.root.ids.input.text
        self.root.ids.input.text = ''
        Clock.schedule_once(self.set_focus, 0.2)
        self.backend.react_on_ans(ans)

    def set_focus(self, event):
        if self.root is None:
            return
        self.root.ids.input.focus = True


class Backend:
    def __init__(self, supr, engine: Quiz) -> None:
        self.supr = supr
        self.engine = engine

    def get_formatted_question(self):
        return Str.arr_to_str(self.question)

    def generate_new_question(self):
        q, ans = self.engine.get_new_question()
        self.question, self.correct_answer = list(q), list(ans)  # Set?? TODO

    def react_on_ans(self, ans):
        ans = ans.strip(' \t\n\r')
        if not self.react_on_cmd(ans):
            self.check_answer(ans)

    def react_on_cmd(self, ans):
        if self.supr.root is None:
            return True
        if ans in (':help!', ':help', ':h'):
            self.supr.root.ids.indicator_label.text = 'Solution:'
            self.supr.root.ids.indicator_label.color = Color.WHITE
            self.supr.root.hint = Str.arr_to_str(self.correct_answer)
            return True
        elif ans in (':n', ':next', ':skip', ':skip 1'):
            self.supr.root.hint = Str.arr_to_str(self.correct_answer)
            self.generate_new_question()
            return True

    def check_answer(self, ans):
        if self.engine.is_accepted(ans, self.correct_answer):
            self.on_true()
        else:
            self.on_false()

    def on_false(self):
        if self.supr.root is None:
            return
        self.supr.root.ids.indicator_label.color = Color.RED
        self.supr.root.ids.indicator_label.text = 'Wrong!!!!'
        self.supr.root.hint = self.engine.backend.err_msg

    def on_true(self):
        if self.supr.root is None:
            return
        self.supr.root.ids.indicator_label.color = Color.GREEN
        self.supr.root.ids.indicator_label.text = 'True!'
        self.generate_new_question()
        self.supr.root.ids.question_label.text = self.get_formatted_question()
        self.supr.root.hint = ''
