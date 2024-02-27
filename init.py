from src.clear import clear
from src.question import question
from src.main import Main
from src.print import end_result, do_again
from src.gtk import Azla
import argparse

# Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument('--term', action='store_true',
                    help='Run The terminal Version')
parser.add_argument('-t', action='store_true',
                    help='Run The terminal Version')
args = parser.parse_args()

# clears the screen
clear()

if args.term or args.t:

    # keeps running when this is set to 1
    run = 1

    # Keep track of sessions
    multiple = 0

    while run == 1:

        multiple = multiple + 1

        # Asks which list to use
        options = Main.main_list()

        # Ask the question and stores it in $result variable
        result = question(Main.wordlist_choice(options, multiple))

        # Prints your result
        end_result(result)

        # Clear the screen
        clear()

        # ask you if you want to go again
        run = do_again()

        # Clear the screen
        clear()

        # breaks out of the program when you choose no
        if run == 2:
            break

else:
    # Run the GTK application
    Azla.run()
