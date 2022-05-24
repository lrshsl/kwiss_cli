from quiz import Quiz


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
    'Ahmm.., I knew that too.\n\n\n\n\n\n I did.',
    'You\'re sooo intelligent! [eyes rolling]',

    'Wow..'
)


if __name__ == '__main__':
    quiz = Quiz(
        file=SRC,
        on_false=INSULTIONS,
        on_true=CONGRATULATIOINS,
        has_humor=not SPEEDRUN
    )
    quiz.run()
