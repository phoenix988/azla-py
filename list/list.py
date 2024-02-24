# defines all the words available to the program
class Word():
    word_list = {
        'basic':  {
            "alma": "apple",
            "salam": "hello", },
        'basic_2': {
            "sakit": "calm"
        },
        'basic_3': {
            "sakit": "calm",
            "alma": "apple"
        }, }

    def __init__(self):
        pass

    def wordlist(choice):
        word_list = Word.word_list

        return word_list[choice]

    def wordlistoptions():
        word_list = Word.word_list

        return word_list
