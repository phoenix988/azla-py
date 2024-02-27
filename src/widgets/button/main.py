from gi.repository import Gtk
from src.main import Main
from src.question import question
from src.widgets.window.main import Window
from src.widgets.box.main import Box
from src.widgets.entry.main import Entry
from src.widgets.func import WidgetFunctions, QuestionApp
from src.widgets.list.main import Combo
from src.shuffle import shuffle
from list.list import Word
import gi
gi.require_version('Gtk', '3.0')


class Button:
    def __init__(self):
        pass

    # Create a button
    start = Gtk.Button(label="Start")
    settings = Gtk.Button(label="Settings")
    exit = Gtk.Button(label="Exit")

    Combo.word_combo.connect("changed", QuestionApp.on_word_combo_changed)

    # Connect the functions to the start button
    start.connect("clicked", lambda button:
                  QuestionApp.start_clicked(button,
                                            QuestionApp.on_word_combo_changed(
                                                Combo.word_combo)))
    exit.connect("clicked", WidgetFunctions.exit_clicked)
