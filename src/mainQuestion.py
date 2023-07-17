from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from words.init import Word
from src.colors import Colors, Size

# function to shuffle a dict
def shuffle(list):
    questions_word = []
    questions_correct = []
    for key, value in list.items():
        questions_word.append(value)
        questions_correct.append(key)
        pairs = zip(questions_word, questions_correct)
        pairs = set(pairs)
    return pairs


class Question():
    options = Word.word_list
    correct = 0
    incorrect = 0
    def run(name):
       choice = Word.wordlist(name)
       return choice
    def widget(choice):
        labels_widgets = {}
        correct = {}
        word = {}
        
        # Shuffle the list
        choice = shuffle(choice)

        for questions in choice:
            formatted_text = f"[color={Colors.label}]{questions[0]}[/color]"
            formatted_text = f"What is {formatted_text} in Azerbajani"
            correct[questions[0]] = questions[1]
            word[questions[0]] = questions[0]
            labels_widgets[questions[1]] = Label(size_hint=(0.3, 0.01), pos_hint={'center_x': 0.5, 'center_y': 2})
            labels_widgets[questions[1]].markup = True
            labels_widgets[questions[1]].text = formatted_text.strip()
        return labels_widgets, correct, word
    def word_options():
        option_widgets = {}
        for key, value in Question.options.items():
            option_widgets[key] = Button(text=key, size_hint_y=None, height=30)
        return option_widgets
