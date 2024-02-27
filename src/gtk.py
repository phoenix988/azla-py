from src.widgets.button.main import Button
from src.widgets.window.main import Window
from src.widgets.list.main import Combo
from src.widgets.box.main import Box
from src.widgets.entry.main import Entry
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


# Define a callback function for the button click event


class Azla:
    # Initialize GTK
    Gtk.init()

    # Append widgets to the main menu box
    # The first screen that you see
    Box.main_menu.pack_start(Combo.lang_combo, False, False, 0)
    Box.main_menu.pack_start(Combo.spacer_1, False, False, 0)
    Box.main_menu.pack_start(Combo.word_combo, False, False, 0)
    Box.main_menu.pack_start(Combo.spacer_2, False, False, 0)
    Box.main_menu.pack_start(Button.start, False, False, 0)
    Box.main_menu.pack_start(Combo.spacer_3, False, False, 0)
    Box.main_menu.pack_start(Button.settings, False, False, 0)
    Box.main_menu.pack_start(Button.exit, False, False, 0)

    # Add main menu box to the window
    Window.main.add(Box.main_menu)

    # Show all widgets
    Window.main.show_all()

    def run():
        # Run the GTK main loop
        Gtk.main()
