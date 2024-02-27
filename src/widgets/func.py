from src.widgets.window.main import Window
from src.widgets.box.main import Box
from src.shuffle import shuffle
from src.print import Text
from list.list import Word

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


# Main function for the question section of the app

# Defining widgets for the question part of the program
class Widgets():

    list_of_answers = []
    list_of_questions = []
    entry = Gtk.Entry()
    label = Gtk.Label()
    current_question = 0

    # Buttons
    submit_button = Gtk.Button(label="Submit")
    next_button = Gtk.Button(label="Next")
    back_button = Gtk.Button(label="Back")
    exit_button = Gtk.Button(label="Exit")

    layout = Gtk.Grid()
    layout.set_row_spacing(5)  # Set row spacing to 10 pixels
    layout.set_column_spacing(5)
    leave_menu = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6,
                         margin_top=60)
    # menu.set_valign(Gtk.Align.CENTER)
    layout.set_valign(Gtk.Align.CENTER)
    layout.set_halign(Gtk.Align.CENTER)
    submit_button.set_valign(Gtk.Align.CENTER)
    submit_button.set_halign(Gtk.Align.CENTER)
    next_button.set_valign(Gtk.Align.CENTER)
    next_button.set_halign(Gtk.Align.CENTER)
    layout.attach(label, 0, 0, 2, 1)
    layout.attach(entry, 0, 1, 2, 1)
    layout.attach(submit_button, 0, 3, 2, 1)
    layout.attach(back_button, 0, 4, 2, 1)
    layout.attach(exit_button, 0, 5, 2, 1)

    Box.question_menu.pack_start(layout, False, False, 0)

    def update():
        count = len(Widgets.list_of_questions)
        current = Widgets.current_question
        Widgets.entry.set_text("")
        if current < count:
            ask = Text.what_is_word(Widgets.list_of_questions[Widgets.current_question])
            Widgets.label.set_text(ask)
        else:
            print("Done")
            Widgets.layout.remove(Widgets.next_button)
            Widgets.layout.remove(Widgets.submit_button)
            Widgets.layout.remove(Widgets.entry)
            Widgets.label.set_text("You Have Reached The End")
            Widgets.current_question = 0
            Widgets.list_of_question = []
            Widgets.list_of_answers = []

    # Action for submit button
    def on_submit_clicked(button):
        Widgets.layout.remove(Widgets.submit_button)
        Widgets.layout.attach(Widgets.next_button, 0, 3, 2, 1)
        Box.question_menu.show_all()
        answer = Widgets.entry.get_text()
        correct_answer = Widgets.list_of_answers[Widgets.current_question]

        if answer.lower() == correct_answer.lower():
            Widgets.label.set_text("Correct!")
        else:
            Widgets.label.set_text(Text.incorrect_line(correct_answer))

    def on_next_clicked(button):
        Widgets.layout.remove(Widgets.next_button)
        Widgets.layout.attach(Widgets.submit_button, 0, 3, 2, 1)
        Box.question_menu.show_all()

        Widgets.current_question = + Widgets.current_question + 1

        Widgets.update()

    # Runs when you press start
    def first_update(opt):
        # Widgets.label.set_text(opt.questions[current_question]["question"])
        # questions = dict(shuffle(opt))
        if Widgets.entry.get_parent() is None:
            Widgets.layout.attach(Widgets.entry, 0, 1, 2, 1)
        if Widgets.submit_button.get_parent() is None:
            Widgets.layout.attach(Widgets.submit_button, 0, 3, 2, 1)
        words = Word.wordlist(opt)

        words = dict(shuffle(words))

        for key, value in words.items():
            Widgets.list_of_answers.append(key)
            Widgets.list_of_questions.append(value)

        ask = Text.what_is_word(Widgets.list_of_questions[Widgets.current_question])
        Widgets.label.set_text(ask)

    submit_button.connect("clicked", on_submit_clicked)
    next_button.connect("clicked", on_next_clicked)


class QuestionApp():
    def __init__(self):
        pass

    def start_clicked(button, selected_list):
        Box.main_menu.set_visible(False)
        Window.main.remove(Box.main_menu)
        Window.main.add(Box.question_menu)
        Box.question_menu.set_visible(True)

        Widgets.first_update(selected_list)

        Window.main.show_all()

    def on_word_combo_changed(combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            selected_text = model[tree_iter][0]
            print("Selected value:", selected_text)
            return selected_text


class WidgetFunctions:

    # Exit button function
    def exit_clicked(button):
        Window.main.destroy()

    # Back button action
    def back_clicked(button):
        Widgets.list_of_answers = []
        Widgets.list_of_questions = []
        Window.main.remove(Box.question_menu)
        Window.main.add(Box.main_menu)
        Box.main_menu.show_all()


Widgets.exit_button.connect("clicked", WidgetFunctions.exit_clicked)
Widgets.back_button.connect("clicked", WidgetFunctions.back_clicked)
