from src.clear import clear
from src.colors import Color

# clears the screen
clear()


# Define Dialog options
class Text:
    enter = "Press Enter to continue: "
    correct = "Correct: "
    incorrect = "Incorrect: "
    again = "Do you want to go again? :"
    yes = "Yes"
    no = "No"
    thank_you = "Thank you for using Azla written in python"


def end_result(opt):
    # Prints your result
    print(f'{Color.GREEN}{Text.correct} {str(opt["correct"])}{Color.END}')
    print(f'{Color.RED}{Text.incorrect} {str(opt["incorrect"])}{Color.END}')
    input(Text.enter)


# Function that prompts you to run again
def do_again():
    # List of possible answers
    answer_list = [Text.yes, Text.no]
    number = 1

    # Creates empty number list
    number_list = []

    # Initially set choice to None
    choice = None
    while choice not in number_list:
        number = 1
        # for loops that append numbers to each option
        for key in answer_list:
            number_list.append(number)
            string = str(number) + " " + key
            print(string)
            number = int(number) + 1

        # Prompts you to make a choice
        choice = input(Text.again)

        if choice.isdigit():
            choice = int(choice)
        else:
            clear()
            print("Invalid Value")

    return choice
