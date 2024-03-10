# defines all the words available to the program
class Word():
    word_list = {
        'basic':  {
            "alma": "apple",
            "salam": "hello",
            "cox sagol": "thank you",
            "sakit": "calm",
        },
        'colors': {
            "sakit": "calm"
        },
        'family': {
            "sakit": "calm",
            "alma": "apple"
        },
        'body': {
            "aş": "head",
            "Qulaq": "ear",
            "Saç": "hair",
            "Ağız": "Mouth",
            "Burun": "Nose",
            "Göz": "Eye",
            "Ağ ciyər": "lungs",
            "Qara ciyər": "liver"
        },
    }

    def __init__(self):
        pass

    def wordlist(choice):
        word_list = Word.word_list

        return word_list[choice]

    def wordlistOptions():
        word_list = Word.word_list

        return word_list
