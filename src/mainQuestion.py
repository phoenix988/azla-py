from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from words.init import Word

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
        for key, value in choice.items():
            text = f'What is {value} in Azerbajani ?'
            correct[value] = key
            word[value] = value
            labels_widgets[key] = Label(text=text,size_hint=(0.3, 0.01), pos_hint={'center_x': 0.5, 'center_y': 2})
        return labels_widgets, correct, word
    def word_options():
        option_widgets = {}
        for key, value in Question.options.items():
            option_widgets[key] = Button(text=key, size_hint_y=None, height=30)
        return option_widgets
