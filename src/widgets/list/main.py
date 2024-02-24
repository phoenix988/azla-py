import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Combo:
    # Create the model for word list
    word_model = Gtk.ListStore(str)

    # Append the model
    word_model.append(["item 1"])
    word_model.append(["item 2"])
    word_model.append(["item 3"])
    word_model.append(["item 4"])

    # Create a combo box with the word list model
    word_combo = Gtk.ComboBox.new_with_model(word_model)
    word_renderer = Gtk.CellRendererText()
    word_combo.pack_start(word_renderer, True)
    word_combo.add_attribute(word_renderer, "text", 0)

    word_combo.set_active(0)
