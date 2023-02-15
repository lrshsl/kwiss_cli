from quiz import Quiz


# -------------------------------------#-------------------------------------#
# Settings

SET_NAME     = 'lat_sextadecima'  # File to read. See README.md     ##- SRC-Init -##
SWITCH_ORDER = False              # Switch word-definition to definition-word
SPEEDRUN     = True               # Trigger for insultions & co


SOURCE_FOLDER = 'src' + '/'          # From where to read the voci files
FILE_EXTENSION = '.voci'             # Can be everything, the format of the content matters


# -------------------------------------#-------------------------------------#
# Code

SRC = ''.join((
    SOURCE_FOLDER,
    SET_NAME,
    FILE_EXTENSION))


INSULTIONS = (
    'Gotcha!',
    'R u sure..?',
    'Seriously??',
    'Rather give up!',
    'Will you ever learn it..?',
    'That was close\n..\n Or at least better than the last 6e+300 tries =P'
)

CONGRATULATIOINS = (
    'Um.. that was luck..',
    'Well, every blind squirrel sometimes finds a nut, right?',
    'Better than last time..',
    'Ahmm.., I knew that too.\n\n\n\n\n\n I did.',
    'You\'re sooo intelligent! [eyes rolling]',

    'Wow..',
    'Impressive',
    'Unbelievable',
    'Tribble Kill!\n\nOh, wrong game'
)


if __name__ == '__main__':
    quiz = Quiz(
        file=SRC,
        on_false=INSULTIONS,
        on_true=CONGRATULATIOINS,
        has_humor=not SPEEDRUN,
    )
    quiz.run()

