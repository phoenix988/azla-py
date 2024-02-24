from src.clear import clear
from src.question import question
from src.main import Main
from src.print import end_result, do_again
from src.gtk import Azla


# clears the screen
clear()

Azla.run()
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
