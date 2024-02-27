from list.list import Word
from src.question import question
from src.main import Main
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Combo:
    # Create the model for word list
    word_model = Gtk.ListStore(str)

    # get the word list options
    option_items = Word.wordlistoptions()

    # Append the model with the word list
    for key, value in option_items.items():
        word_model.append([key])

    # Create the model for language list
    lang_model = Gtk.ListStore(str)
    lang_model.append(["English"])
    lang_model.append(["Azerbajani"])

    # Create a combo box with the word list model
    word_combo = Gtk.ComboBox.new_with_model(word_model)
    word_renderer = Gtk.CellRendererText()
    word_combo.pack_start(word_renderer, True)
    word_combo.add_attribute(word_renderer, "text", 0)

    # Create a combo box with the lang list model
    lang_combo = Gtk.ComboBox.new_with_model(lang_model)
    lang_renderer = Gtk.CellRendererText()
    lang_combo.pack_start(lang_renderer, True)
    lang_combo.add_attribute(lang_renderer, "text", 0)

    # Set active
    word_combo.set_active(0)
    lang_combo.set_active(0)

    # spacer
    spacer_1 = Gtk.Label()
    spacer_2 = Gtk.Label()
    spacer_3 = Gtk.Label()
