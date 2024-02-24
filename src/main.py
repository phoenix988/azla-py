from list.list import Word
from src.clear import clear

# Main class


class Main:
    def __init__(self):
        pass

    def main_list():
        # wordlist available
        optionItems = Word.wordlistoptions()
        exit_file = "Exit"

        # defines the wordlist options
        options = []

        for key, value in optionItems.items():
            options.append(key)

        options.append(exit_file)

        return options

    def wordlist_choice(options, multiple=1):
        # reset the number
        number = 1

        # Creates empty number list
        number_list = []

        choice = None
        while choice not in number_list:

            # If you do multiple sessions it will print it out
            if multiple > 1:
                print(f'Session {multiple}')

            for key in options:
                number_list.append(number)
                string = str(number) + " " + key
                print(string)
                number = int(number) + 1
                last_number = number - 1

            # Prompts you to choose wordlist
            choice = input("Choose your wordlist: ")
            choice = int(choice)
            # Keeps running if you choice an invalid value
            if choice not in number_list:
                clear()
                print("Invalid Value")
            # exit if you choose exit option
            elif choice == last_number:
                exit()
            number = 1

        choice_fix = int(choice) - 1

        # formats the choice so you can match with the correct wordlist
        for key in options:
            index = options.index(key)
            if index == choice_fix:
                final_choice = key
                break
        # Returns the value so it can be used
        return final_choice

    def get_final_result():
        pass
