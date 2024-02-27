# Function to shuffle the words
def shuffle(list):
    questions_word = []
    questions_correct = []
    for key, value in list.items():
        questions_word.append(value)
        questions_correct.append(key)
        pairs = zip(questions_word, questions_correct)
        pairs = set(pairs)
    return pairs
