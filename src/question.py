from src.clear import clear
from list.list import Word
from src.colors import Color
from src.print import Text


def get_result():
    # creates emtpy result table
    result = {
        'correct': 0,
        'incorrect': 0,
    }

    return result


# the main question function that prompts you for answers
def question(choice):

    incorrect = 0
    correct = 0
    result = get_result()

    clear()

    questions = Word.wordlist(choice)

    for key in questions.keys():

        answer = input(
            f'{Color.CYAN}what is {questions[key]} in Azerbajani ?: {Color.END}')

        if answer == key:

            print("\n")
            input(f'{Color.GREEN}{Text.correct}!!! : {Color.END}')
            result['correct'] = correct + 1
            correct = correct + 1
            clear()

        else:

            print("\n")
            input(f'{Color.RED}{Text.incorrect} :( : {Color.END}')
            result['incorrect'] = incorrect + 1
            incorrect = incorrect + 1
            clear()

    return result
